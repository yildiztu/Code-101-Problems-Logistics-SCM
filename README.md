# Code — 101 Problems (Jupyter Notebooks) 🚢📦

## Overview 📘

This workspace contains Jupyter notebooks for solving 101 programming problems, organized by problem and difficulty tiers. The notebooks are designed to be educational and reproducible, providing executable, well-documented solutions and visualizations for each problem.

## Relationship to the Books 📚

The 101 problems in this repository are derived from the following books published on Amazon Kindle:

* **The Logistics Problem-Solving Playbook: 101 Problems Edition: Part I: The Port & Container Terminal Playbook (Problems 1-46)**: An applied playbook focused on 46 core problems at container terminals and ports. Covers topics such as single crane lift sequencing, container stacking rules, dynamic berth allocation, and quay crane scheduling, introducing the 12-Tier Framework as a way to benchmark and systematically improve terminal operations.
	+ https://www.amazon.com/dp/B0FV7ZK9D5
* **The Logistics Problem-Solving Playbook: 101 Problems Edition: Part II: The End-to-End Supply Chain Playbook (Problems 47-101)**: Extends the playbook from the terminal to the full end-to-end supply chain. Builds on the same 12-Tier Framework to connect port operations with network-wide planning, inventory, transportation, and strategic decision-making across 55 advanced logistics problems.
	+ https://www.amazon.com/dp/B0FV89XJZ5
* **Logistics and Supply Chain Management in the Modern Era: Trends, Technologies, and Best Practices**: A comprehensive guide to modern logistics and supply chain management, covering fundamentals (inventory, transportation, warehousing), strategy (JIT, VMI, 3PL), analytics (big data, AI), sustainability, risk and resilience, and the impact of emerging technologies such as IoT, blockchain, and autonomous systems.
	+ https://www.amazon.com/dp/B0DKHYRT89

## Tiered Notebook Philosophy 🧠

The notebooks in this repository are organized using a tiered structure, inspired by the 12-Tier Framework introduced in the playbook. Each problem folder corresponds to one or more exercises from the books and expands them with step-by-step, beginner-friendly Jupyter implementations. The tier numbers may vary per problem.

## Target Audience 🎯

This repository is designed for individuals interested in learning and practicing logistics and supply chain management concepts through hands-on problem-solving.

## Repository Structure 📁

* **Problem Folders 📂:** Each problem has its own folder containing multiple tiered notebooks with increasing complexity and depth.
* `infrastructure/jupyterhub/` 🐳: A Docker-based JupyterHub setup you can run locally on Windows/macOS/Linux.

## Running the Notebooks ▶️

* **Option A (simplest) 💻:** Run notebooks locally with JupyterLab
	+ Install Python, create a virtual environment, install `jupyterlab`.
	+ Open the generated `.ipynb` notebooks.
* **Option B (classroom / multi-user) 👥:** Run JupyterHub via Docker
	+ See: `infrastructure/jupyterhub/README.md`

## Design Principles ⚙️

* The notebooks are designed to be educational and reproducible. 📊
* By default, dependencies should be open-source. Any use of cloud services (e.g., AWS) must be explicitly justified and clearly documented within the corresponding notebook. 🌐

## About the Author ✍️

All three books and the 101 problems are authored by **Turkay Yildiz, Ph.D.**. This repository serves as a Jupyter-based companion to the books, providing executable, well-documented solutions and visualizations for each problem.
