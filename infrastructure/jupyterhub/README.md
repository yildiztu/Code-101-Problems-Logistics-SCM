# JupyterHub (Docker) — Setup and Run

This folder contains a minimal, reproducible setup to run **JupyterHub in Docker**.

The provided `Dockerfile` extends the official JupyterHub image and installs the packages needed for the single-user server (so users do not hit missing dependency errors after login):

- `jupyterlab`
- `jupyter_server`
- `jupyterhub-ldapauthenticator`
- `dockerspawner` (installed, optional to use)

It also preinstalls common open-source scientific packages used by the notebooks in this repository:

- `numpy`
- `pandas`
- `matplotlib`

This is intentional: in a classroom setting, it is better to **bake dependencies into the Docker image** so that notebooks run with `Run All` without per-notebook package installation.

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
