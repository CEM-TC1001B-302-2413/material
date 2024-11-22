import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos_excel(nombre_archivo):
    df = pd.read_excel(nombre_archivo)
    return df

@st.cache_data
def cargar_datos_csv(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    return df

def cargar_respuestas():
    df = pd.read_csv("data/respuestas.csv")
    return df

df1 = cargar_datos_excel("data/datos.xlsx")
df2 = cargar_datos_csv("data/datos.csv")
df_mapa = cargar_datos_csv("data/mapa.csv")
df_respuestas = cargar_respuestas()

st.title("Muestra de datos")

st.dataframe(df1.head(5)) # Muestra sólo las primeras 5 filas
st.caption("Tomado de...")

st.dataframe(df2)
st.caption("Tomado de...")

st.subheader("Respuestas de mi formulario")
st.dataframe(df_respuestas)
st.caption("Respuestas del formulario incluido en este sitio")

st.subheader("Estadísticas")

st.text(f"Suma total: {df2['Calificación'].sum()}")
st.text(f"Promedio: {df2['Calificación'].mean()}")
st.text(f"Mediana: {df2['Calificación'].median()}")
st.text(f"Moda: {df2['Calificación'].mode()[0]}")
st.text(f"Desviación estándar: {df2['Calificación'].std()}")
st.text(f"Varianza: {df2['Calificación'].var()}")
st.text(f"Mínimo: {df2['Calificación'].min()}")
st.text(f"Máximo: {df2['Calificación'].max()}")

c1, c2, c3 = st.columns(3)

c1.metric("Promedio",
          f"{df2['Calificación'].mean():,.2f} puntos",
          "3 puntos")

c2.metric("Reprobados",
          "30%",
          "-5%")

c3.metric("Inscritos",
          "10 alumnos",
          "+2 alumnos")

st.bar_chart(df2, x="Nombre", y="Calificación")

st.scatter_chart(df2, x="Matrícula", y="Calificación")

st.line_chart(df2, x="Matrícula", y="Calificación")

st.subheader("Mapa de México")

st.dataframe(df_mapa)

st.map(df_mapa,
       latitude="Latitud",
       longitude="Longitud",
       color="Color")




