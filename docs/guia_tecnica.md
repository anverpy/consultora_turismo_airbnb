# 🔧 Guía Técnica del Proyecto

## 🏗️ Arquitectura

```text
consultores_turismo_airbnb/
├── streamlit_app/          # Dashboard Streamlit
├── notebooks/              # Análisis por roles
├── data/                   # Datos Inside Airbnb
└── docs/                   # Documentación
```

## 💾 Estructura de Datos

### Fuentes de Datos

- **Inside Airbnb**: `listings.csv`, `calendar.csv`, `reviews.csv`
- **Formato esperado**: CSV con encoding UTF-8
- **Ubicación**: `data/raw/{ciudad}/`

### Campos Principales

| Campo | Descripción | Tipo |
|-------|-------------|------|
| `id` | ID único del alojamiento | int |
| `latitude` | Coordenada latitud | float |
| `longitude` | Coordenada longitud | float |
| `neighbourhood_cleansed` | Barrio | string |
| `room_type` | Tipo de alojamiento | string |
| `price` | Precio por noche | string |
| `availability_365` | Días disponibles/año | int |

## 🔄 Flujo de Procesamiento

### 1. Data Engineering (Notebook A)

```python
# Carga y limpieza de datos
df = pd.read_csv('data/raw/madrid/listings.csv')
df_clean = clean_data(df)
df_clean.to_csv('data/processed/madrid_clean.csv')
```

### 2. Data Analysis (Notebook B)

```python
# Cálculo de KPIs
density = calculate_density(df_clean)
ratio = calculate_ratio(df_clean)
saturation = calculate_saturation(df_clean)
```

### 3. Business Intelligence (Notebook C)

```python
# Visualizaciones y dashboard
create_maps(density_data)
generate_dashboard_data()
```

## 🚀 Deployment

### Local

```bash
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

### Streamlit Cloud

1. Subir repositorio a GitHub
2. Conectar con Streamlit Cloud
3. Deploy automático desde main branch

## 🛠️ Dependencias Críticas

- **streamlit==1.28.1**: Framework dashboard
- **folium==0.14.0**: Mapas interactivos
- **plotly==5.17.0**: Gráficos avanzados
- **pandas==2.1.4**: Manipulación datos

## 🐛 Debug Común

### Error: Módulo no encontrado

```bash
pip install -r requirements.txt --upgrade
```

### Error: Datos no cargan

```python
# Verificar estructura de archivos
import os
print(os.listdir('data/raw/'))
```

### Error: Mapas no renderizan

```python
# Verificar coordenadas válidas
df['latitude'].describe()
df['longitude'].describe()
```
