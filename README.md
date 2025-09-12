# 🏛️ **PROYECTO INSIDE AIRBNB - CONSULTORES EN TURISMO SOSTENIBLE**

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Optimizado-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)
🔗 **Enlaces Importantes**
- 🛠️ **Guía técnica:** `/docs/guia_tecnica.md`
- 📊 **Manual de KPIs:** `/docs/kpis_metodologia.md`
- 🖥️ **Manual dashboard:** `/docs/manual_dashboard.md`

![Status](https://img.shields.io/badge/Status-Complete-green?style=for-the-badge)

https://consultoraturismoairbnb.streamlit.app/

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
- 🔥 **Ocupación:** Demanda de alojamiento turístico durante el periodo analizado.

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
consultora_turismo_airbnb/
├── 📋 README.md                    # Documentación principal
├── 📦 requirements.txt             # Dependencias del proyecto
├── 
├── 📊 data/
│   ├── external/                   # Fuentes externas (INE, demografía, inmobiliarios)
│   │   ├── datos_demograficos.csv
│   │   ├── estadisticas_turismo.csv
│   │   ├── precios_alquileres_reales_procesados.csv
│   │   └── precios_inmobiliarios_reales.csv
│   └── processed/                  # Datos procesados y consolidados
│       ├── airbnb_consultores_turismo.db    # Base de datos principal
│       ├── listings_unificado.csv           # 🎯 Dataset principal (61k registros)
│       ├── listings_nuevo.csv               # Dataset con precios detallados
│       ├── kpis_por_barrio.csv             # KPIs territoriales
│       ├── kpis_por_ciudad.csv             # KPIs agregados por ciudad
│       └── neighbourhoods_*.geojson         # Geometrías de barrios
├── 
├── 📓 notebooks/
│   ├── persona_a_data_engineer.ipynb     # Extracción y limpieza
│   ├── persona_b_data_analyst.ipynb      # Análisis y KPIs
│   └── persona_c_business_intelligence.ipynb # Visualizaciones
├── 
├── 🖥️ streamlit_app/
│   ├── app_unificado.py            # 🚀 APLICACIÓN PRINCIPAL
│   ├── app_nuevo.py                # Dashboard alternativo
│   └── fondobannerconsultora.jpg   # Assets visuales
├── 
└── 📖 docs/                        # Documentación adicional
    ├── guia_tecnica.md             # Guía técnica del proyecto
    ├── kpis_metodologia.md         # Manual de metodología KPIs
    └── manual_dashboard.md         # Manual de usuario dashboard
```

---

## 📊 **DATASETS Y FUENTES DE DATOS**

### � **Dataset Principal: listings_unificado.csv**

Nuestro dataset consolidado combina datos de Inside Airbnb para **Barcelona, Madrid y Mallorca** con **61,289 registros** totales:

#### **🔍 CARACTERÍSTICAS PRINCIPALES**
- **📊 Estructura**: 11 columnas optimizadas para análisis urbano
- **💰 Precios**: Integración con `listings_nuevo.csv` para métricas económicas
- **🗺️ Geolocalización**: Coordenadas precisas por barrio y distrito
- **🏠 Tipología**: Clasificación completa de tipos de alojamiento
- **📈 Disponibilidad**: Datos de ocupación y disponibilidad anual

#### **� INTEGRACIÓN CON LA APLICACIÓN**
La aplicación principal `app_unificado.py`:
1. **Carga** `listings_unificado.csv` como base estructural
2. **Enriquece** con precios de `listings_nuevo.csv`
3. **Filtra** datos (elimina precios extremos ≥6501€, registros incompletos)
4. **Calcula** métricas en tiempo real (ocupación, densidad, impacto económico)

#### **📈 PRINCIPALES MÉTRICAS CALCULADAS**
- **Densidad turística** → Alojamientos por barrio y distrito
- **Ocupación estimada** → `(365 - availability_365) / 365 * 100`
- **Precio medio** → Promedio ponderado por ciudad/barrio
- **Impacto económico** → `listings × precio_medio × ocupación × días`

### 🗃️ **Fuentes de Datos Integradas**
- **Inside Airbnb**: Listings base con geolocalización y disponibilidad
- **Dataset Precios**: `listings_nuevo.csv` con análisis económico detallado
- **INE**: Datos demográficos y de vivienda por barrios
- **Ayuntamientos**: Límites territoriales (GeoJSON) y regulaciones

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
# 🚀 APLICACIÓN PRINCIPAL - Dashboard completo
streamlit run streamlit_app/app_unificado.py

# 📊 Dashboard alternativo (análisis específicos)
streamlit run streamlit_app/app_nuevo.py

# Funcionalidades del dashboard principal:
# - Análisis integrado de listings_unificado.csv + precios
# - Mapas interactivos por barrio y distrito
# - KPIs en tiempo real con filtrado automático
# - Métricas económicas y de saturación turística
# - Visualizaciones optimizadas para 61k registros
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

https://consultoraturismoairbnb.streamlit.app/

### 🖥️ **Funcionalidades del Dashboard Principal (`app_unificado.py`)**
- 🗺️ **Mapas interactivos** de densidad por barrio con datos en tiempo real
- 📊 **KPIs consolidados** para las 3 ciudades con métricas validadas
- 💰 **Análisis de precios** integrado de múltiples fuentes de datos
- 🚨 **Sistema de alertas** por umbrales de saturación territorial
- 📋 **Informes automatizados** listos para autoridades locales
- 🔄 **Filtrado inteligente** de datos extremos y registros corruptos
- ⚡ **Performance optimizado** para datasets de 60k+ registros

### 🎯 **Acceso y Tecnología**
- **Aplicación principal:** `streamlit_app/app_unificado.py`
- **Dataset base:** `listings_unificado.csv` (61,289 registros)
- **Enriquecimiento:** `listings_nuevo.csv` (datos de precios)
- **Documentación:** `/docs/manual_dashboard.md`

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
- 🛠️ **Guía técnica:** `/docs/guia_tecnica.md`
- 📊 **Manual de KPIs:** `/docs/kpis_metodologia.md`
- 🖥️ **Manual dashboard:** `/docs/manual_dashboard.md`

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

### 📅 **Julio 2025 - Versión Consolidada y Optimizada**

#### **🎯 Aplicación Principal: `app_unificado.py`**
- ✅ **Dashboard consolidado:** Integra `listings_unificado.csv` + precios de `listings_nuevo.csv`
- ✅ **Filtrado automático:** Elimina registros corruptos y precios extremos (≥6501€)
- ✅ **Performance optimizado:** Manejo eficiente de 61k registros
- ✅ **Métricas en tiempo real:** Cálculo dinámico de KPIs por ciudad/barrio
- ✅ **Interfaz mejorada:** Tema oscuro y visualizaciones optimizadas

#### **� Datasets Actualizados**
- ✅ **`listings_unificado.csv`:** Dataset principal con 61,289 registros
- ✅ **11 columnas optimizadas:** ID, ciudad, barrio, coordenadas, tipo, precio, disponibilidad
- ✅ **Integración de precios:** Enriquecimiento desde `listings_nuevo.csv`
- ✅ **Documentación completa:** Notebooks explicativos para cada dataset

#### **� Mejoras Técnicas**
- ✅ **Carga robusta:** Múltiples rutas de búsqueda para datasets
- ✅ **Gestión de errores:** Manejo inteligente de datos faltantes
- ✅ **Cálculos validados:** Métricas económicas y de saturación verificadas
- ✅ **Documentación actualizada:** README y docs técnicos sincronizados

---

## 📞 **CONTACTO**

### 👥 **Equipo de Consultores en Turismo Sostenible**
- 🐙 **GitHub:** [/consultores-turismo/airbnb-analysis](https://github.com/AlfonsoCifuentes/consultora_turismo_airbnb/tree/main)

---

<div align="center">

### 🎉 **PROYECTO COMPLETADO CON ÉXITO** 🎉

**Contribuyendo al desarrollo urbano equilibrado y sostenible**

**🚀 Aplicación Principal:** https://consultoraturismoairbnb.streamlit.app/

---

*📅 Última actualización: Julio 2025 | 🏛️ Consultores en Turismo Sostenible*  
*🆕 Versión consolidada con dataset unificado de 61k registros y análisis de precios integrado*

</div>
