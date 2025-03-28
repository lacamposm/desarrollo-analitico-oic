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
     docker build -t python3.12 -f ./curso-introduccion/docker-files/Dockerfile.PythonMin .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12:latest
     ```

#### Windows

1. Construir la imagen de Docker:
     ```sh
     docker build -t python3.12 -f .\curso-introduccion\docker-files\Dockerfile.PythonMin .
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

## Dockerfile.CondaCode

Imagen completa basada en Miniconda con VS Code Server, pensada para entornos de desarrollo avanzados.

Esta imagen utiliza Miniconda como base para una gestión eficiente de paquetes, incluye VS Code Server para brindar una experiencia de desarrollo completa. Ideal para proyectos que requieren múltiples herramientas integradas.

```dockerfile
# Imagen base utilizando continuumio/miniconda3, con Conda preinstalado
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
    libnss3 \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://code-server.dev/install.sh | bash

# Verificar Node.js y npm
RUN node -v && npm -v

# Instalar extensiones de VS Code (code-server) para Python y Jupyter, junto con sus helpers y Git Graph
RUN code-server --install-extension ms-python.python \
    && code-server --install-extension ms-toolsai.jupyter \
    && code-server --install-extension ms-toolsai.jupyter-keymap \
    && code-server --install-extension ms-toolsai.jupyter-renderers \
    && code-server --install-extension mhutchie.git-graph

# Configurar tema oscuro por defecto en VS Code
RUN mkdir -p ~/.local/share/code-server/User && \
    echo '{"workbench.colorTheme": "Default Dark+", "jupyter.alwaysTrustNotebooks": true}' > ~/.local/share/code-server/User/settings.json

# Configuración de git
RUN git config --system core.sshCommand "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" \
    && git config --system --add safe.directory "*"

# Exponer puerto 8080 para code-server
EXPOSE 8080

# CMD para iniciar Vs-Code-Server
CMD ["/bin/bash", "-c", "source /etc/profile && source ~/.bashrc && \
    code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry & \
    exec bash"]
```

1. **FROM continuumio/miniconda3**  
   Usa la imagen oficial de Miniconda como base, que ya incluye Conda preinstalado.

2. **Instalar utilidades necesarias y Node.js**  
   Instala herramientas esenciales como Git, cURL, wget, así como Node.js para desarrollo web.

3. **Configuración de seguridad Git**  
   Configura Git para ignorar verificaciones de hosts SSH y marcar todos los directorios como seguros, evitando problemas de permisos.

4. **Instalar Code-Server (VS Code Server)**  
   Instala VS Code Server para desarrollo en navegador.

5. **Exponer puertos y definir CMD**  
   Expone el puerto 8080 (VS Code) e inicia el servicio.

### Ejecutar y Crear el Contenedor

Estando en la carpeta padre del proyecto:

#### Linux/MacOS

1. Construir la imagen de Docker:
     ```sh
     docker build -t conda-vscode -f ./curso-introduccion/docker-files/Dockerfile.CondaCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8080:8080 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") conda-vscode:latest
     ```

3. Visita VScode para desarrollar o Jupyterlab

     Luego visita para `VScode`:
     ```bash
     http://127.0.0.1:8080/?folder=/desarrollo-analitico-oic
     ```

#### Windows

1. Construir la imagen de Docker:
     ```powershell
     docker build -t conda-vscode -f .\curso-introduccion\docker-files\Dockerfile.CondaCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm `
     -p 8080:8080 `
     -v "${PWD}:/$(Split-Path -Leaf $PWD)" `
     -w "/$(Split-Path -Leaf $PWD)" `
     conda-vscode:latest
     ```

3. Visita VScode para desarrollar o Jupyterlab

     Luego visita:
     ```powershell
     http://127.0.0.1:8080/?folder=/desarrollo-analitico-oic
     ```

## Dockerfile.PoetryCode

Imagen ligera con Python 3.12 y VS Code Server, enfocada en proporcionar un entorno de desarrollo remoto a través del navegador.

