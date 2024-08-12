#se importan las librerias necesarias para realizar la app
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv") # se lee la base de datos

# Titulo de la app
st.header("Análisis Exploratorio de Anuncios de Vehículos en EE.UU.")

#Visualizacion del Dataframe entero
st.write('Visualización del DataFrame')
st.dataframe(df)


# Filtrar por año del modelo
model_years = sorted(df['model_year'].dropna().unique())
selected_year = st.selectbox('Selecciona el año del modelo', model_years)

# Filtrar el DataFrame según el año seleccionado
filtered_data_year = df[df['model_year'] == selected_year]

# Filtrar por tipo de vehículo
vehicle_types = sorted(filtered_data_year['type'].dropna().unique())
selected_type = st.selectbox("Seleccione tipo de vehículo", vehicle_types)

# Filtrar el DataFrame según el tipo seleccionado
filtered_data_type = filtered_data_year[filtered_data_year['type'] == selected_type]

# Mostrar el DataFrame filtrado
st.write(f'DataFrame filtrado por el año {selected_year} y tipo de vehículo {selected_type}')
st.dataframe(filtered_data_type)


# crear una casilla de verificación para el histograma
histogram_button = st.checkbox('Construir un histograma') 

if histogram_button: # si la casilla de verificación está seleccionada
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(df, color='type', x='price', nbins=50, title='Distribución de Precios')
        
    # mostrar un gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación para el grafico de dispersion
scatter_button = st.checkbox('Construir gráfico de dispersión')

# Acción al hacer clic en el botón de gráfico de dispersión
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(df, x="odometer", y="price", title='Relación entre Millas Recorridas y Precio')
    
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

boxplot_button = st.checkbox('Construir boxplot') # crear una casilla de verificación para la opcion de boxplot

if boxplot_button:
    st.write('Creación de un boxplot para el conjunto de datos de anuncios de venta de coches')

    # Crear un boxplot
    fig = px.box(df, x='condition', y='price', title='Precio por Condición del Coche')

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


