# ***🛠️ Clase 4: Implementación de un Proyecto Analítico Completo***

En esta clase desarrollaremos un proyecto analítico a menor escala, integrando un "modelo" de estimacion de precios de predios con una `API REST` utilizando `FastAPI`, almacenamiento en `PostgreSQL` y orquestación con `Docker`. Además, se incluirá una interfaz de usuario desarrollada en `Streamlit`. El objetivo es demostrar el flujo de trabajo end-to-end de una aplicación de datos moderna y sentar las bases para una estructura modular que permita futuras extensiones.

## Objetivos de la Sesión

- Implementar un "modelo" de estimacion de precios de predios.
- Crear una API REST con `FastAPI` para exponer el modelo como servicio.
- Configurar y utilizar `PostgreSQL` para almacenamiento persistente de datos y predicciones.
- Desplegar la solución completa con `Docker`, facilitando la integración de todos los componentes.
- Desarrollar una interfaz interactiva con `Streamlit` que permita la creación de usuarios y la realización de predicciones.

## Componentes del Proyecto

### 1. "Modelo" Analítico.

- Actualmente implementado como un modelo de "juguete" que devuelve números aleatorios.

### 2. API con FastAPI

- Diseño de endpoints para predicciones y usuarios.
- Manejo modular de la lógica a través de servicios y routers.
- Validación de datos con `Pydantic` y documentación automática con Swagger UI.


### 3. Base de Datos PostgreSQL

- Esquema básico para almacenar datos crudos y registros de predicción.
- Conexión mediante `sqlmodel` y `psycopg2`  para gestionar la persistencia.

### 4. Orquestación con Docker

- `Dockerfile` para cada componente.
- `docker-compose.yml` para la integración de servicios (`API`, `PostgreSQL`, `Streamlit`).
- Configuración de variables de entorno y volúmenes para asegurar la correcta comunicación entre contenedores.

### 5. Interfaz de Usuario con Streamlit

- App interactiva para crear usuarios y realizar predicciones.
- Comunicación con la API para demostrar la integración end-to-end.

---

### Preparación del entorno y pruebas (35 min)

- Clonar el repositorio base.
- Verificar el funcionamiento inicial del sistema, incluyendo la construccion y prueba de la imagen Docker.
- Explorar la estructura de carpetas y archivos para familiarizarnos con la organización del proyecto.

### Interacción con la API (60 min)

- Revision del codigo y su funcionamiento e implementacion, centrandonos en `FastAPI` y `sqlmodel`, comprendiendo cada componente implementado.
- Revisión de los endpoints implementados en `FastAPI`.
- Levantar los contenedores con `docker-compose`.
- Comprobación de la correcta inicialización de `PostgreSQL`, `API` y `Streamlit`
- Pruebas mediante Swagger UI y herramientas como `curl`.


### Persistencia con PostgreSQL (20 min)

- Exploración del esquema de la base de datos.
- Consultas y gestión de registros usando `pandas` y `SQLAlchemy`.

## Reflexión Final

Esta clase no solo muestra la implementación técnica de un proyecto analítico completo, sino que también sienta las bases para una estructura modular y escalable. La integración de estas piezas (`"modelo" analítico`, `API`, `database`, `Docker` y `UI`) permite desarrollar soluciones robustas que transforman datos en decisiones informadas.

---

### Recursos y Referencias

- **FastAPI:** [Documentación de FastAPI](https://fastapi.tiangolo.com/)

- **PostgreSQL:** [Documentación de PostgreSQL](https://www.postgresql.org/docs/)

- **psycopg2:** [Documentación de psycopg2](https://www.psycopg.org/docs/)

- **Docker:** [Sitio oficial de Docker](https://www.docker.com/)

- **Docker Compose:** [Guía de Docker Compose](https://docs.docker.com/compose/gettingstarted/)

- **Streamlit:**  [Documentación de Streamlit](https://docs.streamlit.io/)

- **SQLAlchemy:** [Tutorial de SQLAlchemy con PostgreSQL](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)

- **SQLModel:** [Documentación de SQLModel](https://sqlmodel.tiangolo.com/)

- **Código completo en GitHub:**  [GitHub - mini-proyecto-oic](https://github.com/lacamposm/mini-proyecto-oic)

## Para llevar más allá

- Piensa en implementar otros endpoints.