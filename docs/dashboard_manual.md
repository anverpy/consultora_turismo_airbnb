# 🖥️ **MANUAL DEL DASHBOARD - GUÍA DE USUARIO**

## 🎯 **INTRODUCCIÓN**

El Dashboard Regulatorio de Turismo Urbano es una herramienta interactiva diseñada para gobiernos locales, investigadores y profesionales del sector turístico. Permite analizar el impacto de Airbnb en tiempo real y generar insights para la toma de decisiones regulatorias.

---

## 🚀 **ACCESO AL DASHBOARD**

### 🌐 **URL de Acceso**
- **Demo en vivo:** https://dashboard-turismo-sostenible.streamlit.app
- **Versión local:** http://localhost:8501

### 🔑 **Credenciales**
- **Acceso público:** Sin restricciones
- **Datos sensibles:** Protegidos por configuración

### 💻 **Requisitos del Sistema**
- **Navegador:** Chrome 90+, Firefox 88+, Safari 14+
- **Conexión:** Banda ancha recomendada
- **JavaScript:** Habilitado

---

## 📱 **INTERFAZ PRINCIPAL**

### 🎨 **Diseño y Tema**

El dashboard utiliza un **tema oscuro profesional** optimizado para:
- ✅ Reducir fatiga visual en sesiones largas
- ✅ Mejorar contraste de datos y gráficos
- ✅ Presentación profesional para reuniones ejecutivas

### 🧭 **Navegación Principal**

```
🏛️ Dashboard Regulatorio de Turismo Urbano
├── 🎛️ Panel de Control (Sidebar)
├── 📊 Métricas Clave (Header)
└── 📋 Contenido Principal (Tabs)
```

---

## 🎛️ **PANEL DE CONTROL LATERAL**

### 🏙️ **Selector de Ciudad**

**Ubicación:** Parte superior del sidebar

**Opciones disponibles:**
- 🌆 **Madrid** - Capital y centro urbano
- 🏖️ **Barcelona** - Ciudad costera mediterránea  
- 🏝️ **Mallorca** - Territorio insular balear

**Funcionalidad:**
- Filtrado automático de todos los datos
- Actualización sincronizada de gráficos
- Mantenimiento de filtros aplicados

### 🔍 **Filtros de Análisis**

#### ✅ **Solo barrios críticos**
- **Función:** Muestra únicamente barrios con alta saturación
- **Criterio:** Ratio entire home > umbral seleccionado
- **Uso recomendado:** Identificación rápida de zonas problemáticas

#### 📊 **Umbral de saturación (%)**
- **Rango:** 0-100%
- **Default:** 50%
- **Aplicación:** Filtrado dinámico de barrios críticos
- **Recomendación:** 70% para análisis regulatorio

### 👥 **Información del Equipo**

**Roles del proyecto:**
- **🔧 Persona A:** Data Engineer
- **📊 Persona B:** Data Analyst  
- **💼 Persona C:** Business Intelligence

**Estadísticas del proyecto:**
- **61,114** listings procesados
- **3** ciudades principales
- **252** barrios analizados
- **Datos económicos** integrados

---

## 📊 **MÉTRICAS CLAVE (HEADER)**

### 🏠 **Total Listings**
- **Descripción:** Número total de alojamientos activos
- **Interpretación:** Volumen del mercado Airbnb
- **Delta:** Comparativa vs año anterior (+10%)

### 🚨 **Barrios de Atención**
- **Descripción:** Barrios que superan 70% ratio entire home
- **Uso:** Priorización de intervenciones regulatorias
- **Delta:** Crecimiento trimestral

### ⚖️ **Ratio Promedio T/R**
- **Descripción:** % promedio turístico vs residencial
- **Umbrales:**
  - Verde: < 40% (Sostenible)
  - Amarillo: 40-60% (Moderado)
  - Rojo: > 60% (Crítico)

### 💰 **Precio Medio**
- **Descripción:** Precio promedio ponderado por noche
- **Benchmark:** Comparativa europea
- **Moneda:** Euros (€)

---

## 📋 **CONTENIDO PRINCIPAL - TABS**

## 📊 **TAB 1: RESUMEN KPIs**

### 🏆 **KPIs Principales del Ecosistema Turístico**

