🧠 Emotion Detection from Text

An NLP-based web application that detects human emotions from text using a fine-tuned Transformer model and serves predictions through a Flask web interface.

🚀 Features

Detects emotions like happy, sad, angry, fear, love, surprise, etc.

Fine-tuned Transformer model (DistilBERT) on GoEmotions dataset.

Real-time predictions via web UI.

Easy to deploy and extend.

🛠 Tech Stack

Python 3.9+

HuggingFace Transformers

PyTorch

Datasets (GoEmotions)

Flask

HTML/CSS

📁 Project Structure
emotion_detection/
│
├── app.py
├── model.py
├── train.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html

📦 Installation
git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
pip install -r requirements.txt

📊 Dataset

We use the GoEmotions dataset by Google, available via HuggingFace:

from datasets import load_dataset
dataset = load_dataset("go_emotions")


Contains 58k+ labeled Reddit comments with 28 emotion classes.

🧠 Model Training

To fine-tune the model:

python train.py


The trained model will be saved in:

emotion_model/

🌐 Run the Web App
python app.py


Open browser at:
👉 http://127.0.0.1:5000/

🧪 Example

Input:

I am feeling very happy today!


Output:

Emotion: joy
Confidence: 92%

📝 Resume Description

Built an Emotion Detection system using Transformer-based NLP models to classify emotional sentiment from text with a Flask-based real-time web interface.

🔮 Future Improvements

Multi-label emotion classification

React frontend

REST API for mobile apps

Model explainability (SHAP/LIME)

Cloud deployment

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

📄 License

MIT License

🎉 Author

Prathmesh Ramchandra
AIML Engineer | Python | NLP