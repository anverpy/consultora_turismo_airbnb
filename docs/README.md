# 🏛️ Consultores Turismo Sostenible - Análisis Airbnb

> **Proyecto de consultoría para evaluar el impacto urbano de Airbnb en España**

## 🎯 Objetivo

Analizar el impacto de Airbnb en Madrid, Barcelona y Mallorca para proporcionar recomendaciones de regulación sostenible a autoridades locales.

## 🚀 Inicio Rápido

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar dashboard
streamlit run streamlit_app/app.py
```

El dashboard estará disponible en `http://localhost:8501`

## 📊 KPIs Principales

| KPI | Descripción | Umbral Crítico |
|-----|-------------|----------------|
| **Densidad por barrio** | Alojamientos Airbnb por km² | >100/km² |
| **Ratio turístico** | % viviendas dedicadas a Airbnb | >15% |
| **Saturación territorial** | Capacidad vs población local | >20% |

## 🏙️ Ciudades Analizadas

- **🏛️ Madrid**: Enfoque en regulación urbana integral
- **🏖️ Barcelona**: Validación de moratoria existente  
- **🏝️ Mallorca**: Gestión diferenciada por temporada

## 📁 Estructura del Proyecto

```
consultores_turismo_airbnb/
├── streamlit_app/
│   ├── app.py              # Dashboard principal
│   └── app_nuevo.py        # Versión alternativa
├── notebooks/
│   ├── persona_a_data_engineer.ipynb    # Procesamiento datos
│   ├── persona_b_data_analyst.ipynb     # Análisis KPIs
│   └── persona_c_business_intelligence.ipynb # Visualizaciones
├── data/                   # Datos Inside Airbnb (no incluidos)
├── docs/                   # Documentación del proyecto
└── requirements.txt        # Dependencias Python
```

## 🛠️ Tecnologías

- **Streamlit**: Dashboard interactivo
- **Pandas/NumPy**: Procesamiento de datos
- **Plotly**: Visualizaciones avanzadas
- **Folium**: Mapas interactivos

## 📋 Funcionalidades Dashboard

✅ Mapas de densidad por barrio  
✅ KPIs en tiempo real  
✅ Sistema de alertas por saturación  
✅ Análisis comparativo entre ciudades  
✅ Exportación de reportes  

## 📝 Flujo de Trabajo

1. **Data Engineer**: Extracción y limpieza de datos Inside Airbnb
2. **Data Analyst**: Cálculo de KPIs y análisis estadístico
3. **Business Intelligence**: Dashboard y visualizaciones finales

## 🔧 Configuración

- Los datos deben ubicarse en la carpeta `data/`
- El dashboard está optimizado para Streamlit Cloud
- Configuración de tema oscuro incluida

## 📞 Soporte

Para dudas técnicas, revisar los notebooks en orden o consultar el código del dashboard principal.
