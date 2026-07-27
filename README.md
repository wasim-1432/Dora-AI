# 🤖 Dora AI Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Groq-AI-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Gradio-Frontend-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/OpenCV-Vision-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
</p>

<p align="center">
An Intelligent Voice + Vision AI Assistant powered by <b>Groq LLM</b>, <b>Whisper</b>, <b>OpenCV</b>, and <b>Gradio</b>.
</p>

---

# 🌟 Overview

**Dora AI Assistant** is a smart AI-powered assistant that allows users to communicate naturally using **voice commands**.

The assistant records the user's speech, converts it into text using **Groq Whisper**, processes the request using **Groq Llama 3.3**, and replies with both **text** and **AI-generated voice**.

For vision-related questions, Dora automatically opens the webcam, captures an image, analyses it using a Vision AI model, and returns an intelligent response.

---

# ✨ Features

## 🎤 Voice Assistant

- 🎙️ Real-time voice recording
- ⚡ Fast Speech-to-Text
- 💬 Natural conversations
- 🎧 Automatic silence detection
- 🔄 Continuous interaction

---

## 🤖 AI Chat

- 🧠 Powered by Groq Llama 3.3
- 💡 Intelligent responses
- ✨ Short and concise answers
- 🌍 General knowledge support
- 🗣️ Natural language understanding

---

## 📷 Vision AI

Automatically activates the webcam whenever image understanding is required.

### Example Questions

- What is in my hand?
- How many pens are in my hand?
- What colour is my shirt?
- Is anyone behind me?
- Count the objects on my desk.
- What do you see around me?
- Do you see a laptop?
- What object am I holding?

---

## 🔊 AI Voice Reply

- 🎤 ElevenLabs Voice
- 🔄 Automatic Google TTS fallback
- 🎵 Natural speech output
- ⚡ Fast audio generation

---

## 💻 Modern User Interface

- 🌙 Dark Theme
- 🎨 Responsive Design
- 🎤 One-click Recording
- 🔊 Audio Player
- ⚡ Smooth User Experience

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Backend |
| 🤖 Groq API | LLM & Whisper |
| 🎤 SpeechRecognition | Voice Recording |
| 🎵 PyDub | Audio Processing |
| 📷 OpenCV | Vision AI |
| 🔊 ElevenLabs | Text-to-Speech |
| 🌐 Gradio | Frontend |
| 🎮 Pygame | Audio Playback |

---

# 📂 Project Structure

```text
Dora-AI-Assistant/
│
├── main.py
├── ai_agent.py
├── tools.py
├── speech_to_text.py
├── text_to_speech.py
├── .env
├── pyproject.toml
├── README.md
│
├── sample.jpg
├── captured_image.jpg
├── audio_question.mp3
└── final.mp3
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Dora-AI-Assistant.git

cd Dora-AI-Assistant
```

---

## Install Dependencies

Using pip

```bash
pip install -r requirements.txt
```

or using uv

```bash
uv sync
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

ELEVENLABS_API_KEY=YOUR_ELEVENLABS_API_KEY
```

---

# ▶️ Run the Project

```bash
python main.py
```

or

```bash
uv run main.py
```

---

# 💬 Example Questions

## 🤖 General AI

- Who is the Prime Minister of India?
- Explain Artificial Intelligence.
- What is Machine Learning?
- What is Python?
- What is LangChain?
- What is Groq AI?

---

## 📷 Vision AI

- What is in my hand?
- How many pens are in my hand?
- Count the objects.
- Is anyone behind me?
- What colour is my shirt?
- Describe my surroundings.
- What is on my table?
- Do you see a bottle?

---

# 🔄 System Workflow

```text
🎤 User Speaks
      │
      ▼
Speech Recording
      │
      ▼
Groq Whisper (Speech-to-Text)
      │
      ▼
Intent Detection
      │
 ┌───────────────┐
 │               │
 ▼               ▼
Vision Query   Normal Query
 │               │
 ▼               ▼
OpenCV        Groq LLM
 │               │
 └──────┬────────┘
        ▼
 AI Response
        ▼
Text-to-Speech
        ▼
🔊 Voice Output
```

---

# 🎯 Key Highlights

- ✅ Voice-Based AI Assistant
- ✅ Vision AI
- ✅ AI Voice Response
- ✅ Automatic Webcam Detection
- ✅ Speech-to-Text
- ✅ Text-to-Speech
- ✅ Groq Integration
- ✅ Whisper Integration
- ✅ Fast Response Time
- ✅ Beautiful Gradio Interface

---

# 📸 Demo

> Add screenshots of your project here.

Example:

```
screenshots/
│
├── home.png
├── voice_chat.png
├── vision_demo.png
└── response.png
```

---

# 🔮 Future Improvements

- 🎥 Live Camera Streaming
- 😊 Face Detection
- 😄 Emotion Recognition
- 📄 OCR
- 🌍 Multi-language Support
- 💾 Conversation Memory
- 🌦 Weather Updates
- 📰 News Assistant
- 🖥 Desktop Automation
- 📱 Mobile Responsive UI

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 👨‍💻 Author

## Mohd Wasim

💻 AI Developer | Python | Computer Vision | LLMs

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository on GitHub.

It helps others discover the project and motivates future development.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ❤️ Acknowledgements

Special thanks to the amazing open-source tools that made this project possible.

- 🤖 Groq
- 🎤 Whisper
- 🌐 Gradio
- 📷 OpenCV
- 🔊 ElevenLabs
- 🐍 Python

---

<p align="center">
Made with ❤️ by <b>Mohd Wasim</b>

⭐ Don't forget to Star the Repository ⭐
</p>
