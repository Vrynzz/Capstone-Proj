import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="Filming Locations Guidelines"
)
# endregion <--------- Streamlit App Configuration --------->

pdf_viewer("data/GuideToFilming040321.pdf")
