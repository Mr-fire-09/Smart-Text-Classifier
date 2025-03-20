from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

# Training Data
words = ["dog", "cat", "elephant", "car", "table", "chair", "John", "Alice", "doctor", "lion", "phone"]
labels = ["animal", "animal", "animal", "object", "object", "object", "person", "person", "person", "animal", "object"]

# Train Model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(words, labels)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    word = data.get("word", "")
    if word:
        prediction = model.predict([word])[0]
        return jsonify({"result": prediction})
    return jsonify({"result": "Unknown"})

if __name__ == "__main__":
    app.run(debug=True)
