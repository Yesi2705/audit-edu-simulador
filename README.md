# audit-edu-simulador - InvestigaLab
### Simulador de Auditoría Contable - Yesenia Núñez - UFHEC

## 1. Descripción del Proyecto
InvestigaLab es un simulador y laboratorio interactivo para enseñar educación financiera en RD. Convierte datos de inclusión financiera por provincias en gráficos azules interactivos usando Python. Es parte del proyecto final de la página acfinal.netlify.app del profesor Guzmán Pérez.

## 2. Problemática Educativa Resuelta
En República Dominicana falta educación financiera accesible para estudiantes. Este proyecto ayuda a estudiantes de contabilidad a entender conceptos de auditoría y finanzas de forma visual y práctica, por provincias.

## 3. Stack Tecnológico - Paso 2 Desarrollo Antigravity
- Entorno principal: Antigravity (como exige la rúbrica)
- Stack elegido: Streamlit - Nivel Bajo (1 estrella)
- Justificación: Según la tabla oficial del profe, Streamlit es para dashboards interactivos y visualización de datos. Se eligió por ser nivel bajo y fácil de usar. No se usó Flask (nivel medio) ni Django (nivel alto) por su complejidad.

## 4. Estructura del Proyecto - Paso 3
- app.py: Dashboard principal con filtros por provincia, gráficos de barras y código documentado
- requirements.txt: streamlit, pandas, plotly
- README.md: Documentación
- datos.csv: Datos de inclusión financiera RD

## 5. Buenas Prácticas - Paso 4 Documentación
- Commits frecuentes (Compromiso inicial, Refactorizar app.py)
- Código con estándar PEP-8
- Funciones documentadas con comentarios

## 6. Cómo Ejecutar - Paso 5 y 6
1. git clone https://github.com/Yesi2705/audit-edu-simulador.git
2. pip install -r requirements.txt
3. streamlit run app.py
4. Se abre en http://localhost:8501
5. Despliegue Web: https://audit-edu-simulador.streamlit.app (agregar cuando se despliegue)

## 7. Video de Sustentación - Paso 7
Video 3 minutos: [Pegar aquí link de YouTube]
El video muestra el dashboard funcionando en localhost:8501 con gráficos por provincias.

## 8. Entrega Final - Paso 8
Autora: Yesenia Núñez - Contabilidad UFHEC
Repo: https://github.com/Yesi2705/audit-edu-simulador
Materia: Programación Python aplicada a la educación
