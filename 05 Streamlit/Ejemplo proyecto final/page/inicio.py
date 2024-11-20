import streamlit as st

st.title("Mi proyecto final")

st.header("Primera parte")

st.subheader("Primer elemento")

st.text("Un ejemplo de texto")

# Markdown

st.markdown("""

# Encabezado
## Subencabezado
### Subsubencabezado
#### Subsubsubencabezado
---

## Listado ordenado
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
---

## Listado no ordenado
- Primer elemento
- Segundo elemento
- Tercer elemento

## Latex
$$ y = \sum_{i=0}^{100}x_{i}^{2}-2x_{i}+5 $$

## Formato de texto
Hola soy de color :blue[azul].
Tengo fondo :red-background[rojo].
Uso un emoji :sunglasses:.

Soy un texto en *cursivas*.
Soy un texto en **negritas**.
Soy un texto en ***cursivas y negritas***.

Símbolos: -> <- <-> >= <= ~=

Google material icons: :material/Favorite:

[Enlaces](http://www.google.com)

## Tabla

| # | Elemento | Descripción |
| --- | --- | --- |
| 1 | Primer elemento | Descripción del primer elemento |
| 2 | Segundo elemento | Descripción del segundo elemento |
| 3 | Tercer elemento | Descripción del tercer elemento |
| 4 | Cuarto elemento | Descripción del cuarto elemento |

""")

tabla = [
    ["#", "Elemento", "Descripción"],
    [1, "Primer elemento", "Descripción del primer elemento"],
    [2, "Segundo elemento", "Descripción del segundo elemento"],
    [3, "Tercer elemento", "Descripción del tercer elemento"],
    ]

st.table(tabla)

st.image("images/pexels-rdne-6069351.jpg")
st.caption("Imagen tomada de: https://www.pexels.com/photo/a-person-in-orange-shirt-with-tattooed-arms-6069351/")

c1, c2 =  st.columns(2)
c1.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
c2.image("images/pexels-pixabay-270220.jpg")
c2.caption("Imagen tomada de: https://www.pexels.com/photo/police-standing-on-gray-asphalt-during-nighttime-270220/")

c3, c4 = st.columns([0.7, 0.3])
c3.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
c4.image("images/pexels-pixabay-270220.jpg")
c4.caption("Imagen tomada de: https://www.pexels.com/photo/police-standing-on-gray-asphalt-during-nighttime-270220/")

st.video("https://www.youtube.com/watch?v=HNm6N22Yhxo")


