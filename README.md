# 📖 AI Story Generator

An AI-powered story generator built with **Streamlit**, **Groq**, and **Hugging Face**, that creates illustrated stories with AI-generated images for every scene.

---

## 🚀 Features

- Generate stories split into multiple scenes
- AI-generated images for each scene via Stable Diffusion XL
- **Character creator** — define custom characters before generating
- **Story length control** — Short (3), Medium (5), or Long (7) scenes
- **Genre selector** — Fantasy, Horror, Adventure, Sci-fi, Romance, Mystery, Comedy
- **Download as PDF** — export the full story with images
- Dark, modern UI

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-story-generator.git
cd ai-story-generator
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
HF_API_KEY=your_huggingface_token_here
```

> - Get your Groq API key from [console.groq.com](https://console.groq.com)
> - Get your Hugging Face token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
ai-story-generator/
├── app.py                      # Main Streamlit app
├── components/
│   ├── __init__.py             # Makes components a Python package
│   ├── story_generator.py      # Groq LLM story generation
│   ├── image_generator.py      # Hugging Face image generation
│   ├── pdf_generator.py        # PDF export with reportlab
│   └── ui.py                   # All UI rendering components
├── .env                        # API keys (not committed to git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🎛️ Controls

| Control | Description |
|---|---|
| Story Topic | Enter any topic or idea for your story |
| Genre | Pick the story genre |
| Length | Short (3 scenes), Medium (5 scenes), Long (7 scenes) |
| Character Creator | Add custom characters with name, role, and description |
| Generate Story | Creates story + AI images for each scene |
| Download as PDF | Exports full story with images as a PDF file |

---

## 📦 Requirements

```
streamlit
groq
python-dotenv
requests
reportlab
```

---

## Work Flow
[View on Eraser![](https://app.eraser.io/workspace/Rbwtj4qK6GaRhBOin8T1/preview?diagram=BZLtMUsQSI8v-XXmVoMZa&type=embed)](https://app.eraser.io/workspace/Rbwtj4qK6GaRhBOin8T1?diagram=BZLtMUsQSI8v-XXmVoMZa)





## 🤖 Models Used

| Purpose | Model |
|---|---|
| Story Generation | Groq — llama-3.3-70b-versatile |
| Image Generation | Hugging Face — stabilityai/stable-diffusion-xl-base-1.0 |

---

## ⚠️ Important Notes

- Images are generated via Hugging Face Inference API — first load may take time as the model warms up
- A `503` error means the model is loading — the app retries automatically
- **Never commit your `.env` file** — add it to `.gitignore`
- PDF export includes all scene text and AI-generated images

---

## 📄 License

MIT
