📊 Análisis de Ventas de Tienda Online
Pipeline ETL en Python + Dashboard de Inteligencia de Negocios
📌 Resumen Ejecutivo

Este proyecto presenta una solución integral de análisis de datos para una tienda online, simulando un entorno real de trabajo de un Analista de Datos.

Se desarrolló un pipeline ETL en Python para integrar múltiples fuentes de información comercial, transformarlas en un modelo analítico y generar indicadores clave de negocio. Los resultados se visualizaron mediante un dashboard interactivo en Power BI, orientado a facilitar la toma de decisiones estratégicas.

El enfoque del proyecto combina ingeniería de datos básica, análisis exploratorio y business intelligence.

🎯 Objetivos del Proyecto

Integrar datos provenientes de distintas entidades del negocio

Construir métricas comerciales clave

Analizar el desempeño de ventas y rentabilidad

Detectar patrones de comportamiento en clientes y productos

Presentar hallazgos mediante visualizaciones ejecutivas

⚙️ Tecnologías Utilizadas
Tecnología	Aplicación
Python	Desarrollo del proceso ETL
Pandas	Limpieza, transformación y análisis de datos
NumPy	Soporte para cálculos numéricos
Power BI	Visualización y construcción del dashboard
Git & GitHub	Control de versiones y portfolio profesional
🗂️ Arquitectura del Proyecto
tienda-online-analytics/
│
├── data/
│   ├── raw/              # Datos originales
│   └── processed/        # Dataset final listo para análisis
│
├── src/
│   ├── extract.py        # Lectura de datos
│   ├── transformaciones.py  # Limpieza, joins y métricas
│   └── main.py           # Orquestación del pipeline ETL
│
├── dashboard/
│   └── dashboard.pbix    # Dashboard de Power BI
│
├── requirements.txt
└── README.md

🔄 Proceso ETL
1️⃣ Extracción

Se integraron múltiples fuentes de datos del negocio:

Clientes

Productos

Órdenes

Detalle de órdenes

2️⃣ Transformación

Se aplicaron procesos típicos de preparación de datos:

Unión de tablas mediante claves primarias y foráneas

Estandarización de formatos de fecha

Validación de tipos de datos

Eliminación de inconsistencias

Creación de métricas derivadas

3️⃣ Carga

El dataset final consolidado se exportó en formato CSV para su consumo en Power BI.

📊 Métricas de Negocio Construidas
Métrica	Definición
Ventas Totales	Precio × Cantidad vendida
Costos Totales	Costo unitario × Cantidad vendida
Ganancia	Ventas − Costos
Margen de Ganancia (%)	(Ganancia / Ventas) × 100
Ventas por Mes	Evolución temporal del negocio
Top Productos	Productos con mayor volumen de ventas
📈 Dashboard de Power BI

El dashboard fue diseñado con un enfoque ejecutivo, permitiendo:

Seguimiento del rendimiento general de ventas

Evaluación de rentabilidad mediante margen de ganancia

Identificación de productos de alto desempeño

Análisis de tendencias mensuales

Segmentación por cliente y ubicación geográfica

El diseño visual prioriza claridad, contraste y jerarquía de información para facilitar la interpretación.

🚀 Cómo Ejecutar el Proyecto

1️⃣ Clonar el repositorio

git clone https://github.com/TU-USUARIO/tienda-online-analytics.git
cd tienda-online-analytics


2️⃣ Instalar dependencias

pip install -r requirements.txt


3️⃣ Ejecutar el pipeline ETL

python src/main.py


Esto generará el dataset procesado en la carpeta data/processed.

4️⃣ Abrir dashboard/dashboard.pbix en Power BI para visualizar el informe.

🧠 Hallazgos y Conclusiones

A partir del análisis de datos se pueden extraer conclusiones clave para la toma de decisiones:

📌 La rentabilidad no siempre coincide con el volumen de ventas: algunos productos venden mucho pero tienen bajo margen, lo que impacta en la ganancia total.

📌 Existen variaciones mensuales en el desempeño comercial, lo que sugiere estacionalidad o impacto de promociones.

📌 Un grupo reducido de productos concentra gran parte de las ventas, indicando oportunidades para estrategias de cross-selling y control de stock.

📌 El análisis de margen permite priorizar productos estratégicos, no solo los más vendidos.

Este tipo de análisis permite pasar de una visión operativa (ventas) a una visión estratégica (rentabilidad).

💼 Enfoque Profesional

Este proyecto refleja tareas reales de un Data Analyst:

✔ Integración y modelado de datos
✔ Construcción de KPIs de negocio
✔ Análisis exploratorio
✔ Visualización orientada a decisiones
✔ Comunicación de insights

👤 Autor

Bruno Argañaraz
Linkedin : https://www.linkedin.com/in/bruno-arga%C3%B1araz-726a4a199/
Email : bruno.r.arganaraz@gmail.com
