# Code — 101 Problems (Jupyter Notebooks)

This workspace contains Jupyter notebooks for solving 101 programming problems, organized by problem and difficulty tiers.

## What you will find here

- **Problem Folders:** Each problem has its own folder containing multiple tiered notebooks with increasing complexity and depth. Tier numbers may vary per problem.

- `TODO.md`
  - The project rules for generating one folder per problem and one `.ipynb` per Tier.
  - Non-negotiable requirements: open-source-first packages, highly explanatory notebooks, source-referenced examples, visualization, and AWS exceptions (quantum + optional cloud-scale production track).

- `infrastructure/jupyterhub/`
  - A Docker-based JupyterHub setup you can run locally on Windows/macOS/Linux.
  - Includes an English guide and minimal config to get started.

## Recommended way to run the notebooks

- **Option A (simplest):** Run notebooks locally with JupyterLab
  - Install Python, create a virtual environment, install `jupyterlab`.
  - Open the generated `.ipynb` notebooks.

- **Option B (classroom / multi-user):** Run JupyterHub via Docker
  - See: `infrastructure/jupyterhub/README.md`

## Notes

- The notebooks are designed to be educational and reproducible.
- By default, dependencies must be open-source. AWS usage is only allowed when explicitly justified by the source Tier policy (see `TODO.md`).
