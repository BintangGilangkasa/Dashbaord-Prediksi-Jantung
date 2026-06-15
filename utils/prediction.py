import joblib

model = joblib.load("model/logistic_regression.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_heart_disease(data):

    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    probability = model.predict_proba(data_scaled)[0][1]

    return prediction, probability