Emotion Detection from Text

This project is a web-based application that detects human emotions from text input using a fine-tuned Transformer model. The model is trained on the GoEmotions dataset and served through a Flask web interface for real-time predictions.

Overview

The system classifies user-entered text into emotional categories such as joy, sadness, anger, fear, love, and surprise. It uses a pretrained language model that has been fine-tuned on an emotion-annotated dataset to achieve accurate and reliable results.

Features

Emotion classification from raw text input

Fine-tuned Transformer (DistilBERT) model

Flask-based web interface

Simple and extensible project structure

Technology Stack

Python 3.9 or higher

PyTorch

HuggingFace Transformers

HuggingFace Datasets (GoEmotions)

Flask

HTML/CSS

Project Structure
emotion_detection/
│
├── app.py
├── model.py
├── train.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html

Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/emotion-detection.git
cd emotion-detection
pip install -r requirements.txt

Dataset

The project uses the GoEmotions dataset released by Google, available through HuggingFace:

from datasets import load_dataset
dataset = load_dataset("go_emotions")


The dataset contains more than 58,000 labeled text samples across 28 emotion classes.

Model Training

To fine-tune the model on the dataset, run:

python train.py


The trained model will be saved in the emotion_model/ directory.

Training time depends on hardware:

GPU: approximately 10–15 minutes

CPU: approximately 1–2 hours

Running the Application

Start the Flask server:

python app.py


Then open your browser and go to:

http://127.0.0.1:5000/

Example

Input:

I am feeling very happy today.


Output:

Emotion: joy
Confidence: 92%

Resume Description

Built an emotion detection system using Transformer-based NLP models to classify emotional states from text and deployed it as a real-time web application using Flask.

Future Improvements

Multi-label emotion classification

REST API support

React-based frontend

Model explainability using SHAP or LIME

Cloud deployment

License

This project is released under the MIT License.

Contributing

Pull requests are welcome. For major changes, please open an issue first.

Author

Prathmesh Ramchandra
AIML Engineer | Python | NLP