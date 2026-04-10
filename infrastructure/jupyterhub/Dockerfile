FROM quay.io/jupyterhub/jupyterhub:5.4.3

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install JupyterHub components and authentication
RUN pip install --no-cache-dir \
    jupyter_server \
    jupyterlab>=4.0.0 \
    jupyterhub-ldapauthenticator \
    dockerspawner

# Install core scientific computing packages (used in all 630 notebooks)
RUN pip install --no-cache-dir \
    numpy>=1.24.0 \
    pandas>=2.0.0 \
    matplotlib>=3.7.0 \
    seaborn>=0.12.0 \
    scipy>=1.10.0

# Install Jupyter notebook support
RUN pip install --no-cache-dir \
    ipykernel>=6.25.0 \
    ipywidgets>=8.0.0 \
    nbformat>=5.9.0 \
    nbconvert>=7.0.0

# Install optimization libraries (used in 48+ notebooks)
RUN pip install --no-cache-dir \
    pulp>=2.7.0

# Install machine learning packages (used in specific tiers)
RUN pip install --no-cache-dir \
    scikit-learn>=1.3.0 \
    torch>=2.0.0

# Install network and graph algorithms (used in 9+ notebooks)
RUN pip install --no-cache-dir \
    networkx>=3.1

# Install visualization enhancements
RUN pip install --no-cache-dir \
    plotly>=5.14.0

# Install utilities
RUN pip install --no-cache-dir \
    typing-extensions>=4.7.0 \
    joblib>=1.3.0 \
    tqdm>=4.65.0

# Set environment variables
ENV JUPYTER_ENABLE_LAB=yes
ENV PYTHONUNBUFFERED=1
