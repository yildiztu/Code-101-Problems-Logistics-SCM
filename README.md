# Code — 101 Problems (Jupyter Notebooks) 🚢📦

## Overview 📘

This workspace contains Jupyter notebooks for solving 101 programming problems, organized by problem and difficulty tiers. The notebooks are designed to be educational and reproducible, providing executable, well-documented solutions and visualizations for each problem.

## Relationship to the Books 📚

The 101 problems in this repository are derived from the following books published on Amazon.com:

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

* **Problem Categories 📂:** The 101 problems are organized into two main categories:
  * `Part I - The Port & Container Terminal (Problems 1-46)/` - Container terminal and port operations problems
  * `Part II - The End-to-End Supply Chain (Problems 47-101)/` - Full supply chain and logistics problems
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

All three books and the 101 problems are authored by **Turkay Yildiz, Ph.D.**. This repository serves as a Jupyter-based companion to that work, turning the playbook’s concepts and problem statements into executable models and interactive experiments.

Turkay Yildiz received his Ph.D. from the Institute of Marine Sciences and Technology at Dokuz Eylul University in Izmir, Turkey. He holds degrees in Electronics and Management, and a Master’s Degree in Logistics Management from Izmir University of Economics. His research and professional interests span transportation, port operations, logistics, and supply chain management, and he has authored numerous peer‑reviewed publications and conference presentations in these fields. He also has extensive experience in applying information technologies to logistics and supply chain problems.

Research profile: https://www.researchgate.net/profile/Turkay-Yildiz 🔗

## Using and Citing This Work 📖

If you use these notebooks in teaching, research, or practice, please cite the underlying books as the primary sources of the problem statements and conceptual framework:

* Yildiz, T. (2025). *The logistics problem-solving playbook: 101 problems edition, Part I – The port & container terminal playbook (Problems 1–46).* Amazon.com. https://www.amazon.com/dp/B0FV7ZK9D5
* Yildiz, T. (2025). *The logistics problem-solving playbook: 101 problems edition, Part II – The end-to-end supply chain playbook (Problems 47–101).* Amazon.com. https://www.amazon.com/dp/B0FV89XJZ5
* Yildiz, T. (2024). *Logistics and supply chain management in the modern era: Trends, technologies, and best practices.* Amazon.com. https://www.amazon.com/dp/B0DKHYRT89

You may also reference this repository as a Jupyter-based companion that provides executable implementations, visualizations, and extensions of the problems defined in the books.

## Contributions 🤝

Feedback, suggestions, and improvements are welcome. If you identify an error, have an idea for a clearer visualization, or want to extend a tier with an alternative method (e.g., a different heuristic, metaheuristic, or learning approach), feel free to open an issue or submit a pull request.

When contributing, please keep the spirit of the project in mind:

* Prioritize clarity, pedagogy, and reproducibility.
* Prefer open-source dependencies and document any non-trivial setup steps.
* Maintain the tiered structure and clearly explain how a new method relates to the original problem.
