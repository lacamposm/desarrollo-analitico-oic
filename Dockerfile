FROM lacamposm/docker-helpers:python-code

WORKDIR /workspaces/desarrollo-analitico

COPY requirements.txt requirements.txt

# Instalar dependencias con pip
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Puerto Streamlit
EXPOSE 8501

#  ------------  CASO USO IMAGEN CONDA  ------------ #
# FROM lacamposm/docker-helpers:python-conda

# WORKDIR /workspaces/desarrollo-analitico

# COPY environment.yml environment.yml

# # Crear el environment de Conda a partir del environment.yml
# RUN conda env create -f environment.yml

# # Usar el environment para los siguientes comandos
# SHELL ["conda", "run", "-n", "desarrollo-analitico", "/bin/bash", "-c"]

# # Puerto para Streamlit
# EXPOSE 8501