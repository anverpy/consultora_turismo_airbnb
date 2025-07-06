
with tab7:
    st.header("📅 Ocupación Turística")

    st.markdown(f"### 🏙️ Análisis de Ocupación en {ciudad_seleccionada}")

    st.markdown("""<div style="background-color: rgba(0, 212, 255, 0.08); border-left: 3px solid #00d4ff; padding: 10px; margin-bottom: 20px; border-radius: 3px;">
    <p style="margin: 0; font-size: 0.9rem; line-height: 1.4; color: #f2f2f2;">
    📅 <strong>Esta sección muestra cuántos días al año están ocupados o libres los alojamientos turísticos</strong> (Airbnb, apartamentos turísticos) en la ciudad seleccionada, y cómo evoluciona la ocupación a lo largo de los meses.
    </p></div>""", unsafe_allow_html=True)

    df = datasets.get('listings_precios', pd.DataFrame())
    if df.empty or 'availability_365' not in df.columns:
        st.warning("⚠️ No hay datos de ocupación disponibles para mostrar esta sección.")

    if 'city' in df.columns:
        df = df[df['city'].str.lower() == ciudad_seleccionada.lower()]

    avail = pd.to_numeric(df['availability_365'], errors='coerce').dropna()
    total_listings = len(avail)
    if total_listings == 0:
        st.warning("⚠️ No hay datos de ocupación válidos para la ciudad seleccionada.")

    dias_libres_total = avail.sum()
    dias_ocupados_total = total_listings * 365 - dias_libres_total

    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="📆 Días Ocupados (Total)",
            value=f"{int(dias_ocupados_total):,}",
            help="Suma de días al año en que los alojamientos están ocupados (reservados) en el periodo analizado."
        )
    with col2:
        st.metric(
            label="🛏️ Días Libres (Total)",
            value=f"{int(dias_libres_total):,}",
            help="Suma de días al año en que los alojamientos están libres (no reservados) en el periodo analizado."
        )

    st.markdown("""<div style="background-color: rgba(40, 167, 69, 0.08); border: 1px solid #28a745; border-radius: 8px; padding: 12px; margin-bottom: 15px;">
    <p style="margin: 0; font-size: 0.9rem; line-height: 1.4; color: #f2f2f2;">
    <strong>💡 ¿Qué significan estos números?</strong>  
    Un mayor número de días ocupados indica alta demanda turística. Muchos días libres pueden señalar estacionalidad o baja demanda.
    </p></div>""", unsafe_allow_html=True)

    st.markdown("### 📈 Evolución Mensual de la Ocupación")

    meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    factor_estacional = [0.6, 0.65, 0.75, 0.85, 0.95, 1.1, 1.3, 1.35, 1.15, 0.9, 0.7, 0.65]
    ocupacion_media = (365 - avail.mean()) / 365
    ocupacion_mensual = [ocupacion_media * 365 / 12 * f for f in factor_estacional]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=meses,
        y=ocupacion_mensual,
        mode='lines+markers',
        line=dict(color='#00d4ff', width=4),
        marker=dict(size=10, color='#28a745'),
        name="Días Ocupados (estimado)"
    ))
    fig.update_layout(
        title={
            'text': f"📈 Ocupación Turística Mensual Estimada - {ciudad_seleccionada}",
            'font': {'color': 'white', 'size': 18},
            'x': 0.5
        },
        xaxis_title="Mes",
        yaxis_title="Días Ocupados (media por listing)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400,
        margin=dict(l=20, r=20, t=60, b=50),
        showlegend=False
    )
    fig.update_xaxes(gridcolor='rgba(255,255,255,0.2)')
    fig.update_yaxes(gridcolor='rgba(255,255,255,0.2)')

    st.plotly_chart(fig, use_container_width=True, key="grafico_ocupacion_turistica")

    st.markdown("""<div style="background-color: rgba(0, 212, 255, 0.05); border-radius: 8px; padding: 12px; margin-top: 15px;">
    <p style="margin: 0; font-size: 0.9rem; line-height: 1.4; color: #f2f2f2;">
    <strong>🎯 Interpreta el gráfico:</strong>  
    Los picos en verano y festivos reflejan la estacionalidad del turismo urbano en España.  
    Si tienes datos mensuales reales, puedes sustituir la estimación por los valores reales.
    </p></div>""", unsafe_allow_html=True)