#### **Fila 1: KPIs de Volumen**

**🏠 Total de Listings**
- **Valor:** Número absoluto con comparativa anual
- **Análisis:** Contexto europeo y crecimiento sostenido
- **Acción:** Clic para detalles por ciudad

**🚨 Barrios en Situación Crítica**
- **Valor:** Conteo de barrios > 70% ratio
- **Análisis:** Identificación de gentrificación acelerada
- **Acción:** Acceso directo a lista de barrios

**⚖️ Ratio Turístico/Residencial**
- **Valor:** Porcentaje promedio nacional
- **Análisis:** Clasificación de nivel (Crítico/Moderado/Sostenible)
- **Acción:** Comparativa con estándares UE

#### **Fila 2: KPIs Económicos**

**💰 Precio Medio por Noche**
- **Valor:** Precio en euros con competitividad
- **Análisis:** Comparativa con mercado europeo
- **Clasificación:** Alta/Media/Baja competitividad

**📈 Tasa de Ocupación Estimada**
- **Valor:** Porcentaje basado en disponibilidad
- **Análisis:** Demanda robusta vs mercado maduro
- **Benchmark:** 60% umbral mercado maduro

**💼 Ingresos Anuales Estimados**
- **Valor:** Millones de euros anuales
- **Análisis:** Contribución al PIB turístico
- **Cálculo:** Listings × Precio × Ocupación × 365

### 🏙️ **KPIs Desglosados por Ciudad**

**Expanders interactivos** para cada ciudad con:

**Métricas por ciudad:**
- Participación en el total nacional
- Ratio entire home específico
- Precio medio local

**Análisis específico:**
- **Madrid:** Diversificación y regulación efectiva
- **Barcelona:** Concentración centro histórico
- **Mallorca:** Dependencia estacional

### 🏘️ **KPIs de Impacto Social y Urbano**

**📊 Índice de Concentración**
- **Metodología:** % oferta en top 10% barrios densos
- **Niveles:** Alta/Media/Baja concentración
- **Aplicación:** Políticas redistributivas

**🏠 Viviendas Convertidas (Estimación)**
- **Cálculo:** Ratio × Total Listings
- **Impacto:** Presión sobre oferta residencial
- **Contexto:** Significación en mercado local

### 🎯 **Recomendaciones Basadas en KPIs**

**Sistema de alertas automático:**
- **🔴 > 60%:** Acción urgente requerida
- **🟠 40-60%:** Regulación preventiva
- **🟢 < 40%:** Situación controlada

### 🇪🇺 **Comparativa con Estándares Europeos**

**Tres métricas benchmark:**
1. **Objetivo Ratio UE (30%):** Cumplimiento/Exceso
2. **Objetivo Concentración (40%):** Cumplimiento/Exceso  
3. **Precio Competitivo (90€):** Competitivo/Elevado

---

## 🗺️ **TAB 2: MAPAS DE IMPACTO**

### 🗺️ **Mapa Coroplético Interactivo**

**Características:**
- **Tecnología:** Plotly + MapBox
- **Estilo:** Tema oscuro (carto-darkmatter)
- **Interactividad:** Hover, zoom, pan
- **Datos:** Saturación por barrio

**Uso:**
1. Seleccionar ciudad en sidebar
2. Aplicar filtros de saturación
3. Explorar barrios haciendo hover
4. Hacer zoom en áreas específicas

**Información en hover:**
- Nombre del barrio
- Total listings
- Precio medio
- Ratio entire home

### 📥 **Descarga de Datos**

**Botón:** "📥 Descargar datos de barrios"
- **Formato:** CSV
- **Contenido:** Datos filtrados actuales
- **Nombre:** datos_barrios_filtrados.csv
- **Uso:** Análisis externo, informes

### 📊 **Mapas Adicionales**

#### **🏘️ Saturación por Barrio**
- **Tipo:** Gráfico de barras horizontal
- **Datos:** Top 15 barrios por saturación
- **Color:** Escala de rojos (mayor saturación = más rojo)
- **Rotación:** Etiquetas -45° para legibilidad

#### **📊 Densidad vs Precio**
- **Tipo:** Scatter plot con burbujas
- **Ejes:** 
  - X: Total listings
  - Y: Precio medio
