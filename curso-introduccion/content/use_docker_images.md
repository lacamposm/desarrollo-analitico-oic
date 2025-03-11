# Desglose Dockerfile.


## Dockerfile.PythonMin

```dockerfile
FROM python:3.12

CMD ["/bin/bash"]
```


 Arranca el contenedor con la shell bash.

## Ejecutar y Crear el Contenedor

### Linux/MacOS

1. Navegar al directorio del proyecto:
     ```sh
     cd /ruta/al/proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t python-min -f Dockerfile.PythonMin .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -it --rm -v "$(pwd)":/$(basename "$(pwd)") -w /$(basename "$(pwd)") python-min:latest
     ```

### Windows

1. Navegar al directorio del proyecto:
     ```sh
     cd \ruta\al\proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t mi-python-min -f Dockerfile.PythonMin .
     ```
3. Ejecutar el contenedor montando la carpeta actual como volumen:

     ```powershell
     docker run -it --rm -v "${PWD}:/$(Split-Path -Leaf $PWD)" -w "/$(Split-Path -Leaf $PWD)" python-min:latest
     ```

     O en una línea más legible usando el caracter de continuación ` :
     ```powershell
     docker run -it --rm `
          -v "${PWD}:/$(Split-Path -Leaf $PWD)" `
          -w "/$(Split-Path -Leaf $PWD)" `
          python-min:latest
     ```

# Explicación línea a línea de Dockerfile.PythonJupyterlab

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

## Ejecutar y Crear el Contenedor

### Linux/MacOS

1. Navegar al directorio del proyecto:
     ```sh
     cd /ruta/al/proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t mi-python-jupyterlab -f Dockerfile.PythonJupyterlab .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -d -p 8888:8888 -v $(pwd):/app mi-python-jupyterlab
     ```

4. Abrir terminal del contenedor:
     ```sh
     docker exec -it $(docker ps -q --filter ancestor=mi-python-jupyterlab) bash
     ```

### Windows

1. Navegar al directorio del proyecto:
     ```sh
     cd \ruta\al\proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t mi-python-jupyterlab -f Dockerfile.PythonJupyterlab .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -d -p 8888:8888 -v %cd%:/app mi-python-jupyterlab
     ```

4. Abrir terminal del contenedor:
     ```sh
     docker exec -it $(docker ps -q --filter ancestor=mi-python-jupyterlab) bash
     ```

# Explicación línea a línea del Dockerfile.PythonFull

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

## Ejecutar y Crear el Contenedor

### Linux/MacOS

1. Navegar al directorio del proyecto:
     ```sh
     cd /ruta/al/proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t mi-python-full -f Dockerfile.PythonFull .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -d -p 8888:8888 -p 8080:8080 -v $(pwd):/app mi-python-full
     ```

4. Abrir terminal del contenedor:
     ```sh
     docker exec -it $(docker ps -q --filter ancestor=mi-python-full) bash
     ```

### Windows

1. Navegar al directorio del proyecto:
     ```sh
     cd \ruta\al\proyecto
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t mi-python-full -f Dockerfile.PythonFull .
     ```

3. Ejecutar el contenedor montando la carpeta actual como volumen:
     ```sh
     docker run -d -p 8888:8888 -p 8080:8080 -v %cd%:/app mi-python-full
     ```

4. Abrir terminal del contenedor:
     ```sh
     docker exec -it $(docker ps -q --filter ancestor=mi-python-full) bash
     ```

## Publicar la Imagen en Docker Hub

Para publicar la imagen `PythonFull` en Docker Hub, sigue estos pasos:

1. Inicia sesión en Docker Hub:
     ```sh
     docker login
     ```

2. Construir la imagen de Docker:
     ```sh
     docker build -t tu-usuario-dockerhub/mi-python-full:latest -f Dockerfile.PythonFull .
     ```

3. Etiqueta la imagen (si no lo hiciste en el paso anterior):
     ```sh
     docker tag mi-python-full tu-usuario-dockerhub/mi-python-full:latest
     ```

4. Publica la imagen en Docker Hub:
     ```sh
     docker push tu-usuario-dockerhub/mi-python-full:latest
     ```

Asegúrate de reemplazar `tu-usuario-dockerhub` con tu nombre de usuario en Docker Hub.
