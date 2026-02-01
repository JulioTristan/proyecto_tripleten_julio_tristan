import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("Análisis exploratorio de vehículos")

st.write(
    "Esta aplicación muestra un análisis exploratorio de datos "
    "usando Streamlit, Pandas y Plotly."
)

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar una muestra del dataset
st.subheader("Vista previa de los datos")
st.write(df.head())

# Botón para crear el histograma
if st.button("Mostrar histograma de precios"):
    st.write("Histograma de precios de los vehículos")

    fig = px.histogram(
        df,
        x="price",
        nbins=50,
        title="Distribución de precios de vehículos"
    )

    st.plotly_chart(fig)

# Botón: Gráfico de dispersión
if st.button("Mostrar gráfico de dispersión (precio vs kilometraje)"):
    st.write("Relación entre el precio y el kilometraje de los vehículos")

    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Precio vs Kilometraje",
        opacity=0.5,
        labels={
            "odometer": "Kilometraje",
            "price": "Precio"
        }
    )

    st.plotly_chart(fig_scatter)