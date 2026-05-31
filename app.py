import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Hype vs Reality",layout="centered")

st.title("Echoes & Reality ⚖️")
st.markdown("C# Ekosistemindeki makale veya sorun başlıklarının **Hype** mı yoksa **Reality** mi olduğunu test edin.")

with st.form(key="analiz_formu"):
    test_basligi = st.text_input("Test edilecek başlığı buraya girin (Örn: Building AI Agents in .NET):")
    submit_buton = st.form_submit_button(label="Analiz Et")



if submit_buton:
    if test_basligi:
        with st.spinner("Yapay Zeka Başlığı Analiz Ediyor..."):

            model = joblib.load("models/model.joblib")
            vektor_donusturucu = joblib.load("models/vektor.joblib")
            hype_merkez = joblib.load("models/hype_merkez.joblib")
            reality_merkez = joblib.load("models/reality_merkez.joblib")

            test_vektoru = vektor_donusturucu.transform([test_basligi])
            tahmin = model.predict(test_vektoru)[0]

            hype_metre = cosine_similarity(test_vektoru,hype_merkez)[0][0]
            reality_metre = cosine_similarity(test_vektoru,reality_merkez)[0][0]

            st.success("Analiz Tamamlandı!")

            if tahmin == 1:
                st.subheader("Sonuç: Hype 🚨")
            else:
                st.subheader("Sonuç: Reality 🧪")

            st.write("---")

            col1, col2 = st.columns(2)
            hype_yuzde_metni = f"{hype_metre:.2%}"
            reality_yuzde_metni = f"{reality_metre:.2%}"
            col1.metric(label="Hype Merkeze Yakınlık",value=hype_yuzde_metni)
            col2.metric(label="Reality Merkeze Yakınlık",value=reality_yuzde_metni)
            
else:
    print("Lütfen analiz etmek için bir başlık girin!")