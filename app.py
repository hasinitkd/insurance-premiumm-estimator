from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="InsureWise", page_icon="🛡️", layout="wide")

# Hide Streamlit chrome and padding so the site fills the page
st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    </style>""",
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "insurewise.html").read_text(encoding="utf-8")
components.html(html, height=4200, scrolling=True)
