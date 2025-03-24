# ***🛠️Clase 5: Endpoints - Modelo de Regresión Multiple***


En la sesión de hoy, aprovecharemos que ya contamos con un template base de `FastAPI` para centrarnos en la construcción e integración de nuestro modelo. El flujo de la clase se divide en dos etapas principales: primero, la construcción del modelo, y segundo, la implementación del servicio con sus endpoints correspondientes.

---

## Objetivos de la Sesión

### 1. Construcción del Modelo

Vamos a construir un modelo de regresión lineal múltiple utilizando `sklearn`, donde el énfasis no recae en la complejidad del algoritmo, sino en comprender cómo integrar un modelo analítico en un servicio completo.


1. **Introducción a GeoPandas:**  
  Se explicará el uso de la librería `GeoPandas` para la manipulación de información geográfica. Esta herramienta puede enriquecer el análisis de datos al permitir trabajar con datos espaciales, facilitando operaciones básicas como la carga y transformación de archivos geográficos.

2. **Entrenamiento del Modelo con sklearn:**  
  Se utilizará la libreria `sklearn` para entrenar un modelo de regresión lineal múltiple. Durante este proceso se hará énfasis en la selección de variables predictoras y en el entrenamiento básico, manteniendo el foco en la integración más que en la optimización del algoritmo.

3. **Exportación del Modelo:**  
  Una vez entrenado, el modelo se exportará a un archivo con formato `.pkl`. Esta exportación es clave para facilitar el despliegue del modelo en otros entornos o servicios, permitiendo su reutilización sin necesidad de reentrenarlo.

---

### 2. Implementación del Servicio con FastAPI

 
Integraremos el modelo exportado en el servicio utilizando el template de `FastAPI`, definiendo los endpoints que permitirán la interacción con el modelo y el manejo de la información geográfica.

1. **Integración del Modelo en FastAPI:**  
  Se cargará el modelo previamente exportado en el template existente, asegurando que esté listo para responder a las peticiones de predicción.

2. **Desarrollo de Endpoints de Predicción:**  
  
  Permite enviar datos y obtener la predicción generada por el modelo.


---

## Reflexión Final

El enfoque de la clase está en entender que, aunque el modelo de regresión lineal múltiple es una parte central del análisis, el verdadero valor de esta sesion reside en la **construcción de un servicio completo** que integra:

1. **Construcción del Modelo:**  
   - Entrenamiento básico del modelo con `sklearn`.
   - Exportación del modelo a formato `.pkl`.

2. **Implementación del Servicio:**  
   - Integración del modelo en el template de `FastAPI`.
   - Creación de endpoints funcionales para interactuar con el modelo.

Este flujo permite comprender la importancia de una arquitectura de servicio sólida y escalable, donde la integración de componentes diversos (modelo analítico, y servicios web) es lo que se busca resaltar del sistema completo.

---

## Recursos y referencias

- **scikit-learn:** [Documentación de scikit-learn](https://scikit-learn.org/stable/)
- **GeoPandas:** [Documentación de GeoPandas](https://geopandas.org/)
- **FastAPI:** [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- **Pandas:**  [Documentación de Pandas](https://pandas.pydata.org/docs/)
