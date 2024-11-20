import streamlit as st

pages = [
    st.Page("page/inicio.py", title="Página de inicio"),
    st.Page("page/datos.py", title="Datos del proyecto")
    ]

pg = st.navigation(pages)

pg.run()