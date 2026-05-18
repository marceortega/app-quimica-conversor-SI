# =========================================================
# IMPORTAMOS LAS LIBRERÍAS NECESARIAS
# =========================================================

# streamlit:
# Librería principal para crear la aplicación web
import streamlit as st

# pandas:
# Librería usada para crear y mostrar tablas de datos
import pandas as pd


# =========================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# =========================================================

# Configuramos:
# - título que aparece en la pestaña del navegador
# - ícono de la página
# - diseño ancho de pantalla
st.set_page_config(
    page_title="Conversor SI",
    page_icon="🧪",
    layout="wide"
)


# =========================================================
# COLORES PRINCIPALES DEL PROYECTO
# =========================================================

# Estos colores después se pueden reemplazar
# por los colores oficiales de la universidad

COLOR_PRINCIPAL = "#111111"      # negro elegante
COLOR_SECUNDARIO = "#FEd829"     # dorado
COLOR_FONDO = "#F5F5F5"          # gris claro
COLOR_TEXTO = "#1A1A1A"          # negro texto


# =========================================================
# CSS PERSONALIZADO
# =========================================================

# Aquí modificamos el diseño visual usando CSS
# Similar a como se estilizan páginas web

st.markdown(f"""
<style>

    /* Fondo general de la app */
    .stApp {{
        background-color: {COLOR_FONDO};
    }}

    /* Títulos principales */
    h1 {{
        color: {COLOR_TEXTO};
        font-size: 52px;
        font-weight: 800;
    }}

    /* Subtítulos */
    h2 {{
        color: {COLOR_TEXTO};
        font-weight: 700;
    }}

    /* Texto normal */
    p {{
        color: #444444;
        font-size: 20px;
    }}

    /* Barra superior institucional */
    .topbar {{
        background-color: {COLOR_PRINCIPAL};
        padding: 15px;
        border-bottom: 5px solid {COLOR_SECUNDARIO};
        margin-bottom: 30px;
    }}

    /* Texto barra superior */
    .topbar-text {{
        color: white;
        font-size: 18px;
        font-weight: bold;
    }}

    /* Caja principal */
    .main-box {{
        background-color: white;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
        margin-bottom: 30px;
    }}

    /* Botón principal */
    .stButton > button {{
        background-color: {COLOR_PRINCIPAL};
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 30px;
        font-size: 20px;
        font-weight: bold;
    }}

    /* Hover del botón */
    .stButton > button:hover {{
        background-color: {COLOR_SECUNDARIO};
        color: black;
    }}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BARRA SUPERIOR TIPO UNIVERSIDAD
# =========================================================

# Esta sección simula una cabecera institucional
# Más adelante aquí pueden agregar el logo oficial

st.markdown(f"""
<div class="topbar">
    <div class="topbar-text">
        🏛️ UNIVERSIDAD MAYOR — Química Aplicada a la Ingeniería
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# TÍTULO PRINCIPAL
# =========================================================

st.title("🧪 Conversor del Sistema Internacional de Medidas")

st.write(
    "Aplicación para convertir unidades usadas en "
    "Química Aplicada a la Ingeniería."
)


# =========================================================
# DICCIONARIO PRINCIPAL DE CONVERSIONES
# =========================================================

# Aquí almacenamos:
# - nombre de magnitud
# - unidad base
# - factores de conversión

CONVERSIONES = {

    "Masa": {
        "unidad_base": "g",
        "unidades": {
            "Ton": 1_000_000,
            "Kg": 1000,
            "g": 1,
            "mg": 0.001,
            "ug": 0.000001,
        }
    },

    "Volumen": {
        "unidad_base": "L",
        "unidades": {
            "Gal": 3.78541,
            "m3": 1000,
            "L": 1,
            "mL": 0.001,
            "uL": 0.000001,
        }
    },

    "Distancia": {
        "unidad_base": "m",
        "unidades": {
            "Yarda": 0.9144,
            "Pulgada": 0.0254,
            "m": 1,
            "cm": 0.01,
            "km": 1000,
            "mm": 0.001,
            "Pie": 0.3048,
            "Milla": 1609.34
        }
    },

    "Densidad": {
        "unidad_base": "kg/m3",
        "unidades": {
            "Kg/m3": 1,
            "g/mL": 1000,
            "Kg/L": 1000,
            "g/L": 1,
        }
    },

    "Presión": {
        "unidad_base": "Pa",
        "unidades": {
            "mmHg": 133.322,
            "Atm": 101325,
            "Pa": 1,
            "psi": 6894.76,
            "Torr": 133.322,
        }
    },

    "Tiempo": {
        "unidad_base": "s",
        "unidades": {
            "s": 1,
            "min": 60,
            "hora": 3600,
        }
    },

    "Fuerza": {
        "unidad_base": "N",
        "unidades": {
            "Newton": 1,
            "Kilonewton": 1000,
            "Micronewton": 0.000001,
            "Dina": 0.00001,
            "Kilogramofuerza": 9.80665,
        }
    },

    "Energía": {
        "unidad_base": "KJ",
        "unidades": {
            "KJ": 1,
            "Kcal": 4.184,
        }
    }
}


# =========================================================
# CAJA PRINCIPAL VISUAL
# =========================================================

st.markdown('<div class="main-box">', unsafe_allow_html=True)


# =========================================================
# SELECTOR DE MAGNITUD
# =========================================================

magnitud = st.selectbox(
    "Selecciona la magnitud",
    list(CONVERSIONES.keys())
)


# Obtenemos las unidades correspondientes
unidades = CONVERSIONES[magnitud]["unidades"]


# =========================================================
# INPUT DEL VALOR
# =========================================================

valor = st.number_input(
    "Ingresa el valor a convertir",
    value=1.0
)


# =========================================================
# COLUMNAS PARA LAS UNIDADES
# =========================================================

col1, col2 = st.columns(2)

with col1:
    unidad_origen = st.selectbox(
        "Unidad de origen",
        list(unidades.keys())
    )

with col2:
    unidad_destino = st.selectbox(
        "Unidad de destino",
        list(unidades.keys())
    )


# =========================================================
# BOTÓN DE CONVERSIÓN
# =========================================================

if st.button("Convertir"):

    # ============================================
    # CONVERSIÓN A UNIDAD BASE
    # ============================================

    valor_en_base = valor * unidades[unidad_origen]

    # ============================================
    # CONVERSIÓN A UNIDAD DESTINO
    # ============================================

    resultado = valor_en_base / unidades[unidad_destino]

    # ============================================
    # MENSAJE DE ÉXITO
    # ============================================

    st.success("Conversión realizada correctamente")

    # ============================================
    # RESULTADO PRINCIPAL
    # ============================================

    st.markdown("## Resultado")

    st.markdown(
        f"# <span style='color:{COLOR_SECUNDARIO}'>"
        f"{valor} {unidad_origen}"
        f"</span> = {resultado:.6g} {unidad_destino}",
        unsafe_allow_html=True
    )

    # ============================================
    # TABLA DE CONVERSIONES
    # ============================================

    st.markdown("## Tabla de conversiones para la misma magnitud")

    filas = []

    for unidad, factor in unidades.items():

        conversion = valor_en_base / factor

        filas.append({
            "Unidad": unidad,
            "Valor convertido": conversion
        })

    df = pd.DataFrame(filas)

    st.dataframe(
        df,
        use_container_width=True
    )

    # ============================================
    # INFORMACIÓN DE LA UNIDAD BASE
    # ============================================

    st.info(
        f"La unidad base usada para "
        f"{magnitud} es: "
        f"{CONVERSIONES[magnitud]['unidad_base']}"
    )


# Cerramos caja principal visual
st.markdown("</div>", unsafe_allow_html=True)
