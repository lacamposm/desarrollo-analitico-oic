import pandas as pd
import streamlit as st
from my_pandas import SuperTabla


def generar_datos_ejemplo():
    """Genera datos de ejemplo para la demostración."""
    return [
        {"fecha": "2025-01-01", "producto": "Laptop", "cantidad": 10, "precio": 1200.0},
        {"fecha": "2025-01-02", "producto": "Monitor", "cantidad": 15, "precio": 300.0},
        {"fecha": "2025-01-03", "producto": "Laptop", "cantidad": 8, "precio": 1200.0},
        {"fecha": "2025-01-04", "producto": "Teclado", "cantidad": 20, "precio": 80.0},
        {"fecha": "2025-01-05", "producto": "Monitor", "cantidad": 12, "precio": 300.0},
    ]


st.set_page_config(page_title="my_pandas Demo", page_icon="📊")

st.title("📊 Análisis de datos simplificado.")

# Data.
datos = generar_datos_ejemplo()
tabla = SuperTabla(datos)

st.header("📋 Vista de datos")
st.text(str(tabla))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Operaciones")
    operacion = st.selectbox(
        "Selecciona una operación:",
        ["Filtrar", "Ordenar", "Agregar columna", "Agrupar"]
    )
    
    if operacion == "Filtrar":
        producto = st.selectbox(
            "Filtrar por producto:",
            list(set(fila["producto"] for fila in datos))
        )
        resultado = tabla.filtrar(lambda fila: fila["producto"] == producto)
        
    elif operacion == "Ordenar":
        columna = st.selectbox("Ordenar por:", ["fecha", "producto", "cantidad", "precio"])
        ascendente = st.checkbox("Ascendente", value=True)
        resultado = tabla.ordenar_por(columna, ascendente)
        
    elif operacion == "Agregar columna":
        resultado = tabla.agregar_columna(
            "total", 
            lambda fila: fila["cantidad"] * fila["precio"]
        )
        
    elif operacion == "Agrupar":
        resultado = tabla.agrupar_por("producto")

with col2:
    st.subheader("Resultado")
    st.text(str(resultado if 'resultado' in locals() else tabla))

st.header("Comparación con pandas")
st.dataframe(pd.DataFrame(datos))

st.markdown("---")
st.markdown("🌟 Desarrollado con ♥️ como parte del curso de inducción: `desarrollo analítico del OIC`")