- **Tamaño burbuja:** Capacidad total
- **Color:** Ratio entire home

### 🎨 **Interpretación de Mapas**

**Leyenda de colores saturación:**
- 🟢 **< 40%:** Sostenible - Sin restricciones
- 🟡 **40-60%:** Monitoreo - Evaluar tendencias  
- 🟠 **60-80%:** Preventivo - Limitar licencias
- 🔴 **> 80%:** Urgente - Moratoria temporal

---

## 📊 **TAB 3: ANÁLISIS COMPARATIVO**

### 🏙️ **Gráfico Comparativo Principal**
- **Tipo:** Gráfico de barras
- **Datos:** Total listings por ciudad
- **Interactividad:** Hover para valores exactos
- **Color:** Escala azul (mayor volumen = más oscuro)

### 📊 **Distribución por Tipo**
- **Tipo:** Gráfico circular (pie chart)
- **Datos:** Proporción de listings por ciudad
- **Interactividad:** Clic en sectores
- **Etiquetas:** Porcentajes automáticos

### 📋 **Tabla Resumen Comparativa**
**Columnas mostradas:**
- Ciudad
- Total listings
- Ratio entire home %
- Precio medio €

**Funcionalidades:**
- Ordenación por columnas
- Búsqueda rápida
- Exportación (copiar/CSV)

### 💰 **Contexto Económico Nacional**
- **Gasto Turístico Nacional:** Datos Turespaña
- **PIB Turístico:** Contribución sector
- **Fuente:** Datos oficiales actualizados

---

## 🚨 **TAB 4: SISTEMA DE ALERTAS**

### 🚨 **Alertas Automáticas por Saturación**

**Dashboard de alertas en 4 columnas:**

#### 🔴 **CRÍTICOS**
- **Criterio:** Ratio > 80%
- **Acción:** Intervención inmediata
- **Visual:** Gradiente rojo con sombra

#### 🟠 **ALTOS** 
- **Criterio:** Ratio 60-80%
- **Acción:** Regulación preventiva
- **Visual:** Gradiente naranja

#### 🟡 **MODERADOS**
- **Criterio:** Ratio 40-60% 
- **Acción:** Monitoreo intensivo
- **Visual:** Gradiente amarillo

#### 🟢 **SOSTENIBLES**
- **Criterio:** Ratio < 40%
- **Acción:** Mantener observación
- **Visual:** Gradiente verde

### 🎯 **Tabla de Barrios Críticos**
- **Filtro:** Solo CRÍTICOS y ALTOS
- **Ordenación:** Por ratio descendente
- **Columnas:** Barrio, Ciudad, Nivel, Ratio, Listings
- **Exportación:** CSV disponible

### 📈 **Tendencias y Evolución**
- **Tipo:** Gráfico de líneas temporal
- **Datos:** Proyección crecimiento por ciudad
- **Período:** Enero 2024 - Junio 2025
- **Interactividad:** Hover para valores puntuales

---

## 💡 **TAB 5: RECOMENDACIONES**

### 🔧 **Simulador de Impacto de Políticas**

#### **Parámetros de Simulación:**
- **% Reducción nuevas licencias:** Slider 0-100%
- **Plazo implementación:** Select (3/6/12 meses)

#### **Impacto Estimado:**
- **Reducción estimada listings:** Cálculo automático
- **Nuevas viviendas disponibles:** 70% de reducción
- **Actualización:** Tiempo real

### 📊 **Análisis por Ciudad**

Para cada ciudad muestra:
- **Métricas actuales:** Total listings y % entire home
- **Deltas estimados:** Comparativas temporales
- **Recomendaciones específicas:**
  - 🔴 Moratoria inmediata (> 75%)
  - 🟠 Límites graduales (60-75%)
  - 🟡 Monitoreo intensivo (40-60%)
  - 🟢 Política actual (< 40%)

### 📋 **Casos de Uso para Gobierno Local**

**Expanders interactivos** con:

#### 🏛️ **Moratoria Selectiva**
- **Descripción:** Suspender licencias >75% ratio
- **Aplicación:** Barrios históricos saturados
- **Plazo:** 6-12 meses

