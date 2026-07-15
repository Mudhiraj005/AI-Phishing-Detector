import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression

dataset = pd.read_csv('dataset/phishing.csv')

# print(dataset.head())

X = dataset.drop("Label", axis=1)

y = dataset["Label"]

# print(X.head())

# print("-----------------")

# print(y.head())

model = LogisticRegression()

model.fit(X,y)
print("AI Model Trained Successfully!")

joblib.dump(model,"models/phishing_model.pkl")
print("Model saved successfully!")

