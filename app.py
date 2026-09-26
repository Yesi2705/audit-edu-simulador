import streamlit as st
import pandas as pd
import plotly.express as px

def cargar_datos_inclusion():
    data = {
        "Provincia": ["Santo Domingo", "Santiago", "La Vega", "Barahona", "Puerto Plata"],
        "Estudiantes_Evaluados": [45, 32, 28, 15, 30],
        "Promedio_Nota": [85, 78, 92, 70, 88],
        "Tasa_Inclusion_%": [60, 75, 55, 40, 80]
    }
    return pd.DataFrame(data)

def mostrar_dashboard(df):
    st.set_page_config(page_title="InvestigaLab UFHEC", page_icon="📚")
    st.title("📊 InvestigaLab - Inclusión Financiera RD")
    st.markdown("**Autora: Yesenia Núñez - UFHEC - Contabilidad**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Estudiantes", df["Estudiantes_Evaluados"].sum())
    col2.metric("Promedio", f"{df['Promedio_Nota'].mean():.1f}")
    col3.metric("Inclusión", f"{df['Tasa_Inclusion_%'].mean():.1f}%")
    fig = px.bar(df, x="Provincia", y="Promedio_Nota", color="Tasa_Inclusion_%", title="Rendimiento vs Inclusión")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

def main():
    df = cargar_datos_inclusion()
    mostrar_dashboard(df)
    with st.sidebar:
        st.header("🤖 Asistente Pedagógico IA")
        pregunta = st.text_input("Escribe tu duda financiera:")
        if pregunta:
            st.success(f"Recomendación: Para '{pregunta}', se sugiere taller de educación financiera inclusiva.")

if __name__ == "__main__":
    main()
