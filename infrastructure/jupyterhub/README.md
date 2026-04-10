# JupyterHub (Docker) — Setup and Run

This folder contains a complete, reproducible setup to run **JupyterHub in Docker** with all dependencies for the **630 executed notebooks** in this repository.

## What's Included

The provided `Dockerfile` extends the official JupyterHub image and installs all packages needed for running the notebooks:

### JupyterHub Components
- `jupyterlab>=4.0.0` - Modern notebook interface
- `jupyter_server` - Jupyter server backend
- `jupyterhub-ldapauthenticator` - LDAP authentication support
- `dockerspawner` - Docker-based user spawning

### Core Scientific Computing (Used in all 630 notebooks)
- `numpy>=1.24.0` - Numerical computing
- `pandas>=2.0.0` - Data manipulation (522 notebooks)
- `matplotlib>=3.7.0` - Plotting and visualization
- `seaborn>=0.12.0` - Statistical visualization (567 notebooks)
- `scipy>=1.10.0` - Scientific computing (65 notebooks)

### Optimization & Operations Research (48 notebooks)
- `pulp>=2.7.0` - Linear/integer programming

### Machine Learning (11 notebooks)
- `scikit-learn>=1.3.0` - Machine learning algorithms
- `torch>=2.0.0` - Deep learning framework

### Network & Graph Algorithms (9 notebooks)
- `networkx>=3.1` - Graph theory and network analysis

### Visualization & Utilities
- `plotly>=5.14.0` - Interactive visualizations
- `ipywidgets>=8.0.0` - Interactive widgets
- `tqdm>=4.65.0` - Progress bars
- `joblib>=1.3.0` - Parallel processing

This is intentional: in a classroom or multi-user setting, it is better to **bake all dependencies into the Docker image** so that all 630 notebooks run with `Run All` without per-notebook package installation.

## Prerequisites

- Docker Desktop (Windows / macOS / Linux)

## Quick start (build + run)

By default, this setup is intended for quick local testing.

The flag below is **NOT for production**:

- `--Authenticator.allow_all=True`

It accepts any username.

### Build

```bash
docker build -t my-jupyterhub .
```

If you change Python dependencies in the `Dockerfile`, rebuild the image so the environment stays consistent.

### Run

#### Windows PowerShell

```powershell
docker rm -f jupyterhub

docker run -d --name jupyterhub `
  -p 8000:8000 `
  my-jupyterhub `
  jupyterhub --Authenticator.allow_all=True
```

#### Bash (Linux/macOS)

```bash
docker rm -f jupyterhub

docker run -d --name jupyterhub \
  -p 8000:8000 \
  my-jupyterhub \
  jupyterhub --Authenticator.allow_all=True
```

Then open:

```text
http://localhost:8000
```

## Run with `docker-compose`

From this folder:

```bash
docker compose up --build
```

## PAM authenticator (creating users inside the container)

When `PAMAuthenticator` is used, credentials are validated against **Linux users inside the container**.

Example user creation:

```bash
docker exec -it jupyterhub bash -lc "useradd -m student1 && echo 'student1:CHANGE_ME' | chpasswd"
```

Login:

```text
username: student1
password: CHANGE_ME
```

## Useful commands

```bash
docker logs --tail 200 jupyterhub
docker restart jupyterhub
docker stop jupyterhub
docker rm -f jupyterhub
```

## Using a custom `jupyterhub_config.py`

This repo includes a sample config at:

- `./jupyterhub_config.py`

To start the container with that config:

### Windows

```powershell
docker run -d --name jupyterhub -p 8000:8000 `
  -v "${PWD}\jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py" `
  my-jupyterhub
```

### Linux / macOS

```bash
docker run -d --name jupyterhub -p 8000:8000 \
  -v "$(pwd)/jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py" \
  my-jupyterhub
```

## Production notes (AWS optional)

You can run JupyterHub on AWS (e.g., ECS), but you must solve:

- Persistent storage (e.g., EFS)
- Hub state + database persistence (avoid losing `/srv/jupyterhub`)

Typical production components:

- Application Load Balancer (ALB)
- ECS Service (Hub)
- DockerSpawner (one container per user) or KubeSpawner
- RDS PostgreSQL (Hub DB)
- EFS (persistent user notebooks)
- ECR (image registry)
- CloudWatch Logs

Security notes:

- Do not use `allow_all` in production
- Use LDAP/OIDC where appropriate
- Do not hardcode secrets in config files
