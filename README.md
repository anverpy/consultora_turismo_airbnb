# 🏛️ **PROYECTO INSIDE AIRBNB - CONSULTORES EN TURISMO SOSTENIBLE**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Optimizado-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
🔗 **Enlaces Importantes**
- 🛠️ **Guía técnica:** `/docs/technical_guide.md`
- 📊 **Manual de KPIs:** `/docs/kpis_methodology.md`
- 🖥️ **Manual dashboard:** `/docs/dashboard_manual.md`

![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

### 📊 Análisis del Impacto Urbano de Airbnb en España
#### *Madrid • Barcelona • Mallorca*

---

**🎯 Proyecto desarrollado por el equipo de Consultores en Turismo Sostenible**  
*Evaluando el impacto urbano de Airbnb y proponiendo regulaciones sostenibles.*

</div>

---

## 🎯 **OBJETIVOS DEL PROYECTO**

> **CONSULTORA CONTRATADA POR GOBIERNO LOCAL**
> 
> Evaluar el **impacto urbano** de Airbnb y proponer **regulaciones sostenibles** que equilibren el desarrollo turístico con la calidad de vida de los residentes.

### 🔑 **KPIs Principales**
- 🏘️ **Densidad por barrio:** Alojamientos Airbnb por km² o por 1.000 habitantes
- ⚖️ **Ratio turístico/residencial:** % de viviendas dedicadas a Airbnb vs. residenciales
- 🚨 **Saturación territorial:** Capacidad turística vs. población/área local
- 💸 **Análisis económico:** Impacto económico del turismo en las ciudades analizadas. 

---

## 🏙️ **CIUDADES ANALIZADAS**

| 🌆 **Ciudad** | 📊 **Características** | 🎯 **Enfoque** |
|---|---|---|
| **🏛️ Madrid** | Capital, centro urbano, alta densidad | Regulación urbana moderada |
| **🏖️ Barcelona** | Ciudad costera, turismo cultural/playa | Prohibición alquiler vacacional en 2028 |
| **🏝️ Mallorca** | Territorio insular, estacionalidad extrema | Paralización nuevas licencias |

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
consultores_turismo_airbnb/
├── 📋 README.md                    # Documentación principal
├── 📦 requirements.txt             # Dependencias del proyecto
├── 
├── 📊 data/
│   ├── external/                   # Fuentes externas (INE, demografía, inmobiliarios)
│   │   ├── datos_demograficos.csv
│   │   ├── estadisticas_turismo.csv
│   │   ├── precios_alquileres.csv
│   │   └── precios_inmobiliarios_reales.csv
│   └── processed/                  # Datos procesados y consolidados
│       ├── airbnb_consultores_turismo.db    # Base de datos principal
│       ├── listings_madrid_new.csv          # Dataset Madrid consolidado (25 columnas)
│       ├── listings_unificado.csv           # Dataset multi-ciudad
│       ├── kpis_por_barrio.csv             # KPIs territoriales
│       └── neighbourhoods_*.geojson         # Geometrías de barrios
├── 
├── 📓 notebooks/
│   ├── persona_a_data_engineer.ipynb     # Extracción y limpieza
│   ├── persona_b_data_analyst.ipynb      # Análisis y KPIs
│   └── persona_c_business_intelligence.ipynb # Visualizaciones
├── 
├── 🖥️ streamlit_app/
│   ├── app.py                      # Dashboard principal
│   ├── pages/                      # Páginas del dashboard
│   └── utils/                      # Utilidades del dashboard
├── 
├── 🔧 src/
│   ├── data_processing/            # Módulos de procesamiento
│   ├── analysis/                   # Funciones de análisis
│   └── visualization/              # Módulos de visualización
└── 
└── 📖 docs/                        # Documentación adicional
    ├── technical_guide.md          # Guía técnica del proyecto
    ├── kpis_methodology.md         # Manual de metodología KPIs
    ├── dashboard_manual.md         # Manual de usuario dashboard
    ├── presentation_script.md      # Guión presentación ejecutiva (20 min)
    └── presentation_slides.md      # Especificaciones slides (18 slides)
```

---

## 📊 **DATASETS Y FUENTES DE DATOS**

### 🏛️ **Dataset Principal: listings_unificado.csv**

Nuestro dataset consolidado combina datos de Inside Airbnb con datos externos del Instituto de Estadística, los Censos de cada ciudad y un análisis temporal avanzado:

#### **🔍 CARACTERÍSTICAS PRINCIPALES**
- **Precio consolidado** → `price_market` que combina precios base + datos de calendar
- **Métricas económicas** → Disponibilidad y precios
- **Intensidad turística** → Score 0-100 que evalúa la presión turística por alojamiento
- **Datos de regulación** → Licencias oficiales y políticas

#### **📈 PRINCIPALES MÉTRICAS CALCULADAS**
- `ubicación` - Localización de alojamientos para el estudio de la saturación turística por ciudad. 
- `Neighbourhood` - Clasificación de la saturación turística por ciudad para análisis del comportamiento de los huéspedes.
- `precio` - Estudio del precio medio por ciudad y barrio para profundizar en el conocimiento de cada ciudad. 
- `availability` - Comprobación de la disponibilidad de alojamientos para conocer la concentración turística. 

### 🗃️ **Fuentes de Datos Integradas**
- **Inside Airbnb:** Listings base + 9.2M registros de calendar
- **INE:** Datos demográficos y de vivienda
- **Ayuntamientos:** Límites territoriales y regulaciones
- **Fuentes inmobiliarias:** Precios de mercado por zona

---

## 🚀 **INSTALACIÓN Y EJECUCIÓN**

### 📦 **1. Instalación de Dependencias**

```bash
# Clonar el repositorio
git clone [repo-url]
cd consultores_turismo_airbnb

# Instalar dependencias (actualizado con nuevas librerías)
pip install -r requirements.txt

# Nota: El proyecto incluye optimizaciones de performance 
# y nuevas funcionalidades de análisis temporal
```

### 📊 **2. Ejecutar Análisis**

```bash
# Ejecutar notebooks en orden:
# 1. Data Engineer 
jupyter notebook notebooks/persona_a_data_engineer.ipynb

# 2. Data Analyst
jupyter notebook notebooks/persona_b_data_analyst.ipynb

# 3. Business Intelligence
jupyter notebook notebooks/persona_c_business_intelligence.ipynb
```

### 🖥️ **3. Lanzar Dashboard**

```bash
# Ejecutar aplicación Streamlit (versión optimizada)
streamlit run streamlit_app/nuevo_app.py

# El dashboard incluye nuevas funcionalidades:
# - Análisis temporal avanzado
# - Métricas de intensidad turística
# - Performance mejorado para datasets grandes
# - Conclusiones y recomendaciones
```

---

## 📊 **RESULTADOS PRINCIPALES**

### 🏛️ **Madrid**
- **Barrios críticos:** Centro, Malasaña, Chueca
- **Densidad máxima:** 150+ alojamientos/km² en Centro
- **Recomendación:** Moratoria inmediata en zonas saturadas

### 🏖️ **Barcelona**
- **Situación:** Moratoria existente validada con nuestras métricas
- **Ciutat Vella:** Saturación crítica confirmada
- **Recomendación:** Reestablecer alquileres vacacionales controlados tras la desaturación por prohibición.

### 🏝️ **Mallorca**
- **Características:** Estacionalidad extrema, presión costera
- **Municipios críticos:** Palma, Calvià, Deià
- **Recomendación:** Gestión diferenciada por temporada y municipio

---

## 📈 **DASHBOARD INTERACTIVO**

### 🖥️ **Funcionalidades del Dashboard**
- 🗺️ **Mapas interactivos** de densidad por barrio con datos actualizados
- 📊 **KPIs en tiempo real** para las 3 ciudades con métricas consolidadas
- 🚨 **Sistema de alertas** por umbrales de saturación basado en tourism_intensity
- 📋 **Informes automatizados** para autoridades con datos de regulación
- 🔄 **Comparativas temporales** y entre ciudades con análisis estacional
- 📈 **Análisis de volatilidad** de precios y disponibilidad por zona
- ⚡ **Performance optimizado** con base de datos SQLite integrada

### 🎯 **Acceso**
- **Demo en vivo:** [URL del deploy]
- **Código fuente:** `/streamlit_app/`
- **Documentación:** `/docs/dashboard_manual.md`

---

## 🏛️ **APLICACIONES GUBERNAMENTALES**

### 📋 **Casos de Uso**
1. **Regulación de nuevas licencias**
   - Identificación de zonas saturadas
   - Propuestas de moratoria selectiva
   
2. **Monitoreo continuo**
   - Alertas tempranas de saturación
   - Informes ejecutivos automatizados
   
3. **Planificación urbana**
   - Zonificación turística inteligente
   - Distribución equilibrada de la actividad

### 🎯 **Recomendaciones por Ciudad**
- **Madrid:** Zonificación estricta centro + incentivos periferia
- **Barcelona:** Validación eficacia moratoria actual
- **Mallorca:** Plan sostenibilidad insular integral

---

## 🎤 **FUNCIONALIDAD DEL ESTUDIO**

### 📊 **Material para Gobiernos Locales**

Hemos desarrollado un **paquete completo de presentación ejecutiva** diseñado específicamente para consultores que presenten este análisis ante autoridades municipales y regionales.

#### 🎭 **Casos de Uso**
- **Ayuntamientos:** Presentación a alcaldes y concejales de turismo
- **Comunidades Autónomas:** Briefing a consejerías de turismo
- **Consultoras:** Pitch comercial a gobiernos locales
- **Investigadores:** Presentación de resultados en conferencias

---

## 👥 **EQUIPO DE DESARROLLO**

### 🔧 **Data Engineer**
- **Responsabilidad:** Extracción, limpieza y procesamiento de datos
- **Notebook:** `notebooks/persona_a_data_engineer.ipynb`
- **Entregables:** Datasets limpios y pipeline ETL

### 📊 **Data Analyst**
- **Responsabilidad:** Análisis estadístico y cálculo de KPIs
- **Notebook:** `notebooks/persona_b_data_analyst.ipynb`
- **Entregables:** Métricas validadas y correlaciones

### 💼 **Business Intelligence**
- **Responsabilidad:** Visualizaciones e insights de negocio
- **Notebook:** `notebooks/persona_c_business_intelligence.ipynb`
- **Entregables:** Dashboard y presentación ejecutiva

---

## 📚 **DOCUMENTACIÓN TÉCNICA**

### 🔗 **Enlaces Importantes**
- 🛠️ **Guía técnica:** `/docs/technical_guide.md`
- 📊 **Manual de KPIs:** `/docs/kpis_methodology.md`
- 🖥️ **Manual dashboard:** `/docs/dashboard_manual.md`

### 📋 **Fuentes de Datos y Referencias Bibliográficas**

#### 🔗 **Fuentes Primarias de Datos**

**1. Inside Airbnb** 📊
- **URL:** http://insideairbnb.com/
- **Descripción:** Datos detallados de listings de Airbnb en ciudades de todo el mundo
- **Datos utilizados:** Listings, precios, disponibilidad, ubicaciones, tipos de alojamiento
- **Última actualización:** Junio 2025
- **Cita:** Cox, M. (2025). *Inside Airbnb: Data and Tools for Understanding Airbnb's Impact on Cities*. http://insideairbnb.com/

**2. Instituto Nacional de Estadística (INE)** 🏛️
- **URL:** https://www.ine.es/
- **Descripción:** Datos oficiales de población, vivienda y demografía por barrios
- **Datos utilizados:** Población por barrios, parque de viviendas, densidad poblacional
- **Última actualización:** 2024
- **Cita:** Instituto Nacional de Estadística. (2024). *Estadísticas territoriales y demográficas*. Madrid: INE.

**3. Portal de Datos Abiertos de Barcelona** 🏙️
- **URL:** https://opendata-ajuntament.barcelona.cat/
- **Descripción:** Datos oficiales del Ayuntamiento de Barcelona
- **Datos utilizados:** Límites de barrios, normativas turísticas, indicadores urbanos
- **Cita:** Ajuntament de Barcelona. (2025). *Portal de Datos Abiertos*. Barcelona Open Data BCN.

**4. Ayuntamiento de Madrid - Datos Abiertos** 🌆
- **URL:** https://datos.madrid.es/
- **Descripción:** Portal oficial de datos abiertos de Madrid
- **Datos utilizados:** Barrios, distritos, regulaciones turísticas
- **Cita:** Ayuntamiento de Madrid. (2025). *Portal de Datos Abiertos*. Madrid.

**5. Govern de les Illes Balears** 🏝️
- **URL:** https://www.caib.es/
- **Descripción:** Datos oficiales del gobierno balear
- **Datos utilizados:** Regulaciones turísticas, datos territoriales de Mallorca
- **Cita:** Govern de les Illes Balears. (2025). *Datos Territoriales y Turísticos*. Palma de Mallorca.

#### � **Literatura Científica y Referencias**

**6. Estudios de Impacto Urbano**
- Guttentag, D. (2015). "Airbnb: Disruptive innovation and the rise of an informal tourism accommodation sector." *Current Issues in Tourism*, 18(12), 1192-1217.
- Wachsmuth, D., & Weisler, A. (2018). "Airbnb and the rent gap: Gentrification through the sharing economy." *Environment and Planning A*, 50(6), 1147-1170.

**7. Regulación y Políticas Públicas**
- Nieuwland, S., & van Melik, R. (2020). "Regulating Airbnb: How cities deal with perceived negative externalities of short-term rentals." *Cities*, 97, 102504.
- Cocola-Gant, A. (2016). "Holiday rentals: The new gentrification battlefront." *Sociological Research Online*, 21(3), 1-9.

**8. Metodología de Análisis Territorial**
- European Commission. (2020). *Guidelines for Sustainable Tourism Development in Urban Areas*. Brussels: EC Publications.
- UNWTO. (2019). *Overtourism? Understanding and Managing Urban Tourism Growth beyond Perceptions*. Madrid: World Tourism Organization.

#### 🗺️ **Datos Geoespaciales**

**9. OpenStreetMap** 🗺️
- **URL:** https://www.openstreetmap.org/
- **Descripción:** Datos cartográficos abiertos
- **Datos utilizados:** Límites administrativos, infraestructura urbana
- **Cita:** OpenStreetMap contributors. (2025). *OpenStreetMap*. https://www.openstreetmap.org/

**10. Natural Earth** 🌍
- **URL:** https://www.naturalearthdata.com/
- **Descripción:** Datos cartográficos públicos de alta calidad
- **Datos utilizados:** Límites territoriales, datos geoespaciales de referencia
- **Cita:** Natural Earth. (2025). *Free vector and raster map data*. https://www.naturalearthdata.com/

#### 💰 **Datos Económicos Complementarios**

**11. Turespaña - Instituto de Turismo de España** 🇪🇸
- **URL:** https://www.tourspain.es/
- **Descripción:** Estadísticas oficiales del turismo español
- **Datos utilizados:** Gasto turístico, llegadas, impacto económico
- **Cita:** Turespaña. (2025). *Estadísticas de Turismo de España*. Madrid: Instituto de Turismo de España.

**12. Eurostat** 🇪🇺
- **URL:** https://ec.europa.eu/eurostat
- **Descripción:** Oficina estadística de la Unión Europea
- **Datos utilizados:** Comparativas europeas de turismo y vivienda
- **Cita:** Eurostat. (2025). *Tourism and accommodation statistics*. Luxembourg: European Commission.

#### 🔧 **Herramientas y Tecnología**

**13. Tecnologías de Desarrollo**
- Python 3.9+ con bibliotecas: pandas, streamlit, plotly, folium
- SQLite para gestión de datos
- GitHub para control de versiones
- Streamlit Cloud para despliegue

**14. Estándares de Calidad de Datos**
- ISO 19115: Metadata for geographic information
- FAIR Data Principles: Findable, Accessible, Interoperable, Reusable

---

### 📊 **Metodología de Validación de Datos**

Todos los datos han sido procesados siguiendo estándares de calidad científica:
- ✅ **Verificación de fuentes:** Solo datos oficiales y reconocidos académicamente
- ✅ **Limpieza y normalización:** Procedimientos documentados de ETL
- ✅ **Validación cruzada:** Comparación entre múltiples fuentes
- ✅ **Actualización:** Datos del período 2024-2025
- ✅ **Reproducibilidad:** Código y metodología completamente documentados

---

## 🆕 **ÚLTIMAS ACTUALIZACIONES**

### 📅 **Junio 2025 - Versión Consolidada**

#### **🔄 Mejoras en Procesamiento de Datos**
- ✅ **Nuevo dataset consolidado:** `listings_unificado.csv`
- ✅ **Integración calendar data:** Procesados 9.2M registros de disponibilidad
- ✅ **Métricas avanzadas:** Tourism intensity, volatilidad, premiums estacionales
- ✅ **Base de datos optimizada:** SQLite integrada para consultas rápidas

#### **🖥️ Mejoras en Dashboard**
- ✅ **Performance optimizado** para datasets grandes
- ✅ **Nuevas visualizaciones** de análisis temporal 
- ✅ **Tema oscuro personalizado** para mejor experiencia de usuario
- ✅ **Alertas dinámicas** basadas en umbrales inteligentes
- ✅ **Exportación automática** de informes regulatorios

#### **📊 Nuevas Funcionalidades Analíticas**
- ✅ **Score tourism_intensity** (0-100) por alojamiento
- ✅ **Análisis estacional** completo (verano/invierno/fines de semana)
- ✅ **Volatilidad de precios** con detección de anomalías
- ✅ **Correlaciones avanzadas** entre variables territoriales
- ✅ **Predicción de saturación** por barrio y temporada

---

## 📞 **CONTACTO**

### 👥 **Equipo de Consultores en Turismo Sostenible**
- 🐙 **GitHub:** [/consultores-turismo/airbnb-analysis](https://github.com/AlfonsoCifuentes/consultora_turismo_airbnb/tree/main)

---

<div align="center">

### 🎉 **PROYECTO COMPLETADO CON ÉXITO** 🎉

**Contribuyendo al desarrollo urbano equilibrado y sostenible**

[![Streamlit](enlace deploy)

---

*📅 Última actualización: Junio 2025 | 🏛️ Consultores en Turismo Sostenible*  
*🆕 Versión consolidada con dataset avanzado y mejoras de performance*

</div>
