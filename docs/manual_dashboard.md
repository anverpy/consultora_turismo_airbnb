# 🖥️ Manual del Dashboard

## 🚀 Acceso

```bash
streamlit run streamlit_app/app.py
```

URL: `http://localhost:8501`

## 📊 Navegación Principal

### Sidebar - Controles
- **Selector de ciudad**: Madrid, Barcelona, Mallorca
- **Filtros temporales**: Último mes, trimestre, año
- **Tipo de análisis**: Densidad, Ratio, Saturación

### Panel Principal

#### 🗺️ Mapa Interactivo
- **Zoom**: Rueda del ratón
- **Navegación**: Clic y arrastre
- **Información**: Hover sobre zonas coloreadas
- **Colores**:
  - 🟢 Verde: Niveles seguros
  - 🟡 Amarillo: Atención requerida
  - 🔴 Rojo: Zona crítica

#### 📈 Métricas Principales
- **KPIs en tiempo real** en la parte superior
- **Gráficos comparativos** por ciudad
- **Tabla de barrios críticos** en la parte inferior

## ⚠️ Sistema de Alertas

### Alertas Automáticas
- **🚨 Crítico**: KPI supera umbral rojo
- **⚠️ Atención**: KPI en zona amarilla
- **✅ Normal**: KPI en zona verde

### Interpretación de Colores
- **Rojo**: Acción inmediata requerida
- **Amarillo**: Monitoreo cercano
- **Verde**: Situación estable

## 📋 Exportación de Datos

1. Seleccionar ciudad y período
2. Hacer clic en "Exportar Reporte"
3. Formato disponible: CSV, PDF

## 🔧 Solución de Problemas

**Dashboard no carga**: Verificar que todas las dependencias estén instaladas
**Mapas no aparecen**: Comprobar conexión a internet
**Datos faltantes**: Verificar carpeta `data/` con archivos Inside Airbnb
