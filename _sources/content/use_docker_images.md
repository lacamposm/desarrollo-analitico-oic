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
     ```sh
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

# Instalar Node.js 20+ y dependencias Git
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends \
    nodejs \
    git \
    git-lfs \
    openssh-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Verificar Node.js y npm
RUN node -v && npm -v

# Actualizar pip e instalar JupyterLab + Extensión Git
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir jupyterlab jupyterlab-git==0.41.0 \
    && jupyter server extension enable --py jupyterlab_git \
    && jupyter lab build --dev-build=False --minimize=False

# Configuración de git para JupyterLab
RUN git config --system core.sshCommand "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" \
    && git config --system --add safe.directory "*" \
    && mkdir -p ~/.ssh && chmod 700 ~/.ssh \
    && ssh-keyscan github.com >> ~/.ssh/known_hosts 2>/dev/null

# Exponer el puerto de JupyterLab
EXPOSE 8888

# Comando para iniciar JupyterLab sin autenticación
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.disable_check_xsrf=True"]
```

1. **RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - (...)** 
   Agrega el repositorio oficial de Node.js versión 20, actualiza los paquetes e instala Node.js junto con herramientas Git.
2. **RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir jupyterlab jupyterlab-git==0.41.0 (...)**  
   Actualiza pip e instala JupyterLab y la extensión jupyterlab-git específicamente en la versión 0.41.0.

5. **Configuración de git para JupyterLab**  
   Configura Git para trabajar de manera integrada con JupyterLab, incluyendo manejo seguro de repositorios.

6. **EXPOSE 8888**  
   Expone el puerto 8888 para acceder a JupyterLab.

7. **CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]**  
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
     ```powershell
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

## Dockerfile.PythonConda

Imagen completa basada en Miniconda con JupyterLab y VS Code Server, pensada para entornos de desarrollo avanzados.

Esta imagen utiliza Miniconda como base para una gestión eficiente de paquetes, incluye JupyterLab para notebooks y VS Code Server para brindar una experiencia de desarrollo completa. Ideal para proyectos que requieren múltiples herramientas integradas.

```dockerfile
FROM continuumio/miniconda3

# Instalar utilidades necesarias y Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    wget \
    sudo \
    ca-certificates \
    make \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Verificar Node.js y npm
RUN node -v && npm -v

# Actualizar conda y configurar canales
RUN conda update -n base -c defaults conda -y && \
    conda config --add channels conda-forge

# Instalar paquetes Python esenciales con conda
RUN conda install -y \
    jupyterlab \
    ipykernel \
    && conda clean -afy \
    && pip install --no-cache-dir jupyterlab-git \
    && jupyter server extension enable jupyterlab_git \
    && jupyter lab build --dev-build=False --minimize=False

# Configuración de git para JupyterLab
RUN git config --system core.sshCommand "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" \
    && git config --system --add safe.directory "*"

# Instalar Code-Server (VS Code Server)
RUN curl -fsSL https://code-server.dev/install.sh | bash

# Exponer puertos
EXPOSE 8888 8080

# CMD para iniciar JupyterLab y Code-Server
CMD ["/bin/bash", "-c", "source /etc/profile && source ~/.bashrc && \
    jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root \
    --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.disable_check_xsrf=True & \
    code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry & \
    exec bash"]
```

1. **FROM continuumio/miniconda3**  
   Usa la imagen oficial de Miniconda como base, que ya incluye Conda preinstalado.

2. **Instalar utilidades necesarias y Node.js**  
   Instala herramientas esenciales como Git, cURL, wget, así como Node.js para desarrollo web.

3. **Configuración de git para JupyterLab**  
   Establece configuraciones de Git para trabajar correctamente con JupyterLab.

6. **Instalar Code-Server (VS Code Server)**  
   Instala VS Code Server para desarrollo en navegador.

7. **Exponer puertos y definir CMD**  
   Expone los puertos 8888 (JupyterLab) y 8080 (VS Code) e inicia ambos servicios.

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS

1. Construir la imagen de Docker:
     ```sh
     docker build -t python3.12-conda -f ./curso-introduccion/docker-images/Dockerfile.PythonConda .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12-conda:latest
     ```

3. Visita VScode para desarrollar o Jupyterlab

     Luego visita para `VScode`:
     ```bash
     http://0.0.0.0:8080/?folder=/desarrollo-analitico-oic
     ```

     Y para `Jupyterlab`:

     ```bash
     http://127.0.0.1:8888/lab
     ```

#### Windows

1. Construir la imagen de Docker:
     ```powershell
     docker build -t python3.12-conda -f .\curso-introduccion\docker-images\Dockerfile.PythonConda .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python3.12-conda:latest
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

