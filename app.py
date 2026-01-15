from flask import Flask, request, render_template
from model import predict_emotion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = None
    score = None

    if request.method == "POST":
        text = request.form["text"]
        result = predict_emotion(text)
        emotion = result['label']
        score = round(result['score'] * 100, 2)

    return render_template("index.html", emotion=emotion, score=score)

if __name__ == "__main__":
    app.run(debug=True)
