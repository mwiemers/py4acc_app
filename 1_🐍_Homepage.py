import streamlit as st
from load_css import local_css

st.set_page_config(
    page_title='Digital Skills Lab Python for Accounting workshops',
    page_icon="🐍"
)

local_css("css/style.css")

st.title("DSL Python for Accounting workshops")


st.markdown(
    """
    **Michael Wiemers**  
    Learning Development Lead (Academic Partnerships)  
    """)

st.image("img/lse_dsl_logo.png", width=400)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/python_logo.png", width=150)


st.markdown(
    """
    Python is pre-installed on all teaching PCs in the PC teaching rooms.
    
    If you wish to install Python on your personal laptop, plese follow the instructions on this website to install Anaconda to use Python + VS Code + Jupyter Notebooks.
    
    We recommend to set apart 15 minutes to work through this tutorial.

    Please work through the pages from the sidebar menu for information about:
    * Why Python is such a popular programming language and why you should learn it.
    * How you can install Anaconda on your personal laptop.
    * How to access the Python workshop materials from this website.
    * How to access and work with jupyter noteboos in VS Code.
    * Signing up for the workshops.

    &nbsp;
    """, unsafe_allow_html=True
)
