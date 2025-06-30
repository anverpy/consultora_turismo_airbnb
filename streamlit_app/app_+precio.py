"""
Dashboard de Turismo Urbano - Versión Renovada y Funcional
==========================================================

Dashboard completamente reestructurado que utiliza únicamente el dataset principal
listings_unificado.csv con integración completa de precios reales.

Autor: Consultoría de Turismo Urbano
Fecha: 2024
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
import json
from pathlib import Path
import numpy as np
import random
import re
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Turismo Urbano - Renovado",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado con tema oscuro optimizado
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    .hero-header {
        background: linear-gradient(rgba(14, 17, 23, 0.8), rgba(30, 30, 30, 0.8));
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 212, 255, 0.2);
        border: 1px solid #00d4ff;
    }
    
    .metric-card {
        background-color: #1e1e1e;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #00d4ff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .alert-info {
        background: linear-gradient(135deg, #17a2b8, #138496);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(23, 162, 184, 0.3);
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #ff8c00, #ff6600);
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(255, 140, 0, 0.3);
    }
    
    div[data-testid="metric-container"] {
        background-color: #1e1e1e;
        border: 1px solid #333;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #00d4ff;
    }
    
    [data-testid="stSidebar"] > div {
        background-color: #1e1e1e !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #fafafa !important;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def cargar_datos_principales():
    """
    Carga el dataset principal y calcula métricas en tiempo real.
    Enfoque simplificado usando solo listings_unificado.csv
    """
    try:
        # Buscar el archivo principal
        possible_paths = [
            Path(__file__).parent.parent / "data" / "processed" / "listings_unificado.csv",
            Path("data/processed/listings_unificado.csv"),
            Path("../data/processed/listings_unificado.csv")
        ]
        
        data_path = None
        for path in possible_paths:
            if path.exists():
                data_path = path
                break
        
        if data_path is None:
            st.error("❌ No se encontró el archivo listings_unificado.csv")
            return None, None
        
        # Cargar datos
        df = pd.read_csv(data_path)
        
        # Limpiar y procesar datos
        df = df.dropna(subset=['ciudad', 'neighbourhood_cleansed'])
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['price'])
        df = df[df['price'] > 0]
        
        # Calcular métricas por ciudad
        metricas_ciudad = {}
        for ciudad in df['ciudad'].unique():
            df_ciudad = df[df['ciudad'] == ciudad]
            
            # Calcular ratio de entire home
            total_listings = len(df_ciudad)
            entire_home_count = len(df_ciudad[df_ciudad['room_type'] == 'Entire home/apt'])
            ratio_entire_home = (entire_home_count / total_listings * 100) if total_listings > 0 else 0
            
            # Calcular precio medio
            precio_medio = df_ciudad['price'].mean()
            
            # Calcular disponibilidad media
            disponibilidad_media = df_ciudad['availability_365'].mean()
            ocupacion_estimada = max(0, 100 - (disponibilidad_media / 365 * 100))
            
            metricas_ciudad[ciudad] = {
                'total_listings': total_listings,
                'precio_medio': precio_medio,
                'ratio_entire_home': ratio_entire_home,
                'ocupacion_estimada': ocupacion_estimada,
                'entire_home_count': entire_home_count,
                'barrios_count': df_ciudad['neighbourhood_cleansed'].nunique()
            }
        
        return df, metricas_ciudad
        
    except Exception as e:
        st.error(f"❌ Error al cargar datos: {str(e)}")
        return None, None

def crear_metricas_barrio(df):
    """
    Calcula métricas por barrio desde el dataset principal
    """
    metricas_barrio = []
    
    for ciudad in df['ciudad'].unique():
        df_ciudad = df[df['ciudad'] == ciudad]
        
        for barrio in df_ciudad['neighbourhood_cleansed'].unique():
            df_barrio = df_ciudad[df_ciudad['neighbourhood_cleansed'] == barrio]
            
            if len(df_barrio) > 0:
                total_listings = len(df_barrio)
                entire_home_count = len(df_barrio[df_barrio['room_type'] == 'Entire home/apt'])
                ratio_entire_home = (entire_home_count / total_listings * 100) if total_listings > 0 else 0
                precio_medio = df_barrio['price'].mean()
                disponibilidad_media = df_barrio['availability_365'].mean()
                
                metricas_barrio.append({
                    'ciudad': ciudad,
                    'barrio': barrio,
                    'total_listings': total_listings,
                    'entire_home_count': entire_home_count,
                    'ratio_entire_home': ratio_entire_home,
                    'precio_medio': precio_medio,
                    'disponibilidad_media': disponibilidad_media,
                    'lat_mean': df_barrio['latitude'].mean(),
                    'lon_mean': df_barrio['longitude'].mean()
                })
    
    return pd.DataFrame(metricas_barrio)

def crear_mapa_interactivo(df, ciudad_seleccionada, tipo_mapa="concentracion"):
    """
    Crea mapas interactivos basados en los datos reales
    """
    df_ciudad = df[df['ciudad'].str.lower() == ciudad_seleccionada.lower()]
    
    if len(df_ciudad) == 0:
        return None
    
    # Coordenadas del centro por ciudad
    centros = {
        "madrid": [40.4168, -3.7038],
        "barcelona": [41.3851, 2.1734],
        "mallorca": [39.5696, 2.6502]
    }
    
    centro = centros.get(ciudad_seleccionada.lower(), [40.4168, -3.7038])
    
    # Crear mapa base
    m = folium.Map(
        location=centro,
        zoom_start=11,
        tiles='CartoDB dark_matter'
    )
    
    if tipo_mapa == "concentracion":
        # Agrupar por barrio
        df_barrios = df_ciudad.groupby('neighbourhood_cleansed').agg({
            'id': 'count',
            'price': 'mean',
            'latitude': 'mean',
            'longitude': 'mean',
            'room_type': lambda x: (x == 'Entire home/apt').sum()
        }).reset_index()
        
        df_barrios.columns = ['barrio', 'total_listings', 'precio_medio', 'lat', 'lon', 'entire_home_count']
        df_barrios['ratio_entire_home'] = (df_barrios['entire_home_count'] / df_barrios['total_listings'] * 100)
        
        # Tomar top 15 barrios
        top_barrios = df_barrios.nlargest(15, 'total_listings')
        
        for _, barrio in top_barrios.iterrows():
            # Color basado en concentración
            total = barrio['total_listings']
            if total > 500:
                color = 'red'
                categoria = 'Alta'
            elif total > 200:
                color = 'orange'
                categoria = 'Media-Alta'
            elif total > 50:
                color = 'yellow'
                categoria = 'Media'
            else:
                color = 'green'
                categoria = 'Baja'
            
            popup_text = f"""
            <div style="font-family: Arial, sans-serif; min-width: 200px;">
            <h4>{barrio['barrio']}</h4>
            <p><b>Total Listings:</b> {total:,}</p>
            <p><b>Precio Medio:</b> €{barrio['precio_medio']:.0f}/noche</p>
            <p><b>Ratio Entire Home:</b> {barrio['ratio_entire_home']:.1f}%</p>
            <p><b>Concentración:</b> {categoria}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=[barrio['lat'], barrio['lon']],
                radius=max(8, min(25, total / 20)),
                popup=folium.Popup(popup_text, max_width=300),
                color=color,
                fillColor=color,
                fillOpacity=0.7,
                weight=2,
                tooltip=f"{barrio['barrio']}: {total:,} listings"
            ).add_to(m)
    
    elif tipo_mapa == "precios":
        # Agrupar por barrio para precios
        df_barrios = df_ciudad.groupby('neighbourhood_cleansed').agg({
            'id': 'count',
            'price': 'mean',
            'latitude': 'mean',
            'longitude': 'mean'
        }).reset_index()
        
        df_barrios.columns = ['barrio', 'total_listings', 'precio_medio', 'lat', 'lon']
        
        # Filtrar barrios con suficientes datos
        df_barrios = df_barrios[df_barrios['total_listings'] >= 10]
        
        for _, barrio in df_barrios.iterrows():
            precio = barrio['precio_medio']
            
            # Color basado en precio
            if precio > 120:
                color = 'darkred'
                categoria = 'Premium'
            elif precio > 90:
                color = 'red'
                categoria = 'Alto'
            elif precio > 70:
                color = 'orange'
                categoria = 'Medio-Alto'
            elif precio > 50:
                color = 'yellow'
                categoria = 'Medio'
            else:
                color = 'green'
                categoria = 'Económico'
            
            popup_text = f"""
            <div style="font-family: Arial, sans-serif; min-width: 200px;">
            <h4>{barrio['barrio']}</h4>
            <p><b>Precio/día:</b> €{precio:.0f}</p>
            <p><b>Categoría:</b> {categoria}</p>
            <p><b>Total Listings:</b> {barrio['total_listings']:,}</p>
            </div>
            """
            
            folium.CircleMarker(
                location=[barrio['lat'], barrio['lon']],
                radius=max(6, min(20, precio / 8)),
                popup=folium.Popup(popup_text, max_width=300),
                color=color,
                fillColor=color,
                fillOpacity=0.6,
                weight=1,
                tooltip=f"{barrio['barrio']}: €{precio:.0f}/día"
            ).add_to(m)
    
    # Agregar leyenda
    if tipo_mapa == "concentracion":
        legend_html = '''
        <div style="position: absolute; bottom: 15px; left: 15px; width: 200px;
                    background-color: rgba(30, 30, 30, 0.95); border: 2px solid #00d4ff; 
                    z-index: 1000; font-size: 12px; border-radius: 8px; 
                    color: white; padding: 10px;">
        <h4 style="margin: 0 0 10px 0; color: #00d4ff;">Concentración de Listings</h4>
        <div><span style="color: red;">●</span> > 500 listings (Alta)</div>
        <div><span style="color: orange;">●</span> 200-500 listings (Media-Alta)</div>
        <div><span style="color: yellow;">●</span> 50-200 listings (Media)</div>
        <div><span style="color: green;">●</span> < 50 listings (Baja)</div>
        </div>
        '''
    else:
        legend_html = '''
        <div style="position: absolute; bottom: 15px; right: 15px; width: 180px;
                    background-color: rgba(30, 30, 30, 0.95); border: 2px solid #00d4ff; 
                    z-index: 1000; font-size: 12px; border-radius: 8px; 
                    color: white; padding: 10px;">
        <h4 style="margin: 0 0 10px 0; color: #00d4ff;">Precios por Barrio</h4>
        <div><span style="color: darkred;">●</span> > €120 (Premium)</div>
        <div><span style="color: red;">●</span> €90-120 (Alto)</div>
        <div><span style="color: orange;">●</span> €70-90 (Medio-Alto)</div>
        <div><span style="color: yellow;">●</span> €50-70 (Medio)</div>
        <div><span style="color: green;">●</span> < €50 (Económico)</div>
        </div>
        '''
    
    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m

