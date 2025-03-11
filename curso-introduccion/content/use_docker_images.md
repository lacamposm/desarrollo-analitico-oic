# ***Construyendo y corriendo imagenes Docker en local.***


## Dockerfile.PythonMin

Imagen mínima de Python 3.12 para entornos ligeros sin paquetes adicionales.
Esta imagen se utiliza cuando se requiere un entorno base de Python sin dependencias extras, ideal para ejecutar scripts o aplicaciones simples de manera eficiente sin sobrecargar el contenedor.

```dockerfile
FROM python:3.12

CMD ["/bin/bash"]
```

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS


1. Construir la imagen de Docker:

     ```bash
     docker build -t python3.12 -f ./curso-introduccion/docker-images/Dockerfile.PythonMin .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python-min:latest
     ```

#### Windows

1. Construir la imagen de Docker:
     ```cmd
     docker build -t python3.12 -f .\curso-introduccion\docker-images\Dockerfile.PythonMin .
     ```
3. Ejecutar el contenedor montando la carpeta actual como volumen:

     ```powershell
     docker run -it --rm -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python3.12:latest
     ```

     O en una línea más legible usando el caracter de continuación ` :
     ```powershell
     docker run -it --rm `
          -v "${PWD}:/$(Split-Path -Leaf $PWD)" `
          -w "/$(Split-Path -Leaf $PWD)" `
          python3.12:latest
     ```

## Dockerfile.PythonJupyterlab

Esta imagen instala JupyterLab junto a la extensión jupyterlab-git, facilitando la integración con repositorios Git. Es perfecta para desarrolladores y científicos de datos que necesiten un entorno robusto y flexible para trabajar de forma interactiva con notebooks y gestionar versiones de código.

```dockerfile
FROM python:3.12

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN node -v && npm -v

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir jupyterlab jupyterlab-git \
    && jupyter server extension enable jupyterlab_git \
    && jupyter lab build --dev-build=False --minimize=False

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888",\
     "--no-browser", "--allow-root", "--NotebookApp.token=''",\
     "--NotebookApp.password=''", "--NotebookApp.disable_check_xsrf=True"]
```

1. **FROM python:3.12**  
    Utiliza la imagen oficial de Python 3.12 como base.

2. **RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - (...)** 
    Agrega el repositorio oficial de Node.js versión 20, actualiza los paquetes e instala Node.js.

3. **RUN node -v && npm -v**  
    Verifica que Node.js y npm estén instalados correctamente comprobando sus versiones.

4. **RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir jupyterlab jupyterlab-git (...)**  
    Actualiza pip e instala JupyterLab y la extensión jupyterlab-git para gestionar repositorios Git desde la interfaz de JupyterLab.

5. **EXPOSE 8888**  
    Expone el puerto 8888 para acceder a JupyterLab.

6. **CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]**  
     Inicia JupyterLab en la dirección IP 0.0.0.0 y el puerto 8888, sin requerir autenticación.

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS

1. Construir la imagen de Docker:
     ```sh
     docker build --no-cache -t python3.12-jupyterlab -f ./curso-introduccion/docker-images/Dockerfile.PythonJupyterlab .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8888:8888 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12-jupyterlab
     ```


#### Windows

1. Construir la imagen de Docker:
     ```cmd
     docker build --no-cache -t python3.12-jupyterlab -f .\curso-introduccion\docker-images\Dockerfile.PythonJupyterlab .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm -p 8888:8888 -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python3.12-jupyterlab
     ```

     O en una línea más legible usando el caracter de continuación ` :
     ```powershell
     docker run -it --rm `
          -p 8888:8888 `
          -v "${PWD}:/$(Split-Path -Leaf $PWD)" `
          -w "/$(Split-Path -Leaf $PWD)" `
          python3.12-jupyterlab
     ```

## Dockerfile.PythonFull

Imagen completa basada en Python 3.12 con Miniconda, JupyterLab y VS Code Server, pensada para entornos de desarrollo avanzados.

Esta imagen integra Miniconda para una gestión eficiente de paquetes, JupyterLab para la edición y ejecución de notebooks y VS Code Server para brindar una experiencia de desarrollo en la nube similar a un IDE moderno. Es ideal para proyectos complejos que requieren múltiples herramientas de desarrollo integradas en un solo contenedor.

```dockerfile
FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    wget \
    sudo \
    ca-certificates \
    libnss3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR="/opt/conda"
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh \
    && /bin/bash /tmp/miniconda.sh -b -p $CONDA_DIR \
    && rm /tmp/miniconda.sh

ENV PATH="$CONDA_DIR/bin:$PATH"
RUN echo 'export PATH="$CONDA_DIR/bin:$PATH"' >> /etc/profile \
    && echo 'export PATH="$CONDA_DIR/bin:$PATH"' >> ~/.bashrc \
    && echo 'export PATH="$CONDA_DIR/bin:$PATH"' >> ~/.bash_profile

RUN conda update -n base -c defaults conda -y

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry jupyterlab ipykernel

RUN curl -fsSL https://code-server.dev/install.sh | bash

EXPOSE 8888 8080

CMD ["/bin/bash", "-c", "source /etc/profile && source ~/.bashrc && \
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root \
    --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.disable_check_xsrf=True & \
    code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry & \
    exec bash"]
