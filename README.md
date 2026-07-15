# 🤖 AI Phishing Email Detector

An end-to-end Machine Learning project that detects whether an email is **Phishing** or **Legitimate** using **Logistic Regression**.

This project was built from scratch while learning Python, Pandas, and Scikit-Learn. It includes dataset generation, model training, model persistence, and interactive prediction.

---

## 📌 Features

- ✅ Generate a synthetic phishing email dataset
- ✅ Train a Logistic Regression model
- ✅ Save the trained model using Joblib
- ✅ Load the saved model without retraining
- ✅ Predict phishing emails interactively
- ✅ Display prediction confidence
- ✅ Display risk level (Low / Medium / High)

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- NumPy
- Scikit-Learn
- Joblib

---

## 📂 Project Structure

```text
AI-Phishing-Detector/
│
├── dataset/
│   └── phishing.csv
│
├── models/
│   └── phishing_model.pkl
│
├── src/
│   ├── dataset_generator.py
│   ├── train.py
│   └── predict.py
│
├── AI_LEARNING_JOURNEY.md
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mudhiraj05/AI-Phishing-Detector.git

cd AI-Phishing-Detector
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Generate Dataset

```bash
python src/dataset_generator.py
```

This generates

```text
dataset/phishing.csv
```

---

## 4️⃣ Train the AI Model

```bash
python src/train.py
```

This creates

```text
models/phishing_model.pkl
```

---

## 5️⃣ Predict Emails

```bash
python src/predict.py
```

Example

```text
Enter Urgency (0/1): 1
Enter Fake Link (0/1): 1
Enter Grammar Errors (0/1): 0
Enter Attachment (0/1): 0
Enter Requests OTP (0/1): 1
Enter Typosquatting (0/1): 1

==================================
       AI PHISHING DETECTOR
==================================

Prediction : Phishing

Confidence : 96.42%

Risk Level : HIGH
```

---

# 🧠 Machine Learning Workflow

```text
Generate Dataset
        │
        ▼
Train Logistic Regression
        │
        ▼
Save Trained Model
        │
        ▼
Load Model
        │
        ▼
Predict New Email
        │
        ▼
Confidence Score
        │
        ▼
Risk Level
```

---

# 📊 Features Used

| Feature | Description |
|----------|-------------|
| Urgency | Email creates urgency or pressure |
| FakeLink | Suspicious or fake URL |
| GrammarErrors | Poor grammar or spelling mistakes |
| Attachment | Unexpected attachment |
| RequestsOTP | Requests OTP or sensitive information |
| Typosquatting | Fake domain resembling a legitimate one |

---

# 🏗️ Project Components

## Dataset Generator

Creates a synthetic dataset of phishing and legitimate emails using weighted feature scoring.

---

## Model Training

- Loads the dataset
- Separates features and labels
- Trains a Logistic Regression model
- Saves the trained model

---

## Prediction System

- Loads the saved model
- Accepts user input
- Predicts phishing probability
- Displays confidence and risk level

---

# 📚 What I Learned

- Python Programming
- Dictionaries & Lists
- Pandas DataFrames
- CSV Handling
- Logistic Regression
- Feature Engineering
- Model Training
- Model Persistence (Joblib)
- Probability-Based Predictions
- Software Project Structure
- Git & GitHub Workflow

For detailed learning notes, see:

```text
AI_LEARNING_JOURNEY.md
```

---

# 🔮 Future Improvements

- Input Validation
- Real Email Dataset
- Train/Test Split
- Accuracy, Precision, Recall & F1 Score
- Confusion Matrix
- GUI Version (Tkinter)
- Web Version (Flask / FastAPI)
- Deep Learning Model
- Email File (.eml) Analysis

---

# 📄 License

This project is open-source and intended for educational purposes.

---

# 👨‍💻 Author

**Vanam Chenchu Puneeth**

Built as my first end-to-end Machine Learning project while learning AI and Python.