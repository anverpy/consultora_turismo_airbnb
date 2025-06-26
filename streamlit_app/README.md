# 🏛️ Dashboard Regulatorio de Turismo Urbano

## 📊 Análisis del Impacto de Airbnb en España

### 🎯 Descripción del Proyecto

Dashboard interactivo desarrollado por **consultores en turismo sostenible** para evaluar el impacto urbano de Airbnb en Madrid, Barcelona y Mallorca. Esta herramienta está diseñada para **gobiernos locales** que buscan implementar regulaciones sostenibles.

### 🚀 Acceso al Dashboard

**🌐 URL Pública:** `https://turismo-urbano-regulatorio.streamlit.app/`

### 📋 Funcionalidades Principales

#### 🗺️ Mapas Interactivos
- **Mapas coropléticos** por niveles de saturación
- **Análisis territorial** por barrios
- **Visualización geoespacial** con GeoJSON

#### 📊 Métricas Clave
- **Total de anuncios** por ciudad
- **Barrios críticos** con alta saturación
- **Ratio turístico/residencial**
- **Índices de saturación**

#### 🚨 Sistema de Alertas
- **Clasificación automática** por niveles de riesgo
- **Alertas críticas** (>80% saturación)
- **Monitoreo preventivo** (40-80% saturación)

#### 💡 Recomendaciones Regulatorias
- **Políticas específicas** por nivel de saturación
- **Simulador de impacto** de medidas regulatorias
- **Casos de uso** para gobiernos locales

### 🔧 Tecnologías Utilizadas

```python
# Stack Tecnológico
streamlit==1.46.0      # Framework web interactivo
plotly==5.17.0         # Visualizaciones interactivas
folium==0.15.1         # Mapas geoespaciales
pandas==2.1.4          # Análisis de datos
sqlite3                # Base de datos
streamlit-folium==0.25.0  # Integración mapas
```

### 📁 Estructura del Proyecto

```
streamlit_app/
├── app.py              # Dashboard principal
├── .streamlit/
│   └── config.toml     # Configuración Streamlit
└── requirements.txt    # Dependencias

data/
└── processed/
    ├── airbnb_consultores_turismo.db  # Base de datos principal
    ├── neighbourhoods_*.geojson       # Polígonos territoriales
    └── kpis_*.csv                     # KPIs calculados
```

### 🎨 Interfaz de Usuario

#### 🎛️ Panel de Control (Sidebar)
- **Filtro por ciudad:** Madrid, Barcelona, Mallorca
- **Configuración de alertas:** Umbrales personalizables
- **Información del equipo:** Roles y responsabilidades

#### 📑 Tabs Principales
1. **🗺️ Mapas de Impacto:** Visualización territorial
2. **📊 Análisis Comparativo:** Métricas entre ciudades
3. **🚨 Sistema de Alertas:** Monitoreo automático
4. **💡 Recomendaciones:** Políticas sugeridas

### 👥 Equipo de Desarrollo

| Rol | Responsabilidad | Enfoque |
|-----|----------------|---------|
| **🔧 Data Engineer** | Extracción y procesamiento | Pipeline de datos |
| **📊 Data Analyst** | Análisis estadístico | KPIs y correlaciones |
| **💼 Business Intelligence** | Dashboard e insights | Visualización y UX |

### 📈 Métricas de Éxito

#### ✅ Cumplimiento de Requisitos
- **Dashboard funcional:** ✅ 100% operativo
- **Mapas coropléticos:** ✅ Implementados
- **Sistema de alertas:** ✅ Automático
- **Simulador de políticas:** ✅ Interactivo
- **Deploy público:** ✅ Accesible online

#### 🎯 Casos de Uso Validados
- **Gobiernos locales:** Regulación basada en datos
- **Planificadores urbanos:** Análisis territorial
- **Consultores turísticos:** Evaluación de impacto
- **Investigadores:** Datos académicos

### 🔄 Actualización de Datos

El dashboard se alimenta de:
- **Inside Airbnb** (datos trimestrales)
- **Fuentes gubernamentales** (demografía, economía)
- **APIs públicas** (precios inmobiliarios)

### 📞 Contacto y Soporte

**📧 Email:** consultores@turismo-sostenible.es  
**🏢 Organización:** Equipo Consultores en Turismo Sostenible  
**📅 Última actualización:** Junio 2025  

### 🏷️ Licencia

Este proyecto está desarrollado con fines académicos y de consultoría. Los datos utilizados provienen de fuentes públicas y están sujetos a sus respectivas licencias.

---

**🏛️ Dashboard Regulatorio de Turismo Urbano** | Desarrollado con ❤️ por el Equipo de Consultores
