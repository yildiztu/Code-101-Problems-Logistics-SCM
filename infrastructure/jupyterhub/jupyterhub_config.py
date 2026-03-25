c = get_config()

# Hub network/bind
c.JupyterHub.bind_url = "http://:8000"

# Persist Hub state under /srv/jupyterhub (EFS mount recommended on ECS)
c.JupyterHub.cookie_secret_file = "/srv/jupyterhub/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////srv/jupyterhub/jupyterhub.sqlite"

# Default authenticator is PAM (Linux users inside the container)
# c.JupyterHub.authenticator_class = "jupyterhub.auth.PAMAuthenticator"

# Quick test (NOT for production): allow all usernames
# c.Authenticator.allow_all = True

# Optional: limit who can login
# c.Authenticator.allowed_users = {"yildiztu"}
# c.Authenticator.allowed_users = {"yildiztu", "alice", "bob"}

# Optional: admin users
# c.Authenticator.admin_users = {"yildiztu"}

# Spawner (default is LocalProcessSpawner)
# c.JupyterHub.spawner_class = "jupyterhub.spawner.LocalProcessSpawner"

# -------------------------
# LDAP (optional)
# -------------------------
# This image includes: jupyterhub-ldapauthenticator
# Enable LDAP by uncommenting below and setting your values.
#
# c.JupyterHub.authenticator_class = "ldapauthenticator.LDAPAuthenticator"
# c.LDAPAuthenticator.server_address = "ldap.yourdomain.com"
# c.LDAPAuthenticator.server_port = 389
# c.LDAPAuthenticator.use_ssl = False
#
# # Simple bind template
# c.LDAPAuthenticator.bind_dn_template = "cn={username},ou=users,dc=yourdomain,dc=com"
#
# # Alternative search/bind (common in corporate LDAP)
# # c.LDAPAuthenticator.bind_dn = "cn=readonly,dc=yourdomain,dc=com"
# # c.LDAPAuthenticator.bind_password = "CHANGE_ME"
# # c.LDAPAuthenticator.user_search_base = "ou=users,dc=yourdomain,dc=com"
# # c.LDAPAuthenticator.user_attribute = "uid"
#
# # Optional: restrict to LDAP groups
# # c.LDAPAuthenticator.allowed_groups = [
# #     "cn=jupyterhub-users,ou=groups,dc=yourdomain,dc=com",
# # ]

# -------------------------
# Production notes (optional)
# -------------------------
# - For AWS ECS production: prefer external DB (e.g., RDS Postgres) and persistent storage (EFS)
# - For user isolation: consider DockerSpawner/KubeSpawner
#
# DockerSpawner example (commented)
#
# Requirements:
# - Install dockerspawner in the image
# - Run the Hub container with access to the Docker daemon (e.g., mount /var/run/docker.sock) or use a remote Docker host
#
# c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"
#
# c.JupyterHub.hub_ip = "0.0.0.0"
# c.JupyterHub.hub_port = 8000
#
# # Docker image for users
# c.DockerSpawner.image = "jupyter/base-notebook:latest"
#
# # notebook dir
# c.DockerSpawner.notebook_dir = "/home/jovyan/work"
#
# # user volumes
# c.DockerSpawner.volumes = {
#     "efs-home": "/home/jovyan"
# }
#
# # container network
# c.DockerSpawner.use_internal_ip = True
#
# # remove container after stop
# c.DockerSpawner.remove = True
#
# # CPU / RAM limits
# c.Spawner.cpu_limit = 1
# c.Spawner.mem_limit = "4G"
#
# Example external DB:
# c.JupyterHub.db_url = "postgresql://jupyterhub:PASSWORD@your-db-endpoint:5432/jupyterhub"
#
# Example:
# postgresql://jupyterhub:secret@your-db-host:5432/jupyterhub
