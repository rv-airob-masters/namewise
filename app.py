import streamlit as st
from groq import Groq
import re
import json

# Load Groq API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=GROQ_API_KEY)

if "text_input" not in st.session_state:
    st.session_state["text_input"] = ""

st.set_page_config(page_title="NameWise", page_icon="🔍")
st.title("🔍 NameWise : Smart insights into any name")

st.write("Enter a sentence containing one or more person names. The app will extract all names and provide their origin, common usage, and meaning.")

text_input = st.text_area("Enter your text here:", height=100, key="text_input")

col1, col_spacer, col2 = st.columns([1, 6, 1])
with col1:
    analyze_clicked = st.button("Analyze")
with col2:
    reset_clicked = st.button("Reset")

# Handle reset BEFORE rendering the widget
if reset_clicked:
    # Remove the key so the widget will be empty on rerun
    if "text_input" in st.session_state:
        del st.session_state["text_input"]
    st.rerun()



def extract_names_with_llm(text):
    prompt = (
        "/no_think"
        "Extract all person names mentioned in the following text as a JSON array of strings."
        "If there are no names, reply with an empty array [].\n\n"
        "Respond ONLY with the JSON array. Do not include any explanation or reasoning. "
        f"Text: {text}\n\nNames:"
    )
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        temperature=0.0,
    )
    content = response.choices[0].message.content.strip()
    #print("LLm resposnse for names:", content)
    # Extract Python list from response
    try:
        names = eval(content, {"__builtins__": {}})
        if isinstance(names, list):
            # Remove empty/whitespace-only names
            names = [n.strip() for n in names if n.strip()]
            return names
    except Exception:
        pass
    return []

def get_name_info_with_llm(name):
    prompt = (
        f"Provide the following information about the person name in JSON format:\n"
        f"- origin: the country or region where the name originates\n"
        f"- usage: where the name is commonly used\n"
        f"- meaning: the meaning of the name\n"
        f"If any information is unknown, use 'unknown'.\n\n"
        f"Name: {name}\n\n"
        f"Respond only with a JSON object."
    )
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=256,
        temperature=0.2,
    )
    # Try to parse the JSON from the response
    try:
        content = response.choices[0].message.content.strip()
        json_str = re.search(r"\{.*\}", content, re.DOTALL).group(0)
        info = json.loads(json_str)
    except Exception:
        info = {"origin": "unknown", "usage": "unknown", "meaning": "unknown"}
    return info


if analyze_clicked:
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Extracting names..."):
            names = extract_names_with_llm(text_input)
        if not names:
            st.error("No names found in the text.")
        else:
            st.success(f"Extracted names: {', '.join(names)}")
            st.header("Name Details")
            for name in names:
                with st.spinner(f"Querying Groq LLM for details about {name}..."):
                    info = get_name_info_with_llm(name)
                
                with st.expander(f"{name}", expanded=False):
                    st.markdown(f"### Details for **{name}**")
                    st.info(f"**Origin:** {info.get('origin', 'unknown')}")
                    st.info(f"**Common Usage:** {info.get('usage', 'unknown')}")
                    st.info(f"**Meaning:** {info.get('meaning', 'unknown')}")
