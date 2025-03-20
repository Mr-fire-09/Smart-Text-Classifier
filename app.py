from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

app = Flask(__name__)

# Training Data
words = [
    "dog", "cat", "elephant", "lion", "tiger", "giraffe", "zebra", "monkey", "kangaroo", "penguin",
    "car", "table", "chair", "phone", "pen", "laptop", "book", "cup", "bottle", "keyboard",
    "John", "Alice", "doctor", "teacher", "engineer", "nurse", "artist", "lawyer", "scientist", "student"
]
labels = [
    "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal",
    "object", "object", "object", "object", "object", "object", "object", "object", "object", "object",
    "person", "person", "person", "person", "person", "person", "person", "person", "person", "person"
]

# Train Model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(words, labels)

# Debug: Check model predictions on training data
for word, label in zip(words, labels):
    prediction = model.predict([word])[0]
    print(f"Word: {word}, True Label: {label}, Predicted Label: {prediction}")

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
    app.run(host="0.0.0.0", port=5000, debug=True)
