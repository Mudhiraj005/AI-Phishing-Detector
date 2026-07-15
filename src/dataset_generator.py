import random
import pandas as pd

emails = []

for _ in range(1000):

    email = {
    "Urgency": random.randint(0,1),
    "FakeLink": random.randint(0,1),
    "GrammarErrors": random.randint(0,1),
    "Attachment": random.randint(0,1),
    "RequestsOTP": random.randint(0,1),
    "Typosquatting": random.randint(0,1)
    }

    score = (
    email["Urgency"] * 2 +
    email["FakeLink"] * 5 +
    email["GrammarErrors"] * 1 +
    email["Attachment"] * 1 +
    email["RequestsOTP"] * 4 +
    email["Typosquatting"] * 5
    )

    if score >= 7:
        email["Label"] = 1
    else:
        email["Label"] = 0
    
    emails.append(email)


# print(emails)

df = pd.DataFrame(emails)

# print(df)

df.to_csv('dataset/phishing.csv',index=False)

print("Dataset generated successfully")

print(df.head())