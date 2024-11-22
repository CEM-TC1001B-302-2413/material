import streamlit as st

pages = [
    st.Page("page/inicio.py", title="Página de inicio"),
    st.Page("page/datos.py", title="Datos del proyecto"),
    st.Page("page/formulario.py", title="Formulario")
    ]

pg = st.navigation(pages)

pg.run()