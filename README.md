# 🏛️ **PROYECTO INSIDE AIRBNB - CONSULTORES EN TURISMO SOSTENIBLE**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Stre### 🔗 **Enlaces Importantes**
- 🛠️ **Guía técnica:** `/docs/technical_guide.md`
- 📊 **Manual de KPIs:** `/docs/kpis_methodology.md`
- 🖥️ **Manual dashboard:** `/docs/dashboard_manual.md`
- 🎯 **Guión presentación:** `/docs/presentation_script.md`
- 📊 **Slides presentación:** `/docs/presentation_slides.md`t](https://img.shields.io/badge/Streamlit-1.29.0-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

### 📊 Análisis del Impacto Urbano de Airbnb en España
#### *Madrid • Barcelona • Mallorca*

---

**🎯 Proyecto desarrollado por el equipo de Consultores en Turismo Sostenible**  
*Evaluando el impacto urbano de Airbnb y proponiendo regulaciones sostenibles*

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

---

## 🏙️ **CIUDADES ANALIZADAS**

| 🌆 **Ciudad** | 📊 **Características** | 🎯 **Enfoque** |
|---|---|---|
| **🏛️ Madrid** | Capital, centro urbano, alta densidad | Regulación urbana integral |
| **🏖️ Barcelona** | Ciudad costera, turismo cultural/playa | Gestión saturación histórica |
| **🏝️ Mallorca** | Territorio insular, estacionalidad extrema | Sostenibilidad insular |

---

## 📁 **ESTRUCTURA DEL PROYECTO**

```
consultores_turismo_airbnb/
├── 📋 README.md                    # Documentación principal
├── 📦 requirements.txt             # Dependencias del proyecto
├── 
├── 📊 data/
│   ├── raw/                        # Datos originales Inside Airbnb
│   │   ├── madrid/
│   │   ├── barcelona/
│   │   └── mallorca/
│   ├── external/                   # Fuentes externas
│   └── processed/                  # Datos procesados
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

## 🚀 **INSTALACIÓN Y EJECUCIÓN**

### 📦 **1. Instalación de Dependencias**

```bash
# Clonar el repositorio
git clone [repo-url]
cd consultores_turismo_airbnb

# Instalar dependencias
pip install -r requirements.txt
```

### 📊 **2. Ejecutar Análisis**

```bash
# Ejecutar notebooks en orden:
# 1. Data Engineer (Persona A)
jupyter notebook notebooks/persona_a_data_engineer.ipynb

# 2. Data Analyst (Persona B) 
jupyter notebook notebooks/persona_b_data_analyst.ipynb

# 3. Business Intelligence (Persona C)
jupyter notebook notebooks/persona_c_business_intelligence.ipynb
```

### 🖥️ **3. Lanzar Dashboard**

```bash
# Ejecutar aplicación Streamlit
streamlit run streamlit_app/app.py
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
- **Recomendación:** Mantener y refinar regulación actual

### 🏝️ **Mallorca**
- **Características:** Estacionalidad extrema, presión costera
- **Municipios críticos:** Palma, Calvià, Deià
- **Recomendación:** Gestión diferenciada por temporada y municipio

---

## 📈 **DASHBOARD INTERACTIVO**

### 🖥️ **Funcionalidades**
- 🗺️ **Mapas interactivos** de densidad por barrio
- 📊 **KPIs en tiempo real** para las 3 ciudades
- 🚨 **Sistema de alertas** por umbrales de saturación
- 📋 **Informes automatizados** para autoridades
- 🔄 **Comparativas temporales** y entre ciudades

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

## 🎤 **PRESENTACIONES EJECUTIVAS**

### 📊 **Material para Gobiernos Locales**

Hemos desarrollado un **paquete completo de presentación ejecutiva** diseñado específicamente para consultores que presenten este análisis ante autoridades municipales y regionales.

#### 🎯 **Guión de Presentación (20 minutos)**
- **Archivo:** `/docs/presentation_script.md`
- **Estructura:** Introducción → Metodología → Resultados → Recomendaciones → Herramientas
- **Enfoque:** Consultor profesional con autoridad técnica
- **Incluye:** Material Q&A, gestión de objeciones, propuesta comercial

#### 📊 **Slides Detalladas (18 slides)**
- **Archivo:** `/docs/presentation_slides.md`
- **Contenido:** Especificaciones técnicas de cada slide
- **Visuales:** Mapas coropléticos, gráficos evolución, comparativas UE
- **Timing:** 1-2 minutos por slide con transiciones fluidas

#### 🎭 **Casos de Uso**
- **Ayuntamientos:** Presentación a alcaldes y concejales de turismo
- **Comunidades Autónomas:** Briefing a consejerías de turismo
- **Consultoras:** Pitch comercial a gobiernos locales
- **Investigadores:** Presentación de resultados en conferencias

---

## 👥 **EQUIPO DE DESARROLLO**

### 🔧 **Persona A - Data Engineer**
- **Responsabilidad:** Extracción, limpieza y procesamiento de datos
- **Notebook:** `notebooks/persona_a_data_engineer.ipynb`
- **Entregables:** Datasets limpios y pipeline ETL

### 📊 **Persona B - Data Analyst**
- **Responsabilidad:** Análisis estadístico y cálculo de KPIs
- **Notebook:** `notebooks/persona_b_data_analyst.ipynb`
- **Entregables:** Métricas validadas y correlaciones

### 💼 **Persona C - Business Intelligence**
- **Responsabilidad:** Visualizaciones e insights de negocio
- **Notebook:** `notebooks/persona_c_business_intelligence.ipynb`
- **Entregables:** Dashboard y presentación ejecutiva

---

## 📚 **DOCUMENTACIÓN TÉCNICA**

### 🔗 **Enlaces Importantes**
- 🛠️ **Guía técnica:** `/docs/technical_guide.md`
- 📊 **Manual de KPIs:** `/docs/kpis_methodology.md`
- 🖥️ **Manual dashboard:** `/docs/dashboard_manual.md`
- 🎯 **Guión presentación:** `/docs/presentation_script.md`
- 📊 **Slides presentación:** `/docs/presentation_slides.md`

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

## 🏆 **IMPACTO Y RESULTADOS**

### 📈 **Métricas de Éxito**
- ✅ **3 ciudades analizadas** con metodología unificada
- ✅ **15+ KPIs calculados** y validados
- ✅ **Dashboard interactivo** completamente funcional
- ✅ **Recomendaciones específicas** por zona y ciudad
- ✅ **Sistema de alertas** automatizado

### 🎯 **Aplicabilidad**
- 🏛️ **Gobiernos locales:** Herramientas de regulación basadas en datos
- 📊 **Investigadores:** Metodología replicable para otras ciudades
- 🏢 **Sector turístico:** Insights para desarrollo sostenible

---

## 📞 **CONTACTO**

### 👥 **Equipo de Consultores en Turismo Sostenible**
- 📧 **Email:** consultores@turismo-sostenible.es
- 🌐 **Web:** www.turismo-sostenible.es
- 📱 **LinkedIn:** /company/consultores-turismo-sostenible
- 🐙 **GitHub:** /consultores-turismo/airbnb-analysis

---

<div align="center">

### 🎉 **PROYECTO COMPLETADO CON ÉXITO** 🎉

**Contribuyendo al desarrollo urbano equilibrado y sostenible**

[![Streamlit](https://img.shields.io/badge/Demo-Streamlit-red?style=for-the-badge)](https://airbnb-analysis.streamlit.app)
[![GitHub](https://img.shields.io/badge/Code-GitHub-black?style=for-the-badge)](https://github.com/consultores-turismo/airbnb-analysis)
[![Documentation](https://img.shields.io/badge/Docs-GitBook-blue?style=for-the-badge)](#)

---

*📅 Desarrollado en Junio 2025 | 🏛️ Consultores en Turismo Sostenible*

</div>
