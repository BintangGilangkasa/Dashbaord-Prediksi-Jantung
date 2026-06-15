import streamlit as st
import matplotlib.pyplot as plt

def show_visualization(probability):
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.barh([0], [probability], color='red')
    ax.set_xlim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel('Tingkat Risiko Penyakit Jantung')
    st.pyplot(fig)

def show_result(prediction):

    if prediction == 1:
        st.error("⚠️ Pasien Berpotensi Mengalami Penyakit Jantung")
    else:
        st.success("✅ Pasien Tidak Terindikasi Penyakit Jantung")