```

1. **FROM python:3.12**  
    Selecciona como base la imagen oficial de Python en su versión 3.12.

2. **RUN apt-get update && apt-get install -y --no-install-recommends (...)**  
    Actualiza los índices de paquetes e instala herramientas básicas (bash, curl, git, etc.) sin incluir paquetes innecesarios.

3. **ENV CONDA_DIR="/opt/conda"**  
    Define la variable CONDA_DIR para indicar la ubicación donde se instalará Miniconda.

4. **RUN wget --quiet (...) && /bin/bash /tmp/miniconda.sh -b -p $CONDA_DIR && rm /tmp/miniconda.sh**  
    Descarga silenciosamente el instalador de Miniconda, lo ejecuta y luego elimina el instalador.

5. **ENV PATH="$CONDA_DIR/bin:$PATH"**  
    Añade la ruta de Miniconda al PATH para que los comandos de conda estén disponibles.

6. **RUN echo 'export PATH="$CONDA_DIR/bin:$PATH"' >> /etc/profile (...)**  
    Actualiza archivos de configuración para incluir conda en el PATH en todas las sesiones.

7. **RUN conda update -n base -c defaults conda -y**  
    Actualiza conda para asegurarse de que esté en su última versión.

8. **RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir poetry jupyterlab ipykernel**  
    Actualiza pip e instala paquetes de Python (Poetry, JupyterLab, ipykernel).

9. **RUN curl -fsSL https://code-server.dev/install.sh | bash**  
    Descarga e instala code-server (VS Code Server).

10. **EXPOSE 8888 8080**  
     Declara los puertos que se expondrán: 8888 (JupyterLab) y 8080 (code-server).

11. **CMD ["/bin/bash", "-c", "source /etc/profile && source ~/.bashrc && (...) exec bash"]**  
     Define el comando que se ejecuta al iniciar el contenedor, iniciando JupyterLab y code-server, y dejando la terminal activa.

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS

1. Construir la imagen de Docker:
     ```sh
     docker build -t python3.12-full -f ./curso-introduccion/docker-images/Dockerfile.PythonFull .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12-full:latest
     ```

3. Visita VScode para desarrollar o Jupyterlab

     Luego visita para `VScode`:
     ```bash
     http://0.0.0.0:8080/?folder=/desarrollo-analitico-oic
     ```

     Y para `Jupyterlab`:

     ```bash
     http://127.0.0.1/8888/lab
     ```

#### Windows

1. Construir la imagen de Docker:
     ```cmd
     docker build -t python3.12-full -f .\curso-introduccion\docker-images\Dockerfile.PythonFull .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python3.12-full:latest
     ```

3. Visita VScode para desarrollar o Jupyterlab

     Luego visita:
     ```powershell
     http://0.0.0.0:8080/?folder=/desarrollo-analitico-oic
     ```

     Y para `Jupyterlab`:

     ```powershell
     http://127.0.0.1:8888/lab
     ```

## Publicar la Imagen en Docker Hub

Para publicar las imágenes en Docker Hub, sigue estos pasos:

1. Inicia sesión en Docker Hub:
     ```sh
     docker login
     ```
     Ingresa tu nombre de usuario y contraseña cuando se solicite.

2. Etiquetar las imágenes
   Para subir una imagen a tu repositorio en Docker Hub, primero debes etiquetarla con tu nombre de usuario:

     Para PythonMin:
     ```sh
     docker tag python3.12 tu-usuario-dockerhub/nombre-asignado:python3.12
     ```
     Para PythonJupyterlab:
     ```sh
     docker tag python3.12-jupyterlab tu-usuario-dockerhub/nombre-asignado:python3.12-jupyterlab
     ```
     Para PythonFull:
     ```sh
     docker tag python3.12-full tu-usuario-dockerhub/nombre-asignado:python3.12-full
     ```
3. Subir las imágenes a Docker Hub
   Una vez etiquetadas, puedes subirlas a Docker Hub:

     Para PythonMin:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado/python3.12:latest
     ```
     Para PythonJupyterlab:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado/pythonjupyterlab:latest
     ```
     Para PythonFull:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado/pythonfull:latest
     ```
4. Descargar y utilizar imágenes desde Docker Hub
   Para descargar y usar una imagen publicada:

     ```sh
     docker pull tu-usuario-dockerhub/nombre-asignado/pythonfull:latest
     ```

     Para Linux:
     ```sh
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "$(pwd):/workspace" -w "/workspace" tu-usuario-dockerhub/pythonfull:latest
     ```

     Para Windows:
     ```powershell
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "${PWD}:/workspace" -w "/workspace" tu-usuario-dockerhub/pythonfull:latest
     ```
5. Explicación de los parámetros
- `-it`: Permite la interacción con el contenedor.
- `--rm`: Elimina el contenedor al detenerse.
- `-p 8888:8888`: Mapea el puerto 8888 para JupyterLab.
- `-p 8080:8080`: Mapea el puerto 8080 para VS Code Server.
- `-v "$(pwd):/workspace"`: Monta el directorio actual en el contenedor como `/workspace`.
- `-w "/workspace"`: Define `/workspace` como el directorio de trabajo.
   Una vez ejecutado el contenedor, puedes acceder a:

   - JupyterLab: `http://localhost:8888`
   - VS Code Server: `http://localhost:8080`

Asegúrate de reemplazar `tu-usuario-dockerhub` con tu nombre de usuario en Docker Hub si estás subiendo tus propias imágenes.