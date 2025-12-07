# ⚾ Análisis de Datos MLB con Machine Learning

Proyecto de Inteligencia Artificial - Análisis y predicción de lanzamientos de béisbol usando datos de Statcast MLB (2015-2024)

## 📋 Descripción

Este proyecto realiza un análisis exhaustivo de datos de pitcheo de las Grandes Ligas de Béisbol (MLB) utilizando técnicas de ciencia de datos y machine learning. El proyecto abarca desde la descarga y exploración de datos hasta la construcción de modelos predictivos avanzados y clustering de estilos de lanzamiento.

### Objetivos principales:
- 📊 Análisis exploratorio de datos de lanzamientos MLB
- 🎯 Predicción de tipos de lanzamiento
- 📈 Predicción de resultados de bateo
- 🤖 Modelos avanzados de clasificación
- 🔍 Clustering de estilos de pitcheo

## 🗂️ Estructura del Proyecto

```
IA-Proyecto/
│
├── notebooks/                          # Análisis en Jupyter Notebooks
│   ├── 01_descarga_datos.ipynb        # Descarga de datos de Statcast (2015-2024)
│   ├── 02_exploracion_inicial.ipynb   # Exploración inicial del dataset
│   ├── 03_analisis_datos.ipynb        # Análisis estadístico detallado
│   ├── 04_prediccion_lanzamiento.ipynb # Modelos de predicción de pitch type
│   ├── 05_prediccion_resultados.ipynb  # Predicción de eventos de bateo
│   ├── 06_prediccion_avanzada.ipynb    # Modelos avanzados (XGBoost, etc.)
│   └── 07_clustering_estilos.ipynb     # Clustering de estilos de pitcheo
│
├── data/                              # Datos del proyecto
│   └── statcast_raw_data/            # Datos raw de Statcast por año
│       ├── statcast_2015.csv
│       ├── statcast_2016.csv
│       └── ... (hasta 2024)
│
├── src/                               # Código fuente reutilizable
│   ├── __init__.py
│   └── csv_manager.py                # Utilidades para manejo de CSVs
│
├── enunciado/                         # Documentación del enunciado
│
├── requirements.txt                   # Dependencias del proyecto
└── README.md                          # Este archivo
```

## 🚀 Instalación

### 1. Clonar el repositorio:
```bash
git clone https://github.com/iancotosoto/IA-Proyecto.git
cd IA-Proyecto
```

### 2. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 📊 Flujo de Trabajo

### 1️⃣ Descarga de Datos
El notebook `01_descarga_datos.ipynb` descarga datos de Statcast MLB desde 2015 hasta 2024:
- Utiliza la biblioteca `pybaseball` para acceder a datos oficiales
- Descarga paralela optimizada por año
- Almacenamiento en formato CSV para análisis posterior
- Sistema de caché para evitar descargas repetidas

### 2️⃣ Exploración Inicial
`02_exploracion_inicial.ipynb` realiza el primer análisis del dataset:
- Inspección de estructura y dimensiones
- Identificación de variables clave
- Análisis de valores nulos y outliers
- Visualizaciones exploratorias

### 3️⃣ Análisis Estadístico
`03_analisis_datos.ipynb` profundiza en el análisis:
- Análisis de calidad de datos y valores faltantes
- Estadísticas descriptivas por variable
- Análisis de correlaciones
- Visualizaciones de la zona de strike
- Distribuciones de tipos de lanzamiento
- Análisis de eventos y resultados

### 4️⃣ Predicción de Tipo de Lanzamiento
`04_prediccion_lanzamiento.ipynb` construye modelos para predecir el tipo de pitch:
- Selección y preprocesamiento de features
- Modelos base: Logistic Regression, Decision Trees, Random Forest
- Evaluación con métricas de clasificación
- Análisis de importancia de features

### 5️⃣ Predicción de Resultados
`05_prediccion_resultados.ipynb` predice eventos de bateo:
- Clasificación de eventos (hit, out, walk, strikeout, etc.)
- Modelos de clasificación multiclase
- Matriz de confusión y análisis de errores
- Evaluación de métricas por clase

### 6️⃣ Modelos Avanzados
`06_prediccion_avanzada.ipynb` implementa técnicas avanzadas:
- XGBoost y Gradient Boosting
- Optimización de hiperparámetros
- Validación cruzada
- Comparación de rendimiento entre modelos

### 7️⃣ Clustering de Estilos
`07_clustering_estilos.ipynb` agrupa estilos de pitcheo:
- K-Means clustering de perfiles de lanzadores
- Método del codo para selección de k
- Caracterización de clusters
- Visualización de perfiles de pitcheo

## 💻 Uso

### Inicio Rápido:
```bash
# Activar entorno virtual
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Iniciar Jupyter
jupyter notebook
```

### Orden recomendado de ejecución:
1. `01_descarga_datos.ipynb` - Descargar datos (opcional si ya tienes los datos)
2. `02_exploracion_inicial.ipynb` - Familiarizarse con los datos
3. `03_analisis_datos.ipynb` - Análisis detallado
4. `04_prediccion_lanzamiento.ipynb` - Primer modelo predictivo
5. `05_prediccion_resultados.ipynb` - Predicción de eventos
6. `06_prediccion_avanzada.ipynb` - Modelos optimizados
7. `07_clustering_estilos.ipynb` - Análisis de perfiles

## 📦 Dependencias Principales

- **Python 3.8+**
- **Análisis de datos:**
  - `numpy >= 1.24.0`
  - `pandas >= 2.0.0`
- **Visualización:**
  - `matplotlib >= 3.7.0`
  - `seaborn >= 0.12.0`
- **Machine Learning:**
  - `scikit-learn >= 1.3.0`
- **Jupyter:**
  - `jupyter >= 1.0.0`
  - `notebook >= 7.0.0`
- **Datos MLB:**
  - `pybaseball` - API para datos de béisbol
- **Utilidades:**
  - `tqdm >= 4.65.0`

Ver `requirements.txt` para la lista completa.

## 📈 Características del Dataset

Los datos de Statcast incluyen información detallada sobre cada lanzamiento:
- **Información del juego:** fecha, equipos, inning
- **Información del lanzador:** ID, nombre, mano dominante
- **Información del bateador:** ID, nombre, lado del bate
- **Características del lanzamiento:** tipo, velocidad, spin, ubicación
- **Resultado:** descripción del evento, resultado del at-bat
- **Datos de tracking:** ángulo de salida, velocidad de salida, distancia

**Volumen de datos:** ~700,000 lanzamientos por temporada × 10 años = ~7 millones de registros

## 🎯 Resultados Esperados

- Modelos de clasificación con accuracy > 70% en predicción de pitch type
- Identificación de factores clave que determinan el tipo de lanzamiento
- Perfiles de estilos de pitcheo mediante clustering
- Insights sobre patrones de comportamiento de lanzadores
- Predicción de probabilidades de eventos de bateo

## 🤝 Contribuciones

Este es un proyecto académico. Para sugerencias o mejoras:
1. Fork del repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto es parte de un trabajo académico para el curso de Inteligencia Artificial.

## 👥 Autor

Ian Cotosoto - [@iancotosoto](https://github.com/iancotosoto)

## 🙏 Agradecimientos

- **pybaseball** - Por proporcionar una excelente API para acceder a datos MLB
- **MLB Statcast** - Por hacer públicos los datos de tracking
- **Scikit-learn** - Por las herramientas de machine learning
- Comunidad de data science y baseball analytics

---

**Proyecto de IA - 2025** | MLB Pitch Analysis & Prediction

## Autor

[Tu nombre]

## Licencia

[Tipo de licencia]