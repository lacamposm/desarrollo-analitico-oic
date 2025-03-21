# ***🛠️ Clase 4: Implementación de un Proyecto Analítico Completo***

En esta clase desarrollaremos un proyecto analítico a menor escala, integrando un "modelo" de estimacion de precios de predios con una `API REST `utilizando `FastAPI`, almacenamiento en `PostgreSQL` y orquestación con `Docker`. Además, se incluirá una interfaz de usuario desarrollada en `Streamlit`. El objetivo es demostrar el flujo de trabajo end-to-end de una aplicación de datos moderna y sentar las bases para una estructura modular que permita futuras extensiones.

## Objetivos de la Sesión

- Implementar un "modelo" de estimacion de precios de predios.
- Crear una API REST con `FastAPI` para exponer el modelo como servicio.
- Configurar y utilizar `PostgreSQL` para almacenamiento persistente de datos y predicciones.
- Desplegar la solución completa con `Docker`, facilitando la integración de todos los componentes.
- Desarrollar una interfaz interactiva con `Streamlit` que permita la creación de usuarios y la realización de predicciones.

## Componentes del Proyecto

### 1. Modelo Analítico - Regresión Lineal

- Implementación simplificada utilizando scikit-learn.
- Entrenamiento con un subconjunto del dataset "House Prices" de Kaggle.
- Serialización del modelo para su uso en producción.
- **Nota:** Actualmente implementado como un modelo de "juguete" que devuelve números aleatorios.

### 2. API con FastAPI

- Diseño de endpoints para predicciones y usuarios.
- Validación de datos con Pydantic y documentación automática con Swagger UI.
- Manejo modular de la lógica a través de servicios y routers.

### 3. Base de Datos PostgreSQL

- Esquema básico para almacenar datos crudos y registros de predicción.
- Conexión mediante `SQLAlchemy` para gestionar la persistencia.

### 4. Orquestación con Docker

- `Dockerfile` para cada componente.
- `docker-compose.yml` para la integración de servicios (`API`, `PostgreSQL`, `Streamlit`).
- Configuración de variables de entorno y volúmenes para asegurar la correcta comunicación entre contenedores.

### 5. Interfaz de Usuario con Streamlit

- App interactiva para crear usuarios y realizar predicciones.
- Comunicación con la API para demostrar la integración end-to-end.

## Preparación del entorno y pruebas (60 min)

- Clonar el repositorio base.
- Verificar el funcionamiento inicial del sistema, incluyendo la prueba de la imagen Docker y la activación del servicio.
- Levantar los contenedores con docker-compose.


### Interacción con la API (30 min)

- Revisión de los endpoints implementados en FastAPI.
- Pruebas mediante Swagger UI y herramientas como `curl`.
- Implementación de nuevos endpoints (por ejemplo, estadísticas).

### Persistencia con PostgreSQL (25 min)

- Exploración del esquema de la base de datos.
- Consultas y gestión de registros usando `SQLAlchemy`.
- Análisis del flujo de datos desde la API hasta `PostgreSQL`.

*El resto de la sesión se dedicará a revisar y profundizar en el código, comprendiendo cada componente implementado.*

## Reflexión Final

Esta clase no solo muestra la implementación técnica de un proyecto analítico completo, sino que también sienta las bases para una estructura modular y escalable. La integración de estas piezas (modelo analítico, API, base de datos, Docker y Streamlit) permite desarrollar soluciones robustas que transforman datos en decisiones informadas.

> “El objetivo de un modelo no es ser perfecto, sino ser útil.”

---

## Recursos y referencias
- [Código completo del proyecto en GitHub](https://github.com/lacamposm/mini-proyecto-oic)
- [Documentación oficial de FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial de SQLAlchemy con PostgreSQL](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
- [Guía de despliegue con Docker Compose](https://docs.docker.com/compose/gettingstarted/)

## Para llevar más allá

- Implementar otros endpoints.