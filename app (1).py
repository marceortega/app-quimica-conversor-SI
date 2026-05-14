import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conversor SI", page_icon="🧪")

st.title("🧪 Conversor del Sistema Internacional de Medidas")
st.write("Aplicación para convertir unidades usadas en Química Aplicada a la Ingeniería.")

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

magnitud = st.selectbox("Selecciona la magnitud", list(CONVERSIONES.keys()))

unidades = CONVERSIONES[magnitud]["unidades"]

valor = st.number_input("Ingresa el valor a convertir", value=1.0)

unidad_origen = st.selectbox("Unidad de origen", list(unidades.keys()))
unidad_destino = st.selectbox("Unidad de destino", list(unidades.keys()))

if st.button("Convertir"):
    valor_en_base = valor * unidades[unidad_origen]
    resultado = valor_en_base / unidades[unidad_destino]

    st.success("Conversión realizada correctamente")
    st.subheader("Resultado")
    st.write(f"**{valor} {unidad_origen} = {resultado:.6g} {unidad_destino}**")

    st.subheader("Tabla de conversiones para la misma magnitud")

    filas = []
    for unidad, factor in unidades.items():
        conversion = valor_en_base / factor
        filas.append({
            "Unidad": unidad,
            "Valor convertido": conversion
        })

    df = pd.DataFrame(filas)
    st.dataframe(df, use_container_width=True)

    st.info(
        f"La unidad base usada para {magnitud} es: "
        f"{CONVERSIONES[magnitud]['unidad_base']}"
    )
