# Code — 101 Problems (Jupyter Notebooks) 🚢📦

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter)](https://jupyter.org/)
[![YouTube](https://img.shields.io/badge/YouTube-IntelliBoost-red.svg?logo=youtube)](https://www.youtube.com/@IntelliBoost/courses)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

> *A comprehensive, interactive, and tiered approach to solving 101 complex logistics and supply chain problems using Python and Jupyter Notebooks.*

---

<details>
<summary><b>📖 Table of Contents</b></summary>

- [Overview 📘](#overview-)
- [Relationship to the Books 📚](#relationship-to-the-books-)
- [Video Courses & Tutorials 🎥](#video-courses--tutorials-)
- [Tiered Notebook Philosophy 🧠](#tiered-notebook-philosophy-)
- [Target Audience 🎯](#target-audience-)
- [Repository Structure 📁](#repository-structure-)
- [Running the Notebooks ▶️](#running-the-notebooks-️)
- [GitHub Setup & Usage 🚀](#github-setup--usage-)
- [Design Principles ⚙️](#design-principles-️)
- [About the Author ✍️](#about-the-author-️)
- [Using and Citing This Work 📖](#using-and-citing-this-work-)
- [Contributions 🤝](#contributions-)

</details>

---

## Overview 📘

This workspace contains Jupyter notebooks for solving **101 programming problems**, organized by problem and difficulty tiers. The notebooks are designed to be educational and reproducible, providing executable, well-documented solutions and visualizations for each problem.

## Relationship to the Books 📚

The 101 problems in this repository are derived from the following books published on Amazon.com:

* **The Logistics Problem-Solving Playbook: 101 Problems Edition: Part I: The Port & Container Terminal Playbook (Problems 1-46)**: An applied playbook focused on 46 core problems at container terminals and ports. Covers topics such as single crane lift sequencing, container stacking rules, dynamic berth allocation, and quay crane scheduling, introducing the 12-Tier Framework as a way to benchmark and systematically improve terminal operations.
	+ https://www.amazon.com/dp/B0FV7ZK9D5
* **The Logistics Problem-Solving Playbook: 101 Problems Edition: Part II: The End-to-End Supply Chain Playbook (Problems 47-101)**: Extends the playbook from the terminal to the full end-to-end supply chain. Builds on the same 12-Tier Framework to connect port operations with network-wide planning, inventory, transportation, and strategic decision-making across 55 advanced logistics problems.
	+ https://www.amazon.com/dp/B0FV89XJZ5
* **Logistics and Supply Chain Management in the Modern Era: Trends, Technologies, and Best Practices**: A comprehensive guide to modern logistics and supply chain management, covering fundamentals (inventory, transportation, warehousing), strategy (JIT, VMI, 3PL), analytics (big data, AI), sustainability, risk and resilience, and the impact of emerging technologies such as IoT, blockchain, and autonomous systems.
	+ https://www.amazon.com/dp/B0DKHYRT89

## Video Courses & Tutorials 🎥

To complement the books and Jupyter notebooks, you can follow along with full video courses and tutorials on our YouTube channel. These videos walk through the problem-solving processes and code implementations step-by-step:

### 📺 Featured Video Courses

<table align="center">
  <tr>
    <td align="center" width="50%">
      <a href="https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu">
        <img src="https://img.youtube.com/vi/25kv-tONUck/maxresdefault.jpg" alt="Part I Course Thumbnail" width="100%" style="border-radius: 8px;">
      </a>
      <br>
      <strong>🚢 Part I: The Port & Container Terminal Course</strong><br>
      <em>Video series covering Problems 1-46</em><br>
      <a href="https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu">Watch Playlist →</a>
    </td>
    <td align="center" width="50%">
      <a href="https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z">
        <img src="https://img.youtube.com/vi/himrb9cEuz8/maxresdefault.jpg" alt="Part II Course Thumbnail" width="100%" style="border-radius: 8px;">
      </a>
      <br>
      <strong>🔗 Part II: The End-to-End Supply Chain Course</strong><br>
      <em>Video series covering Problems 47-101</em><br>
      <a href="https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z">Watch Playlist →</a>
    </td>
  </tr>
</table>

### 📚 Additional Resources

* **[IntelliBoost YouTube Channel](https://www.youtube.com/@IntelliBoost/courses)** — *Subscribe for all courses and updates!*
* **[Individual Problem Tutorials](https://www.youtube.com/@IntelliBoost/videos)** — *Browse specific problem solutions*

> 💡 **Tip:** Each video corresponds to specific notebook tiers. Look for the problem number in the video title to match with the Jupyter notebooks in this repository.

## Tiered Notebook Philosophy 🧠

The notebooks in this repository are organized using a **tiered structure**, inspired by the **12-Tier Framework** introduced in the playbook. Each problem folder corresponds to one or more exercises from the books and expands them with step-by-step, beginner-friendly Jupyter implementations.

The tiered approach generally follows a progression from exact mathematical foundations to advanced AI and real-time simulations:
1. **Tier 1**: Mathematical Formulation (MIP, Pen & Paper)
2. **Tier 2**: Classic Heuristic Algorithms
3. **Tier 3**: Advanced Metaheuristics (GA, PSO, ACO)
4. **Tier 4**: AI/ML and Reinforcement Learning
5. **Tier 5+**: Digital Twins, Human-AI Collaboration, and Quantum Computing

> *Note: The specific tiers and total number of tiers may vary per problem.*

## Target Audience 🎯

This repository is designed for:
- 🎓 **Students & Educators** interested in learning logistics and supply chain concepts through hands-on problem-solving.
- 🧑‍💻 **Data Scientists & Operations Researchers** looking for practical implementations of complex optimization algorithms.
- 🏢 **Supply Chain Professionals** exploring advanced concepts like Digital Twins, Reinforcement Learning, and Quantum Computing in logistics.

## Repository Structure 📁

* **Problem Categories 📂:** The 101 problems are organized into two main categories:
  * `Part I - The Port & Container Terminal (Problems 1-46)/` - Container terminal and port operations problems
  * `Part II - The End-to-End Supply Chain (Problems 47-101)/` - Full supply chain and logistics problems

* **Within-Part Grouping 📂:** Within each Part, problems are grouped under TOC-based subfolders (A–E) for cleaner navigation:

  **Part I - The Port & Container Terminal:**
  * **A. Foundations of Terminal Operations (The Building Blocks)** - Basic terminal operations including crane sequencing, container stacking, reefer monitoring, berth scheduling, and gate operations (Problems 1-6)
  * **B. Core Quay-Side Operations (The Ship-to-Shore Interface)** - Ship-to-shore operations including berth allocation, quay crane assignment/scheduling, dual cycling, and vessel stowage (Problems 7-15)
  * **C. Core Yard & Land-Side Operations (The Heart of the Terminal)** - Yard operations including storage location assignment, container reshuffling, yard crane scheduling, and truck/AGV dispatching (Problems 16-26)
  * **D. Integrated Tactical & Pre-Planning Problems (Connecting the Silos)** - Cross-functional integration including berth-crane coordination, yard pre-marshalling, rail-terminal scheduling, and labor management (Problems 27-34)
  * **E. Strategic Design & Long-Term Investment (Shaping the Future)** - Strategic planning including terminal layout, equipment selection, capacity expansion, and competitive pricing (Problems 35-46)

  **Part II - The End-to-End Supply Chain:**
  * **A. Foundational Analytics & Inventory Control (The Language of Supply Chain)** - Demand forecasting, inventory policies (EOQ, newsvendor), and ABC/XYZ classification (Problems 47-58)
  * **B. Warehouse & Fulfillment Center Operations (Inside the Four Walls)** - Warehouse design, slotting optimization, order picking, and value-added services (Problems 59-68)
  * **C. Transportation, Routing & Freight Management (The Physical Internet)** - Vehicle routing problems, fleet management, freight mode selection, and loading optimization (Problems 69-81)
  * **D. Strategic Network Design & Sourcing (The Blueprint of the Business)** - Facility location, supplier selection, sourcing strategies, and contract design (Problems 82-91)
  * **E. Integrated, Resilient, & Modern Supply Chains (The Frontier)** - Location-routing, inventory-routing, resilient networks, last-mile delivery, and sustainable logistics (Problems 92-101)

* **Problem Folders 📂:** Each problem has its own folder containing multiple tiered notebooks with increasing complexity and depth.
* `infrastructure/jupyterhub/` 🐳: A Docker-based JupyterHub setup you can run locally on Windows/macOS/Linux.

## Running the Notebooks ▶️

### � Quick Start (Recommended)

**Prerequisites:** Python 3.11+ installed on your system

```bash
# Clone the repository
git clone https://github.com/yildiztu/Code-101-Problems.git
cd Code-101-Problems

# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install all required packages
pip install -r requirements.txt

# Launch JupyterLab
jupyter lab
```

### 📦 Package Requirements

All 630 executed notebooks have been tested with the following packages:

**Core Scientific Computing (Required):**
- `numpy>=1.24.0` - Used in all 630 notebooks
- `pandas>=2.0.0` - Used in 522 notebooks
- `matplotlib>=3.7.0` - Used in all 630 notebooks
- `seaborn>=0.12.0` - Used in 567 notebooks
- `scipy>=1.10.0` - Used in 65 notebooks

**Optimization Libraries (Required):**
- `pulp>=2.7.0` - Used in 48 notebooks for linear/integer programming

**Machine Learning (Optional):**
- `scikit-learn>=1.3.0` - For ML-based approaches
- `torch>=2.0.0` - Used in 11 notebooks for deep learning

**Network & Graph (Required):**
- `networkx>=3.1` - Used in 9 notebooks for graph algorithms

**Jupyter Support (Required):**
- `jupyter>=1.0.0`
- `jupyterlab>=4.0.0`
- `ipykernel>=6.25.0`
- `ipywidgets>=8.0.0`

See `requirements.txt` for the complete list of packages.

### 🐳 Docker Option (Containerized Environment)

**Prerequisites:** Docker installed on your system

```bash
# Build the Docker image
docker build -t logistics-playbook .

# Run the container
docker run -p 8888:8888 -v $(pwd):/workspace logistics-playbook

# Access JupyterLab at: http://localhost:8888
```

**Docker Features:**
- ✅ All dependencies pre-installed
- ✅ Consistent environment across platforms
- ✅ No local Python setup required
- ✅ Isolated from system packages

### ☁️ Cloud Platforms (Optional)

**Supported Platforms:**
- Google Colab
- Azure Notebooks
- AWS SageMaker

**Usage:** Upload individual notebooks to your preferred cloud platform

**Note:** Some advanced features may require additional configuration

## GitHub Setup & Usage 🚀

### Prerequisites:
* **Git Installation:**
  ```bash
  # Windows: Download from https://git-scm.com/download/win
  # macOS: brew install git
  # Linux (Ubuntu/Debian): sudo apt-get install git
  # Linux (Fedora): sudo dnf install git
  ```

* **GitHub Account:** Create account at https://github.com

### Clone Repository:
```bash
# Clone the repository
git clone https://github.com/yildiztu/Code-101-Problems.git

# Navigate to repository
cd Code-101-Problems
```

### Platform-Specific Setup:

**Windows:**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install jupyterlab numpy pandas matplotlib seaborn

# Launch JupyterLab
jupyter lab
```

**macOS/Linux:**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install jupyterlab numpy pandas matplotlib seaborn

# Launch JupyterLab
jupyter lab
```

### Repository Updates:
```bash
# Navigate to repository directory
cd Code-101-Problems

# Pull latest changes
git pull origin main

# Activate virtual environment (if needed)
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
```

## Design Principles ⚙️

* The notebooks are designed to be educational and reproducible. 📊
* By default, dependencies should be open-source. Any use of cloud services (e.g., AWS) must be explicitly justified and clearly documented within the corresponding notebook. 🌐

## About the Author ✍️

All three books and the 101 problems are authored by **Turkay Yildiz, Ph.D.**. This repository serves as a Jupyter-based companion to that work, turning the playbook’s concepts and problem statements into executable models and interactive experiments.

Turkay Yildiz received his Ph.D. from the Institute of Marine Sciences and Technology at Dokuz Eylul University in Izmir, Turkey. He holds degrees in Electronics and Management, and a Master’s Degree in Logistics Management from Izmir University of Economics. His research and professional interests span transportation, port operations, logistics, and supply chain management, and he has authored numerous peer‑reviewed publications and conference presentations in these fields. He also has extensive experience in applying information technologies to logistics and supply chain problems.

**Academic Profiles & Publications:**
* 🔬 **ResearchGate:** [Turkay-Yildiz](https://www.researchgate.net/profile/Turkay-Yildiz)
* 🎓 **Google Scholar:** [Publications](https://scholar.google.com/citations?user=dxYzo_AAAAAJ)
* 🆔 **ORCID:** [0000-0003-0851-050X](https://orcid.org/0000-0003-0851-050X)
* 🌐 **SciProfiles:** [turkay-yildiz](https://sciprofiles.com/profile/turkay-yildiz)

## Using and Citing This Work 📖

If you use these notebooks in teaching, research, or practice, please cite the underlying books as the primary sources of the problem statements and conceptual framework.

### APA Style (7th Edition)
```text
Yildiz, T. (2025). The logistics problem-solving playbook: 101 problems edition, Part I – The port & container terminal playbook (Problems 1–46). Amazon.com. https://www.amazon.com/dp/B0FV7ZK9D5

Yildiz, T. (2025). The logistics problem-solving playbook: 101 problems edition, Part II – The end-to-end supply chain playbook (Problems 47–101). Amazon.com. https://www.amazon.com/dp/B0FV89XJZ5

Yildiz, T. (2024). Logistics and supply chain management in the modern era: Trends, technologies, and best practices. Amazon.com. https://www.amazon.com/dp/B0DKHYRT89
```

### MLA Style (9th Edition)
```text
Yildiz, Turkay. The Logistics Problem-Solving Playbook: 101 Problems Edition, Part I – The Port & Container Terminal Playbook (Problems 1–46). Amazon.com, 2025, https://www.amazon.com/dp/B0FV7ZK9D5.

Yildiz, Turkay. The Logistics Problem-Solving Playbook: 101 Problems Edition, Part II – The End-to-End Supply Chain Playbook (Problems 47–101). Amazon.com, 2025, https://www.amazon.com/dp/B0FV89XJZ5.

Yildiz, Turkay. Logistics and Supply Chain Management in the Modern Era: Trends, Technologies, and Best Practices. Amazon.com, 2024, https://www.amazon.com/dp/B0DKHYRT89.
```

### Chicago Style (17th Edition - Author-Date)
```text
Yildiz, Turkay. 2025. The Logistics Problem-Solving Playbook: 101 Problems Edition, Part I – The Port & Container Terminal Playbook (Problems 1–46). Amazon.com. https://www.amazon.com/dp/B0FV7ZK9D5.

Yildiz, Turkay. 2025. The Logistics Problem-Solving Playbook: 101 Problems Edition, Part II – The End-to-End Supply Chain Playbook (Problems 47–101). Amazon.com. https://www.amazon.com/dp/B0FV89XJZ5.

Yildiz, Turkay. 2024. Logistics and Supply Chain Management in the Modern Era: Trends, Technologies, and Best Practices. Amazon.com. https://www.amazon.com/dp/B0DKHYRT89.
```

You may also reference this repository as a Jupyter-based companion that provides executable implementations, visualizations, and extensions of the problems defined in the books.

## Contributions 🤝

Feedback, suggestions, and improvements are welcome. If you identify an error, have an idea for a clearer visualization, or want to extend a tier with an alternative method (e.g., a different heuristic, metaheuristic, or learning approach), feel free to open an issue or submit a pull request.

When contributing, please keep the spirit of the project in mind:

* Prioritize clarity, pedagogy, and reproducibility.
* Prefer open-source dependencies and document any non-trivial setup steps.
* Maintain the tiered structure and clearly explain how a new method relates to the original problem.
