import datetime
import pandas as pd
import streamlit as st

st.title("Ejemplo de formulario")

formulario = st.form("form-crimen")

nombre = formulario.text_input("Nombre")

edad = formulario.number_input("Edad",
                               min_value=0,
                               max_value=150,
                               value=18)

lista_género = ["Femenino",
                "Masculino",
                "No binario",
                "Prefiero no responder"]

género = formulario.radio("Género",
                          lista_género)

estados_mexico = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
    "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima",
    "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo",
    "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca",
    "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa",
    "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán",
    "Zacatecas"
]

estado = formulario.selectbox("Estado en el que resides",
                              estados_mexico)

formulario.text("Propiedades")

casa = formulario.checkbox("Casa")
departamento = formulario.checkbox("Departamento")
negocio = formulario.checkbox("Negocio")
auto = formulario.checkbox("Automóvil")
moto = formulario.checkbox("Motocicleta")

delito = formulario.toggle("¿Has sido víctima de un delito?")

delitos = [
    "Homicidio", "Lesiones", "Robo a casa habitación", "Robo de vehículo", 
    "Robo a transeúnte", "Robo a negocio", "Robo de identidad", "Extorsión", 
    "Fraude", "Abuso de confianza", "Amenazas", "Secuestro", "Acoso sexual", 
    "Abuso sexual", "Violación", "Hostigamiento sexual", "Trata de personas", 
    "Corrupción de menores", "Violencia familiar", "Violencia de género", 
    "Desaparición forzada", "Tráfico de personas", "Delitos contra la salud", 
    "Narcotráfico", "Lavado de dinero", "Contrabando", "Delitos ambientales", 
    "Daños en propiedad ajena", "Delitos electorales", "Delitos informáticos", 
    "Pornografía infantil", "Falsificación de documentos", "Uso indebido de recursos públicos", 
    "Delitos fiscales", "Delitos contra la propiedad intelectual", 
    "Delitos contra la seguridad pública", "Abigeato", "Vandalismo", 
    "Desobediencia civil", "Privación ilegal de la libertad", "Usurpación de identidad", 
    "Delitos relacionados con armas de fuego", "Terrorismo", "Espionaje", 
    "Delitos contra la humanidad", "Despojo", "Alteración del orden público", 
    "Incitación a la violencia", "Discriminación", "Sabotaje", 
    "Obstrucción de la justicia", "Intimidación"
]

tipos_delitos = formulario.multiselect("Tipos de delitos de los que has sido víctima",
                                       delitos)

última_fecha = formulario.date_input("Fecha más reciente en la que fue víctima de un delito",
                                     min_value=datetime.date(2000, 1, 1),
                                     max_value=datetime.date(2050, 12, 31))

monto_perdido = formulario.slider("Monto perdido por delitos",
                                  min_value=0,
                                  max_value=1000000,
                                  value=50000)

submit = formulario.form_submit_button("Enviar datos")

if submit:
    df = pd.read_csv("data/respuestas.csv")
    if delito:
        tipos_delito_formato = tipos_delitos
        última_fecha_formato = última_fecha
        monto_perdido_formato = monto_perdido
    else:
        tipos_delito_formato = ""
        última_fecha_formato = ""
        monto_perdido_formato = ""
    nuevo_registro = pd.DataFrame([{
        "Nombre": nombre,
        "Edad": edad,
        "Género": género,
        "Estado de la república": estado,
        "Casa": casa,
        "Departamento": departamento,
        "Automóvil": auto,
        "Motocicleta": moto,
        "Víctima de delito": delito,
        "Tipos de delito": tipos_delito_formato,
        "Fecha más reciente": última_fecha_formato,
        "Monto perdido": monto_perdido_formato
        }])
    df = pd.concat([df, nuevo_registro],
                   ignore_index=True)
    df.to_csv("data/respuestas.csv", index=False)
    st.success("¡Registro exitoso!")




