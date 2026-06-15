import streamlit as st
import joblib
from utils.visualization import show_visualization, show_result
from utils.prediction import predict_heart_disease

st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="Logo.png",
    layout="wide"
)

st.title("Dashboard Prediksi Penyakit Jantung")

st.write("""
Sistem memprediksi tingkat risiko penyakit jantung berdasarkan data kesehatan pasien.
""")

# SIDEBAR
st.sidebar.header("Input Data Pasien")

age = st.sidebar.number_input(
    "Usia",
    min_value=20,
    max_value=100,
    value=50
)

sex = st.sidebar.selectbox(
    "Jenis Kelamin",
    ["Perempuan", "Laki-laki"]
)

trestbps = st.sidebar.number_input(
    "Tekanan Darah (mmHg)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.sidebar.number_input(
    "Kolesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

thalach = st.sidebar.number_input(
    "Detak Jantung Maksimum",
    min_value=60,
    max_value=250,
    value=150
)

# Konversi ke format dataset
sex = 1 if sex == "Laki-laki" else 0

if st.sidebar.button("Prediksi Risiko"):

    data = [[
        age,
        sex,
        trestbps,
        chol,
        thalach
    ]]

    prediction, probability = predict_heart_disease(data)

    st.subheader("Hasil Prediksi")
    
    accuracy = joblib.load("model/accuracy.pkl")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "Prediksi",
            "Resiko Tinggi" if prediction == 1 else "Resiko Rendah"
        )
    
    with col2:
        st.metric(
            "Tingkat Risiko",
            f"{probability*100:.2f}%",

        )
    
    with col3:
        st.metric(
            "Akurasi Model",
            f"{accuracy*100:.2f}%",
        )