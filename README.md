# 🧠 Emotion Detection from Text

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg?style=for-the-badge&logo=flask&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗_Transformers-Latest-orange.svg?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**A powerful NLP-based web application that detects human emotions from text using state-of-the-art Transformer models.**

[Demo](#-run-the-web-app) • [Installation](#-installation) • [Features](#-features) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎭 **Multi-Emotion Detection** | Detects 7 core emotions: *anger*, *disgust*, *fear*, *joy*, *neutral*, *sadness*, and *surprise* |
| 🚀 **Real-Time Predictions** | Instant emotion analysis with confidence scores |
| 🤖 **Pre-trained Model** | Powered by `distilroberta-base` fine-tuned on emotion datasets |
| 🌐 **Web Interface** | Clean, intuitive Flask-based UI for easy interaction |
| ⚡ **Lightweight** | Minimal dependencies, easy to deploy anywhere |

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core programming language |
| **Flask** | Web framework for the application |
| **HuggingFace Transformers** | NLP model inference |
| **PyTorch** | Deep learning backend |
| **HTML/CSS** | Frontend interface |

</div>

---

## 📁 Project Structure

```
emotion_detection/
├── 📄 app.py              # Flask web application
├── 🧠 model.py            # Emotion prediction logic
├── 📋 requirements.txt    # Python dependencies
├── 📖 README.md           # Project documentation
└── 📂 templates/
    └── 🖼️ index.html      # Web interface template
```

---

## � Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/emotion-detection.git
   cd emotion-detection
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📖 Usage

### 🌐 Run the Web App

```bash
python app.py
```

Open your browser and navigate to:

> 🔗 **http://127.0.0.1:5000/**

### 🐍 Use as a Python Module

```python
from model import predict_emotion

# Get emotion prediction
text = "I am feeling very happy today!"
result = predict_emotion(text)

print(f"Emotion: {result['label']}")
print(f"Confidence: {result['score'] * 100:.2f}%")
```

---

## 🧪 Example

<table>
<tr>
<td width="50%">

### Input
```
I am feeling very happy today!
```

</td>
<td width="50%">

### Output
```
🎭 Emotion: joy
📊 Confidence: 92%
```

</td>
</tr>
</table>

### More Examples

| Input Text | Detected Emotion | Confidence |
|------------|------------------|------------|
| *"I can't believe they did that to me!"* | anger | 87% |
| *"This is so scary..."* | fear | 91% |
| *"What a pleasant surprise!"* | surprise | 89% |
| *"I miss my old friends"* | sadness | 85% |

---

## 🤖 Model Details

This project uses the **[j-hartmann/emotion-english-distilroberta-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)** model from HuggingFace:

- **Architecture**: DistilRoBERTa (distilled version of RoBERTa)
- **Training Data**: Emotion-labeled English text datasets
- **Emotions**: anger, disgust, fear, joy, neutral, sadness, surprise
- **Performance**: Optimized for inference speed while maintaining accuracy

---

## 🔮 Future Improvements

- [ ] 🏷️ Multi-label emotion classification
- [ ] ⚛️ React/Next.js frontend upgrade
- [ ] 📡 REST API endpoints for mobile apps
- [ ] 🔍 Model explainability (SHAP/LIME integration)
- [ ] ☁️ Cloud deployment (AWS/GCP/Heroku)
- [ ] 📊 Emotion trends visualization
- [ ] 🌍 Multi-language support

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

<div align="center">

**Prathmesh**

*AIML| Python | NLP*

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)

</div>

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and Python

</div>