```dockerfile
# Imagen base de Python 3.12
FROM python:3.12

# Instalar utilidades necesarias y Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    wget \
    sudo \
    ca-certificates \
    make \
    libnss3 \    
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL https://code-server.dev/install.sh | bash

# Verificar Node.js y npm
RUN node -v && npm -v

# Instalar paquetes Python necesarios para notebooks en VS-Code
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry

# Instalar extensiones de VS Code (code-server) para Python, Jupyter y Git Graph
RUN code-server --install-extension ms-python.python \
    && code-server --install-extension ms-toolsai.jupyter \
    && code-server --install-extension ms-toolsai.jupyter-keymap \
    && code-server --install-extension ms-toolsai.jupyter-renderers \
    && code-server --install-extension mhutchie.git-graph

# Configurar tema oscuro por defecto en VS Code
RUN mkdir -p ~/.local/share/code-server/User && \
    echo '{"workbench.colorTheme": "Default Dark+", "jupyter.alwaysTrustNotebooks": true}' > ~/.local/share/code-server/User/settings.json

# Configuración de git
RUN git config --system core.sshCommand "ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" \
    && git config --system --add safe.directory "*"

# Exponer puerto 8080 para code-server.
EXPOSE 8080

# 7. CMD para iniciar Code-Server y un servidor de notebooks en segundo plano
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
     docker build -t python3.12-poetry-vscode -f ./curso-introduccion/docker-files/Dockerfile.PoetryCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -p 8080:8080 -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python3.12-poetry-vscode
     ```

3. Acceder a VS Code Server:
     ```bash
     http://localhost:8080/?folder=/desarrollo-analitico-oic
     ```

#### Windows

1. Construir la imagen de Docker:
     ```powershell
     docker build -t python3.12-poetry-vscode -f .\curso-introduccion\docker-files\Dockerfile.PoetryCode .
     ```

2. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```powershell
     docker run -it --rm `
     -p 8080:8080 `
     -v "${PWD}:/$(Split-Path -Leaf $PWD)" `
     -w "/$(Split-Path -Leaf $PWD)" `
     python3.12-poetry-vscode
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
     Para CondaCode:
     ```sh
     docker tag conda-vscode tu-usuario-dockerhub/nombre-asignado:conda-vscode
     ```
     Para Poetry:
     ```sh
     docker tag python3.12-poetry-vscode tu-usuario-dockerhub/nombre-asignado:python3.12-poetry-vscode
     ```
3. Subir las imágenes a Docker Hub
   Una vez etiquetadas, puedes subirlas a Docker Hub:

     Para PythonMin:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12
     ```
     Para CondaCode:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:conda-vscode
     ```
     Para Poetry:
     ```sh
     docker push tu-usuario-dockerhub/nombre-asignado:python3.12-poetry-vscode
     ```
4. Descargar y utilizar imágenes desde Docker Hub
   Para descargar y usar una imagen publicada:

     ```sh
     docker pull tu-usuario-dockerhub/nombre-asignado:conda-vscode
     ```

     Para Linux:
     ```sh
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "$(pwd):/workspace" -w "/workspace" tu-usuario-dockerhub/nombre-asignado:conda-vscode
     ```

     Para Windows:
     ```powershell
     docker run -it --rm -p 8888:8888 -p 8080:8080 -v "${PWD}:/workspace" -w "/workspace" tu-usuario-dockerhub/nombre-asignado:conda-vscode
     ```

     Asegúrate de reemplazar `tu-usuario-dockerhub` con tu nombre de usuario en Docker Hub si estás subiendo tus propias imágenes.

5. Explicación de los parámetros
     - `-it`: Permite la interacción con el contenedor.
     - `--rm`: Elimina el contenedor al detenerse.
     - `-p 8888:8888`: Mapea el puerto 8888 para JupyterLab.
     - `-p 8080:8080`: Mapea el puerto 8080 para VS Code Server.
     - `-v "$(pwd):/workspace"`: Monta el directorio actual en el contenedor como `/workspace`.
     - `-w "/workspace"`: Define `/workspace` como el directorio de trabajo.

     -  Una vez ejecutado el contenedor, puedes acceder a:

          - JupyterLab: `http://localhost:8888`
          - VS Code Server: `http://localhost:8080`
