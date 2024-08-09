import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from PIL import Image #img için kullanılan bir kütüphane

st.set_page_config(initial_sidebar_state="collapsed")

# Load the logo
#logo = Image.open('images/softmavi.png')

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join("images\softbluelogo.svg")

styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
        "margin": "2px",
        "height": "70px", 
        "width": "250px", 
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}

# Diğer Sayfaları import edelim
from pages.homepage import homepage
from pages.model_page import model_page
from pages.statistics_page import statistics_page

# Navbar
page = st_navbar(["Ana Sayfa", "Modeli Deneyin", "İstatistikler"], styles=styles,logo_path=logo_path)


# Seçilen sayfaya gidelim
if page == "Ana Sayfa":
    homepage()
elif page == "Modeli Deneyin":
    model_page()
elif page == "İstatistikler":
    statistics_page()
else:
    homepage()


