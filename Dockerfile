#  --------------  CASO USO Conda-VScode  -------------- #
FROM lacamposm/docker-helpers:conda-vscode

WORKDIR /desarrollo-analitico-oic

COPY environment.yml environment.yml

# Crear el environment de Conda a partir del environment.yml
RUN conda env create -f environment.yml

# Configurar la activación automática del entorno conda
RUN echo 'eval "$(conda shell.bash hook)"' >> ~/.bashrc && \
    echo 'conda activate desarrollo-analitico-oic' >> ~/.bashrc

# Puerto para VScode-server y Streamlit
EXPOSE 8080 8501

#  --------------  CASO USO Poetry-VScode  -------------- #
# FROM lacamposm/docker-helpers:python3.12-poetry-vscode

# WORKDIR /desarrollo-analitico-oic

# COPY requirements.txt requirements.txt

# # Instalar dependencias con pip
# RUN python -m pip install --upgrade pip
# RUN python -m pip install -r requirements.txt

# # Puerto para VScode-server y Streamlit
# EXPOSE 8501