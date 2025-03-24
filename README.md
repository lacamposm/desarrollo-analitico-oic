# 📆 **Curso de inducción para el desarrollo analítico del OIC**

- **Docente:** [Luis Andrés Campos Maldonado](https://co.linkedin.com/in/lacamposm)
- **Correo:** [luisandres.campos@igac.gov.co](mailto:luisandres.campos@igac.gov.co)
- **Github:** [https://github.com/lacamposm]()

---

## 🛠️ Herramientas a instalar en el curso.

Para participar efectivamente en el curso, es necesario instalar las siguientes herramientas esenciales:

| Herramienta | ¿Desde qué clase se requiere? | Comentarios                                               |
|-------------|-------------------------------|-----------------------------------------------------------|
| **Git**     | ✅ Clase 1                    | Fundamental para control de versiones y trabajo colaborativo. |
| **Docker**  | ✅ Clase 2                    | Recomendado Docker Desktop, especialmente en Windows y MacOS. |

---

## 🛠️ **Herramientas principales del curso:**

- **[`Python`](https://www.python.org/):** Lenguaje principal para desarrollo analítico.
- **[`Git`](https://git-scm.com/book/ms/v2/Getting-Started-About-Version-Control) y [`GitHub`](https://github.com/)/[`GitLab:`](https://about.gitlab.com/)** Control de versiones y colaboración.
- **[`Docker`](https://www.docker.com/):** Contenedores y despliegue reproducible.
- **[`Docker-compose:`](https://docs.docker.com/compose/)** Orquestación y despliegue de servicios.
- **[`FastAPI`](https://fastapi.tiangolo.com/):** Desarrollo rápido y eficiente de APIs.
---

## 📌 **Clase 1 – Viernes, 7 de marzo de 2025**
**Introducción y Herramientas Colaborativas (Git y GitHub)**

En esta primera sesión conoceremos la estructura, objetivos y expectativas del curso. Exploraremos las herramientas clave que facilitarán nuestro trabajo durante todo el curso, enfocándonos especialmente en Git y GitHub. Realizaremos un ejercicio práctico para experimentar de primera mano la importancia del control de versiones y la colaboración efectiva en equipo.

- Presentación general del curso (objetivos y expectativas).
- Presentacion del calendario y contenidos del curso.
- Introducción práctica a Git y GitHub con ejercicio colaborativo.

---

## 📌 **Clase 2 – Martes, 11 de marzo de 2025**
**Python, Ambientes Virtuales y Docker**

En esta clase abordaremos `Python` como lenguaje fundamental para analítica de datos, con énfasis en la creación y gestión de ambientes virtuales. Exploraremos cómo Docker facilita la creación de entornos reproducibles y aprenderemos prácticas generales y recomendadas para desarrollar servicios analíticos.

- Introducción básica a Docker.
- Ambientes virtuales (`venv`, `conda`).
- Construccion de imagen Docker con kernel `Python` para usar con [`Vscode-server`](https://code.visualstudio.com/docs/remote/vscode-server)

---

## 📌 **Clase 3 – Viernes, 14 de marzo de 2025**
**Programación Orientada a Objetos y Documentación Profesional**

Esta sesión abordará los principios fundamentales de la programación orientada a objetos en Python, mostrando cómo estructurar eficientemente proyectos complejos mediante modularización. Además, se explicará cómo documentar código utilizando docstrings con [`Sphinx`](https://www.sphinx-doc.org/en/master/) para asegurar calidad profesional en los proyectos desarrollados.

- Conceptos clave de Programación Orientada a Objetos (OOP).
- Modularización y creación de paquetes reutilizables.
- Uso efectivo de docstrings para documentación del código.
- Generación profesional de documentación con Sphinx.

---

## 📌 **Clase 4 – Viernes, 21 de marzo de 2025**
**Implementación de un Proyecto Analítico Completo**

En esta clase desarrollaremos un proyecto analítico a menor escala, integrando un modelo de estimación de precios de predios con una API REST utilizando `FastAPI`, almacenamiento en `PostgreSQL` y orquestación con `Docker`. El objetivo es demostrar el flujo de trabajo end-to-end de una aplicación de datos moderna.

- Implementación dummy de estimación de precios de predios.
- Creación de una API REST con `FastAPI` para exponer el modelo como servicio.
- Configuración de `PostgreSQL` para almacenamiento persistente de datos y predicciones.
- Despliegue de la solución completa con `Docker` y `docker-compose`.

---

## 📌 **Clase 5 – Martes, 25 de marzo de 2025**
**Modelo Analítico con Regresión**

En esta clase profundizaremos en la construccion de nuestro servicio completo con `FastAPI`

- Implementando un modelo de regresion lineal multiple con `sklearn` sobre la informacion en la tabla [`raw_data`](https://raw.githubusercontent.com/lacamposm/Metodos-Estadisticos/refs/heads/main/data/kc_house_data.csv) de nuestra base de datos `PostgreSQL`.
- Introduccion a la libreria `GeoPandas` como facilitador para la manipulacion basica de informacion geografica.
- Exportaremos nuestro modelo a un formato facilmente consumible como el un `.pkl`.
- Implementacion de endpoint de prediccion con nuestro verdadero modelo.

---

## 📌 **Clase 6 – Viernes, 28 de marzo de 2025**
**Despliegue de Servicios Analíticos con Docker-compose y Streamlit**

En esta sesión final aprenderemos cómo desplegar de manera eficiente nuestros servicios analíticos en ambientes controlados usando `docker-compose`. También desarrollaremos un frontend interactivo usando `Streamlit` para consumir nuestras APIs, completando así el flujo completo desde la creación del modelo hasta su puesta en producción de forma integral.

- Despliegue del servicio analítico usando `docker-compose`.
- Creación de una aplicación web sencilla con `Streamlit`.
- Consumo del servicio analítico desde la aplicación web.

---

## ✅ **Objetivo final del curso:**  
Dotar a los participantes de habilidades prácticas, modernas y aplicables profesionalmente en entornos analíticos reales.

---

🚩 **Nota:**  
Se recomienda revisar constantemente los contenidos asignados de cada sesión para asegurar el máximo aprovechamiento de las sesiones prácticas.
