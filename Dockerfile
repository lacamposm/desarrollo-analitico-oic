FROM lacamposm/docker-helpers:python3.12-notebooks-code-server

WORKDIR /desarrollo-analitico-oic

COPY requirements.txt requirements.txt

# Instalar dependencias con pip
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Puerto Streamlit
EXPOSE 8501

#  ------------  CASO USO IMAGEN CONDA  ------------ #
# FROM lacamposm/docker-helpers:python-conda-notebooks-code-server

# WORKDIR /desarrollo-analitico-oic

# COPY environment.yml environment.yml

# # Crear el environment de Conda a partir del environment.yml
# RUN conda env create -f environment.yml

# # Usar el environment para los siguientes comandos
# SHELL ["conda", "run", "-n", "desarrollo-analitico-oic", "/bin/bash", "-c"]

# # Instalar el paquete notebook, que provee el comando jupyter-notebook
# RUN pip install notebook

# # Configurar la activación automática del entorno conda
# RUN echo 'eval "$(conda shell.bash hook)"' >> ~/.bashrc && \
#     echo 'conda activate desarrollo-analitico-oic' >> ~/.bashrc

# # Puerto para Streamlit
# EXPOSE 8501