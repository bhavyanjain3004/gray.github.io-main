import streamlit as st
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "product_moderation"))
sys.path.append(os.path.join(os.path.dirname(__file__), "content_moderation"))

from product_moderation.product_description_app import product_description
from content_moderation.content_moderation_app import content_moderation
from Main import main


st.set_page_config(layout="wide", page_title="Image Background")
st.markdown("""
<style>

/* ===== FRAME ===== */
.stApp {
    background-color: #9CB6E5;
}
            

/* ===== INNER CANVAS ===== */
.block-container {
    background-color: #FBF6EE;
    max-width: 1200px;
    margin: 3rem auto;
    padding: 3rem 4rem;
    border-radius: 36px;
}

/* ===== TYPOGRAPHY ===== */
html, body {
    font-family: "Inter", "Segoe UI", sans-serif;
    color: #2B2B2B;
}

h1 {
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -0.03em;
}

h2 {
    font-size: 1.8rem;
    font-weight: 600;
}

p {
    font-size: 0.95rem;
    line-height: 1.6;
}

/* ===== SIDEBAR ===== */
[data-testid="stSidebar"] {
    background-color: #8C8A3C;
}

[data-testid="stSidebar"] * {
    color: #FBF6EE;
}

/* ===== BUTTON ===== */
.stButton > button {
    background-color: #A46A43;
    color: #FFFFFF;
    border-radius: 999px;
    padding: 0.6rem 1.8rem;
    font-weight: 600;
    border: none;
}

/* ===== CARD ===== */
.card {
    background-color: #FFFFFF;
    border-radius: 28px;
    padding: 2rem;
    box-shadow: 0 18px 40px rgba(0,0,0,0.08);
}

/* ===== PASTEL VARIANTS ===== */
.card-blue {
    background-color: #E6EEFA;
}
.card-pink {
    background-color: #F7D6DC;
}
.card-butter {
    background-color: #F4E7B5;
}
/* ==============================
   FORCE ALL CONTENT TEXT TO DARK
   ============================== */

/* Headings created by st.header / st.subheader / markdown */
h1, h2, h3, h4, h5, h6 {
    color: #1F1F1F !important;
}

/* Markdown text */
[data-testid="stMarkdownContainer"] *,
.stMarkdown *,
.stMarkdown p,
.stMarkdown span {
    color: #1F1F1F !important;
}

/* Specifically fix section titles like "Input your text and image" */
[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3 {
    color: #1F1F1F !important;
    opacity: 1 !important;
}

</style>
""", unsafe_allow_html=True)


st.sidebar.success("Select a a tool below.")

page_names_to_funcs = {
    "Home": main,
    "Product Description": product_description,
    "Content Moderation": content_moderation,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()