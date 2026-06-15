import joblib

scaler = joblib.load("model/logistic_regression.pkl")

def preprocess_input(data):
    
    data_scaled = scaler.transform(data)

    return data_scaled