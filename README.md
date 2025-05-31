# 🔍 NameWise: Smart Insights into Any Name

NameWise is a Streamlit application that extracts person names from text and provides detailed information about their origin, common usage, and meaning.

## 🌟 Features

- Extracts all person names from input text using Groq's LLM capabilities
- Provides detailed information for each name:
  - Origin (country/region where the name originates)
  - Common usage (where the name is typically used)
  - Meaning (the semantic meaning behind the name)
- Clean, intuitive user interface with expandable details for each name

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Groq API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rv-airob-masters/namewise.git
   cd namewise
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Groq API key:
   - Create a `.streamlit/secrets.toml` file with your API key:
     ```toml
     GROQ_API_KEY = "your-groq-api-key"
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## 💡 Practical Applications

### NLP Integration

NameWise can be integrated into larger NLP pipelines to enhance user experiences by providing personalized insights about names mentioned in conversations or documents.

### Speech-to-Text Integration

Combine NameWise with speech recognition systems to:
1. Convert audio to text using speech-to-text APIs
2. Pass the transcribed text to NameWise for name extraction and analysis
3. Provide real-time information about names mentioned in conversations

Example workflow:
```python
# Pseudo-code for audio integration
from speech_recognition import Recognizer, AudioFile
import requests

# 1. Convert speech to text
recognizer = Recognizer()
with AudioFile("conversation.wav") as source:
    audio = recognizer.record(source)
text = recognizer.recognize_google(audio)

# 2. Extract and analyze names using NameWise API
names_info = process_with_namewise(text)

# 3. Present information to user
for name, info in names_info.items():
    print(f"Name: {name}")
    print(f"Origin: {info['origin']}")
    print(f"Usage: {info['usage']}")
    print(f"Meaning: {info['meaning']}")
```

### Customer Service Enhancement

Deploy NameWise in customer service applications to:
- Automatically identify customer names during conversations
- Provide agents with cultural context about customer names
- Create more personalized and culturally sensitive interactions

### Educational Tool

Use NameWise as an educational tool to:
- Learn about the cultural and historical significance of names
- Explore the etymology and meaning of names across different cultures
- Enhance multicultural understanding and appreciation

## 🛠️ How It Works

NameWise uses Groq's LLM models to:
1. Extract person names from input text
2. Generate detailed information about each name

The application leverages prompt engineering to ensure accurate name extraction and detailed information retrieval.

## 📝 License

[MIT License](LICENSE)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.