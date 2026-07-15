import pandas as pd
import joblib

model = joblib.load("models/phishing_model.pkl")

def get_user_input():
    return {
        "Urgency": int(input("Enter Urgency (0/1):")),
        "FakeLink": int(input("Enter Fake Link (0/1):")),
        "GrammarErrors": int(input("Enter Grammar Errors (0/1):")),
        "Attachment": int(input("Enter Attachment (0/1):")),
        "RequestsOTP": int(input("Enter Requests OTP (0/1):")),
        "Typosquatting": int(input("Enter Typosquatting (0/1):"))
    }


def predict_email(model,new_email):
    probability = model.predict_proba(new_email)
    return probability


def display_results(probability):
    print("==================================")
    print("       AI PHISHING DETECTOR       ")
    print("==================================")

    confidence = probability[0][1] * 100

    if probability[0][1] > 0.5:
        print("Prediction : Phishing")
    else:
        print("Prediction : Legitimate")


    print(f"Confidence: {confidence:.2f}%")

    if(confidence > 70):
        print("Risk Level: High")
    elif(confidence > 40): 
        print("Risk Level: Medium")
    else:
        print("Risk Level: Low")

def main():
    email = pd.DataFrame([get_user_input()])
    probability = predict_email(model,email)
    display_results(probability)


if __name__ == "__main__":
    main()