## Dockerfile.PythonCode

Imagen ligera con Python 3.12 y VS Code Server, enfocada en proporcionar un entorno de desarrollo remoto a través del navegador.

```dockerfile
FROM python:3.12
 
# Instalar utilidades necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    wget \
    sudo \
    ca-certificates \
    libnss3 \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
 
# Instalar paquetes Python necesarios para notebooks en VS-Code
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry ipykernel jupyter_client ipython
 
# Instalar Code-Server (VS Code Server)
RUN curl -fsSL https://code-server.dev/install.sh | bash

# Instalar extensiones de VS-Code para notebooks
RUN code-server --install-extension ms-toolsai.jupyter

# Exponer solo el puerto para VS Code
EXPOSE 8080
 
# CMD para iniciar solo Code-Server
CMD ["/bin/bash", "-c", "source /etc/profile && source ~/.bashrc && \
    code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry & \
    exec bash"]
```

1. **Instalar utilidades necesarias**  
   Instala herramientas básicas de desarrollo y sistema.

3. **Instalar paquetes Python para notebooks**  
   Configura los paquetes mínimos necesarios para trabajar con notebooks en VS Code.

4. **Instalar Code-Server y extensión Jupyter**  
   Instala VS Code Server y la extensión para trabajar con notebooks Jupyter.

5. **CMD para iniciar Code-Server**  
   Inicia VS Code Server en el puerto 8080 sin autenticación.

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS

1. Construir la imagen de Docker:
     ```sh
     docker build -t python3.12-code -f ./curso-introduccion/docker-images/Dockerfile.PythonCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8080:8080 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12-code:latest
     ```

3. Acceder a VS Code Server:
     ```bash
     http://localhost:8080/?folder=/desarrollo-analitico-oic
     ```

#### Windows

1. Construir la imagen de Docker:
     ```powershell
     docker build -t python3.12-code -f .\curso-introduccion\docker-images\Dockerfile.PythonCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm -p 8080:8080 -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python3.12-code:latest
     ```

3. Acceder a VS Code Server:
     ```powershell
     http://localhost:8080/?folder=/desarrollo-analitico-oic
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
     Para PythonConda:
     ```sh
     docker tag python3.12-conda tu-usuario-dockerhub/nombre-asignado:python3.12-conda
     ```
     Para PythonCode:
     ```sh
     docker tag python3.12-code tu-usuario-dockerhub/nombre-asignado:python3.12-code
     ```
3. Subir las imágenes a Docker Hub
   Una vez etiquetadas, puedes subirlas a Docker Hub:

     Para PythonMin:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12
     ```
     Para PythonJupyterlab:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12-jupyterlab
     ```
     Para PythonConda:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12-conda
     ```
     Para PythonCode:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12-code
     ```
4. Descargar y utilizar imágenes desde Docker Hub
   Para descargar y usar una imagen publicada:

     ```sh
     docker pull tu-usuario-dockerhub/nombre-asignado:python3.12-conda
     ```

     Para Linux:
     ```sh
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "$(pwd):/workspace" -w "/workspace" tu-usuario-dockerhub/nombre-asignado:python3.12-conda
     ```

     Para Windows:
     ```powershell
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "${PWD}:/workspace" -w "/workspace" tu-usuario-dockerhub/nombre-asignado:python3.12-conda
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