def main():
    """Función principal del dashboard renovado"""
    
    # Header principal
    st.markdown("""
    <div class="hero-header">
    <h1 style="color: #00d4ff; margin-bottom: 1rem;">🏙️ Dashboard Turismo Urbano</h1>
    <h3 style="color: #fafafa; margin-bottom: 0.5rem;">Análisis Integral de Alojamientos Turísticos</h3>
    <p style="color: #cccccc; font-style: italic;">Versión renovada con datos integrados y visualizaciones completas</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cargar datos
    with st.spinner("🔄 Cargando datos..."):
        df, metricas_ciudad = cargar_datos_principales()
    
    if df is None or metricas_ciudad is None:
        st.error("❌ No se pudieron cargar los datos. Verifica que el archivo listings_unificado.csv existe.")
        return
    
    # Sidebar de configuración
    st.sidebar.header("⚙️ Configuración")
    
    ciudades_disponibles = list(metricas_ciudad.keys())
    ciudad_seleccionada = st.sidebar.selectbox(
        "🏙️ Seleccionar Ciudad:",
        ciudades_disponibles,
        index=0 if ciudades_disponibles else 0
    )
    
    # Mostrar métricas principales
    st.header(f"📊 Métricas para {ciudad_seleccionada.title()}")
    
    if ciudad_seleccionada in metricas_ciudad:
        metricas = metricas_ciudad[ciudad_seleccionada]
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "🏠 Total Listings",
                f"{metricas['total_listings']:,}",
                help="Número total de alojamientos turísticos"
            )
        
        with col2:
            st.metric(
                "💰 Precio Medio",
                f"€{metricas['precio_medio']:.0f}",
                delta="por noche",
                help="Precio promedio por noche en euros"
            )
        
        with col3:
            st.metric(
                "🏢 Ratio Entire Home",
                f"{metricas['ratio_entire_home']:.1f}%",
                help="Porcentaje de alojamientos completos vs habitaciones"
            )
        
        with col4:
            st.metric(
                "📈 Ocupación Est.",
                f"{metricas['ocupacion_estimada']:.1f}%",
                help="Ocupación estimada basada en disponibilidad"
            )
    
    # Tabs principales
    tab1, tab2, tab3, tab4 = st.tabs([
        "🗺️ Mapas Territoriales",
        "📊 Análisis por Barrio",
        "💰 Análisis de Precios",
        "📈 Tendencias y Métricas"
    ])
    
    with tab1:
        st.header("🗺️ Análisis Territorial")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Mapa de Concentración")
            mapa_concentracion = crear_mapa_interactivo(df, ciudad_seleccionada, "concentracion")
            if mapa_concentracion:
                st_folium(mapa_concentracion, width=700, height=400, key="mapa_concentracion")
            else:
                st.info("No hay datos disponibles para esta ciudad")
        
        with col2:
            st.subheader("💰 Mapa de Precios")
            mapa_precios = crear_mapa_interactivo(df, ciudad_seleccionada, "precios")
            if mapa_precios:
                st_folium(mapa_precios, width=700, height=400, key="mapa_precios")
            else:
                st.info("No hay datos de precios para esta ciudad")
    
    with tab2:
        st.header("📊 Análisis por Barrio")
        
        # Calcular métricas por barrio
        df_barrios = crear_metricas_barrio(df)
        df_ciudad_barrios = df_barrios[df_barrios['ciudad'].str.lower() == ciudad_seleccionada.lower()]
        
        if not df_ciudad_barrios.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🏆 Top 10 Barrios por Concentración")
                top_barrios = df_ciudad_barrios.nlargest(10, 'total_listings')
                
                fig_barras = px.bar(
                    top_barrios,
                    y='barrio',
                    x='total_listings',
                    orientation='h',
                    title="Concentración de Alojamientos por Barrio",
                    labels={'total_listings': 'Total Listings', 'barrio': 'Barrio'},
                    color='total_listings',
                    color_continuous_scale='viridis'
                )
                fig_barras.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    height=400
                )
                st.plotly_chart(fig_barras, use_container_width=True)
            
            with col2:
                st.subheader("💰 Top 10 Barrios por Precio Medio")
                top_precios = df_ciudad_barrios.nlargest(10, 'precio_medio')
                
                fig_precios = px.bar(
                    top_precios,
                    y='barrio',
                    x='precio_medio',
                    orientation='h',
                    title="Precio Medio por Barrio (€/noche)",
                    labels={'precio_medio': 'Precio Medio (€)', 'barrio': 'Barrio'},
                    color='precio_medio',
                    color_continuous_scale='reds'
                )
                fig_precios.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    height=400
                )
                st.plotly_chart(fig_precios, use_container_width=True)
            
            # Tabla resumen
            st.subheader("📋 Resumen por Barrios")
            df_display = df_ciudad_barrios[['barrio', 'total_listings', 'precio_medio', 'ratio_entire_home']].copy()
            df_display['precio_medio'] = df_display['precio_medio'].round(0)
            df_display['ratio_entire_home'] = df_display['ratio_entire_home'].round(1)
            df_display.columns = ['Barrio', 'Total Listings', 'Precio Medio (€)', 'Ratio Entire Home (%)']
            
            st.dataframe(
                df_display.sort_values('Total Listings', ascending=False),
                use_container_width=True,
                height=300
            )
        else:
            st.info("No hay datos de barrios disponibles para esta ciudad")
    
    with tab3:
        st.header("💰 Análisis de Precios")
        
        df_ciudad = df[df['ciudad'].str.lower() == ciudad_seleccionada.lower()]
        
        if not df_ciudad.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 Distribución de Precios")
                
                fig_hist = px.histogram(
                    df_ciudad,
                    x='price',
                    nbins=30,
                    title="Distribución de Precios por Noche",
                    labels={'price': 'Precio (€)', 'count': 'Número de Listings'},
                    color_discrete_sequence=['#00d4ff']
                )
                fig_hist.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white'
                )
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                st.subheader("🏠 Precios por Tipo de Alojamiento")
                
                precios_por_tipo = df_ciudad.groupby('room_type')['price'].agg(['mean', 'count']).reset_index()
                precios_por_tipo.columns = ['Tipo', 'Precio_Medio', 'Cantidad']
                precios_por_tipo = precios_por_tipo[precios_por_tipo['Cantidad'] >= 10]  # Filtrar tipos con pocos datos
                
                fig_box = px.box(
                    df_ciudad,
                    x='room_type',
                    y='price',
                    title="Distribución de Precios por Tipo de Alojamiento",
                    labels={'room_type': 'Tipo de Alojamiento', 'price': 'Precio (€)'}
                )
                fig_box.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white'
                )
                st.plotly_chart(fig_box, use_container_width=True)
            
            # Estadísticas de precios
            st.subheader("📈 Estadísticas de Precios")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("💰 Precio Mínimo", f"€{df_ciudad['price'].min():.0f}")
            
            with col2:
                st.metric("💰 Precio Máximo", f"€{df_ciudad['price'].max():.0f}")
            
            with col3:
                st.metric("📊 Precio Mediano", f"€{df_ciudad['price'].median():.0f}")
            
            with col4:
                st.metric("📈 Desviación Estándar", f"€{df_ciudad['price'].std():.0f}")
        else:
            st.info("No hay datos de precios disponibles para esta ciudad")
    
    with tab4:
        st.header("📈 Tendencias y Métricas Avanzadas")
        
        # Comparativa entre ciudades
        st.subheader("🏙️ Comparativa entre Ciudades")
        
        # Crear DataFrame para comparativa
        datos_comparativa = []
        for ciudad, metricas in metricas_ciudad.items():
            datos_comparativa.append({
                'Ciudad': ciudad.title(),
                'Total Listings': metricas['total_listings'],
                'Precio Medio': metricas['precio_medio'],
                'Ratio Entire Home': metricas['ratio_entire_home'],
                'Ocupación Estimada': metricas['ocupacion_estimada'],
                'Número de Barrios': metricas['barrios_count']
            })
        
        df_comparativa = pd.DataFrame(datos_comparativa)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras comparativo
            fig_comp = px.bar(
                df_comparativa,
                x='Ciudad',
                y='Total Listings',
                title="Total de Listings por Ciudad",
                color='Total Listings',
                color_continuous_scale='viridis'
            )
            fig_comp.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig_comp, use_container_width=True)
        
        with col2:
            # Gráfico de precios comparativo
            fig_precios_comp = px.bar(
                df_comparativa,
                x='Ciudad',
                y='Precio Medio',
                title="Precio Medio por Ciudad (€/noche)",
                color='Precio Medio',
                color_continuous_scale='reds'
            )
            fig_precios_comp.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig_precios_comp, use_container_width=True)
        
        # Tabla comparativa
        st.subheader("📋 Tabla Comparativa")
        df_display_comp = df_comparativa.copy()
        df_display_comp['Precio Medio'] = df_display_comp['Precio Medio'].round(0)
        df_display_comp['Ratio Entire Home'] = df_display_comp['Ratio Entire Home'].round(1)
        df_display_comp['Ocupación Estimada'] = df_display_comp['Ocupación Estimada'].round(1)
        
        st.dataframe(df_display_comp, use_container_width=True)
        
        # Análisis de correlaciones
        st.subheader("🔍 Análisis de Correlaciones")
        
        df_ciudad = df[df['ciudad'].str.lower() == ciudad_seleccionada.lower()]
        if not df_ciudad.empty and len(df_ciudad) > 100:
            # Gráfico de dispersión precio vs disponibilidad
            fig_scatter = px.scatter(
                df_ciudad.sample(min(1000, len(df_ciudad))),  # Muestra para mejor rendimiento
                x='availability_365',
                y='price',
                color='room_type',
                title="Relación entre Precio y Disponibilidad Anual",
                labels={'availability_365': 'Disponibilidad (días/año)', 'price': 'Precio (€/noche)'}
            )
            fig_scatter.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("No hay suficientes datos para análisis de correlaciones")
    
    # Footer informativo
    st.markdown("---")
    st.markdown("""
    <div class="alert-info">
    <h4>ℹ️ Información del Dashboard</h4>
    <p><strong>Datos:</strong> Basado en listings_unificado.csv con precios reales integrados</p>
    <p><strong>Actualización:</strong> Los datos se procesan en tiempo real desde el archivo fuente</p>
    <p><strong>Cobertura:</strong> {ciudades} ciudades con un total de {total_listings:,} alojamientos</p>
    </div>
    """.format(
        ciudades=len(metricas_ciudad),
        total_listings=sum(m['total_listings'] for m in metricas_ciudad.values())
    ), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
