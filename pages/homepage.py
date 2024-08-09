import streamlit as st
from PIL import Image

def homepage():
    #st.image("images/softmavi.png", use_column_width=True)
    st.title("Sonsuz Döngü")
    
    st.subheader("Ekibimiz")


    team = Image.open(r"images\Ekip.jpeg")
    #resized_team = team.resize((500, 250)) 

    
    # Kolon genişliklerini belirleyelim: 2/3 ve 1/3
    #col1, col2 = st.columns([2, 1])

    # İlk kolon
    #with col1:
    st.image(team, caption="Ekibimiz", use_column_width=True)
        # Bu kolona eklemek istediğin içerikleri buraya ekleyebilirsin

    # İkinci kolon
    #with col2:
    st.write("Takımımız 2024 yılında Mayıs ayında kuruldu. SOGEP projesi olan yazılım ile geleceğe atılım projesi  sayesinde tanıştık ve bir araya geldik . Takımımız Güncel Teknolojiler ve Yapay zeka  modellerini kullanarak yazılım dünyasına yenilikçi projeler üretmek amacıyla kuruldu. ")
        # Bu kolona eklemek istediğin içerikleri buraya ekleyebilirsin

    st.subheader("Projemiz")

    st.write("""
    Bu proje, sosyal medyada şiddet eğilimli olan, tehdit altında hisseden veya intihara meyilli kişilerin paylaşımlarını tespit ederek yetkili birimlere ulaştırılmasını ve tedbir alınmasını sağlamayı amaçlamaktadır.
    """)

    #if st.button("Modeli Deneyin"):
        #model_page()
        #st.experimental_set_query_params(page="model_page")
        #st.experimental_rerun()