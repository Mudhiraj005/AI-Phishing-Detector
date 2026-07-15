# 🤖 AI Phishing Email Detector - Learning Journey

This document summarizes everything I learned while building my first Machine Learning project from scratch.

---

# Phase 0 - Machine Learning Fundamentals

## ✅ What is AI?

Artificial Intelligence is a system that learns patterns from data and uses those patterns to make predictions on unseen data.

---

## ✅ Features

Features are measurable characteristics used by the model to make predictions.

Example:

- Urgency
- Fake Link
- Grammar Errors
- Attachment
- Requests OTP
- Typosquatting

---

## ✅ Feature Vector

A feature vector is one complete set of feature values representing one email.

Example

```text
[1, 0, 1, 0, 1, 1]
```

---

## ✅ Dataset

A dataset is a collection of feature vectors.

Rows = Samples (Emails)

Columns = Features

---

## ✅ Labels

Labels are the correct answers (Ground Truth).

```text
0 → Legitimate

1 → Phishing
```

---

## ✅ Weights

Each feature contributes differently to the prediction.

Example:

| Feature | Weight |
|----------|--------|
|Urgency|2|
|FakeLink|5|
|GrammarErrors|1|
|Attachment|1|
|RequestsOTP|4|
|Typosquatting|5|

---

## ✅ Threshold

A threshold is the decision boundary.

Example

```text
Score >= 7

↓

Phishing
```

---

## ✅ Bias

Bias is a learnable parameter that helps shift the decision boundary.

It is learned during training together with the weights.

---

## ✅ Loss

Loss measures how wrong the model's predictions are.

Lower loss means the model is learning.

---

## ✅ Training

Training is the process where the model adjusts its weights and bias to reduce loss.

---

# Evaluation Metrics

## ✅ Accuracy

Accuracy measures the percentage of total correct predictions.

---

## ✅ Precision

Precision answers:

> Out of all emails predicted as phishing,
how many were actually phishing?

---

## ✅ Recall

Recall answers:

> Out of all actual phishing emails,
how many did the model successfully detect?

---

## ✅ F1 Score

F1 Score combines Precision and Recall into a single metric.

Useful when balancing false positives and false negatives.

---

## ✅ Confusion Matrix

Four possible outcomes.

### True Positive (TP)

Reality = Phishing

Prediction = Phishing

---

### False Positive (FP)

Reality = Legitimate

Prediction = Phishing

---

### True Negative (TN)

Reality = Legitimate

Prediction = Legitimate

---

### False Negative (FN)

Reality = Phishing

Prediction = Legitimate

---

# Python Concepts Learned

## Random Number Generation

```python
random.randint(0,1)
```

Generates either

```text
0

or

1
```

---

## Dictionaries

Used to represent one email.

```python
email = {
    "Urgency":1,
    "FakeLink":0,
    ...
}
```

---

## Lists

Used to store multiple emails.

```python
emails = []
```

---

## Pandas DataFrame

Converts a list of dictionaries into a table.

```python
df = pd.DataFrame(emails)
```

---

## Saving CSV

```python
df.to_csv("dataset/phishing.csv", index=False)
```

### index=False

Prevents Pandas from writing the index column into the CSV.

---

## Reading CSV

```python
dataset = pd.read_csv("dataset/phishing.csv")
```

---

# Machine Learning Workflow

## Feature Matrix (X)

```python
X = dataset.drop("Label", axis=1)
```

Contains only input features.

---

## Label Vector (y)

```python
y = dataset["Label"]
```

Contains the correct answers.

---

## axis=1

Represents columns.

Used when removing the Label column.

---

## axis=0

Represents rows.

---

# Logistic Regression

Imported using

```python
from sklearn.linear_model import LogisticRegression
```

Created using

```python
model = LogisticRegression()
```

---

## Training

```python
model.fit(X, y)
```

The model learns from the dataset.

---

## Prediction

```python
model.predict(...)
```

Returns

```text
0 → Legitimate

1 → Phishing
```

---

## Prediction Probability

```python
model.predict_proba(...)
```

Returns

```text
[
Probability(Legitimate),
Probability(Phishing)
]
```

Example

```text
[[0.22,0.78]]
```

↓

22% Legitimate

78% Phishing

---

# Saving the Model

```python
joblib.dump(model, "models/phishing_model.pkl")
```

Stores the trained model on disk.

---

# Loading the Model

```python
model = joblib.load("models/phishing_model.pkl")
```

Loads the trained model without retraining.

---

# Project Structure

```text
AI-Phishing-Detector/

dataset/
    phishing.csv

models/
    phishing_model.pkl

src/
    dataset_generator.py
    train.py
    predict.py

README.md
AI_LEARNING_JOURNEY.md
```

---

# What I Built

✅ Dataset Generator

✅ Logistic Regression Training

✅ Model Saving

✅ Model Loading

✅ Interactive Prediction System

✅ Prediction Probability

✅ Confidence Score

✅ Risk Classification

---

# Skills Gained

- Python Programming
- Pandas
- NumPy (Basics)
- Scikit-Learn
- Logistic Regression
- Data Engineering
- Feature Engineering
- Model Persistence
- Probability-Based Predictions
- Software Project Structure
- Git & GitHub Project Organization

---

# Future Improvements

- Input Validation
- Train/Test Split
- Accuracy Report
- Precision & Recall Report
- F1 Score Report
- Confusion Matrix Visualization
- GUI Version
- Web Version (Flask/FastAPI)
- Real Email Dataset
- Deep Learning Version

---

# Version

**AI Phishing Detector v1.0**

Built as my first end-to-end Machine Learning project while learning Python, Pandas, and Scikit-Learn.