#### 📊 **Zonificación Inteligente**
- **Descripción:** Niveles restricción por zona
- **Aplicación:** Planificación urbana equilibrada
- **Plazo:** 12-24 meses

#### 🔍 **Monitoreo Continuo**
- **Descripción:** Alertas automáticas trimestrales
- **Aplicación:** Detección temprana problemas
- **Plazo:** Permanente

---

## 🎯 **CASOS DE USO POR PERFIL**

### 🏛️ **Funcionarios Públicos**

**Flujo de trabajo recomendado:**
1. **Inicio:** Revisar métricas clave en header
2. **Análisis:** Tab KPIs para contexto general
3. **Territorial:** Tab Mapas para localización
4. **Alertas:** Tab Sistema identificar urgencias
5. **Acción:** Tab Recomendaciones para medidas

**Informes automáticos:**
- Exportar datos filtrados
- Screenshots de mapas
- Métricas para presentaciones

### 📊 **Investigadores**

**Funcionalidades de análisis:**
- Descarga datasets completos
- Metodología documentada
- Código fuente accesible
- Referencias bibliográficas

**Casos de estudio:**
- Comparativa entre ciudades
- Evolución temporal
- Impacto de regulaciones

### 🏢 **Sector Turístico**

**Insights de negocio:**
- Identificación oportunidades
- Análisis competitivo
- Optimización pricing
- Gestión estacional

**Métricas clave:**
- Ocupación por zona
- Precios competitivos
- Saturación mercado

---

## 🔧 **CARACTERÍSTICAS TÉCNICAS**

### ⚡ **Rendimiento**
- **Tiempo carga inicial:** < 3 segundos
- **Actualización filtros:** < 1 segundo
- **Generación gráficos:** < 2 segundos
- **Cache inteligente:** Datos pre-cargados

### 📱 **Responsividad**
- **Desktop:** Optimizado para 1920x1080
- **Tablet:** Adaptación automática
- **Mobile:** Vista simplificada
- **Navegadores:** Chrome, Firefox, Safari

### 🔒 **Seguridad**
- **Datos sensibles:** Protegidos
- **Acceso:** Sin autenticación requerida
- **HTTPS:** Conexión segura
- **Rate limiting:** Protección sobrecarga

---

## 🆘 **SOLUCIÓN DE PROBLEMAS**

### ❌ **Problemas Comunes**

#### **Dashboard no carga**
1. Verificar conexión internet
2. Actualizar navegador
3. Limpiar cache y cookies
4. Probar navegador diferente

#### **Mapas no se muestran**
1. Habilitar JavaScript
2. Verificar bloqueadores contenido
3. Comprobar extensiones navegador
4. Recargar página (F5)

#### **Datos incorrectos**
1. Verificar filtros aplicados
2. Cambiar ciudad seleccionada
3. Resetear filtros (recargar página)
4. Comprobar fecha última actualización

#### **Gráficos en blanco**
1. Esperar carga completa
2. Verificar filtros muy restrictivos
3. Cambiar configuración sidebar
4. Contactar soporte técnico

### 📞 **Soporte Técnico**
- **Email:** soporte@consultores-turismo.es
- **Horario:** L-V 9:00-18:00 CET
- **Documentación:** /docs/
- **GitHub Issues:** Para desarrolladores

---

## 📚 **RECURSOS ADICIONALES**

### 🎓 **Tutoriales**
- **Video guía:** 15 min tutorial completo
- **Manual PDF:** Versión imprimible
- **FAQ:** Preguntas frecuentes

### 📖 **Documentación Técnica**
- **Guía técnica:** /docs/technical_guide.md
- **Manual KPIs:** /docs/kpis_methodology.md
- **API:** Endpoints disponibles

### 🔗 **Enlaces Útiles**
- **Demo live:** URL dashboard
- **Código fuente:** GitHub repository
- **Datos raw:** Inside Airbnb
- **Metodología:** Artículos científicos

---

<div align="center">

## 🎯 **DASHBOARD: DECISIONES INTELIGENTES BASADAS EN DATOS**

*Interfaz intuitiva • Análisis potente • Resultados accionables*

**Consultores en Turismo Sostenible • Junio 2025**

</div>
