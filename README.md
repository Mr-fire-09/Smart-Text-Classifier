# 🧠 SmartTextClassifier - A Simple Machine Learning Text Categorizer

## 📌 Project Overview
SmartTextClassifier is a simple machine learning model that predicts whether an input word belongs to the category of **animal, object, or person**. It uses a **Naïve Bayes classifier** with a **bag-of-words approach** to make predictions.

## 🚀 Features
- Classifies words into **Animal**, **Object**, or **Person**.
- Uses **scikit-learn's Naïve Bayes model** for classification.
- Simple **command-line interface** for easy usage.
- Expandable with a **larger dataset**.

## 🛠 Installation & Setup
### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/SmartTextClassifier.git
cd SmartTextClassifier
```

### Step 2: Install Dependencies
Ensure you have Python installed. Then, install the required libraries:
```bash
pip install scikit-learn
```

### Step 3: Run the Classifier
Execute the following command to start the classifier:
```bash
python text_classifier.py
```

### Step 4: Input Words
Once the program runs, you can enter words like:
```
Enter a word (or 'exit' to quit): cow
'cow' is classified as: animal
```

## 📂 Project Structure
```
SmartTextClassifier/
│── text_classifier.py  # Main Python script for classification
│── README.md           # Project documentation (this file)
```

## 📈 Future Improvements
- Add more **categories** (e.g., place, food, emotion).
- Implement a **GUI** version using Tkinter or Flask.
- Train the model with a **larger dataset** for better accuracy.

## 🤝 Contributing
Feel free to **fork** this project and add improvements! 😊

## 📜 License
This project is open-source and available under the **MIT License**.

---
🚀 **Enjoy SmartTextClassifier and start classifying words intelligently!**
