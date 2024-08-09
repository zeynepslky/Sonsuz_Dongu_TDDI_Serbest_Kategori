import streamlit as st
from simpletransformers.classification import ClassificationModel

def model_page():
    st.title("Modeli Deneyin")
    st.write("Lütfen Türkçe bir metin girin ve modelimizin analizini görün.")
    
    # Modeli yükleyelim
    @st.cache_resource
    def load_model():
        model = ClassificationModel("bert", "./bert_model", use_cuda=False)
        return model

    model = load_model()

    # Kullanıcıdan metin alalım
    input_text = st.text_area("Metni Girin", "Buraya bir metin yazın...")

    if st.button("Tahmin Et"):
        # Modelle tahmin yapalım
        prediction, _ = model.predict([input_text])
        st.write(f"Tahmin: {prediction[0]}")