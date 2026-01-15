from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def predict_emotion(text):
    result = classifier(text)[0]
    result = sorted(result, key=lambda x: x['score'], reverse=True)
    return result[0]
