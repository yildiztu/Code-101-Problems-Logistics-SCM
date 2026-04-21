# 08. The Quay Crane Assignment Problem

## 📋 Problem Overview

Picture the bustling container terminal at the Port of Rotterdam at 6:00 AM on a typical Monday morning. Seven massive container vessels are simultaneously berthed along the 1,200-meter quay, each requiring immediate attention from the terminal's fleet of 12 quay cranes. The MSC\_Madrid has just arrived with 2,400 containers to discharge, while the COSCO\_Shanghai is waiting to load 1,800 containers destined for Asian ports. The Maersk\_Boston requires both discharge and loading operations totaling 3,200 container movements.

## 🎯 Solution Approaches

### **Tier 1**: Stochastic Programming Formulation — [`P8-Tier-1_executed.ipynb`](./P8-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Minimize expected total completion time: Σₛ pˢ Σᵥ Tᵥˢ


### **Tier 2**: The Classic Heuristic (Beam Search Implementation) — [`P8-Tier-2_executed.ipynb`](./P8-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Deterministic crane productivity rates (average across scenarios)
  - Priority-based vessel ordering


### **Tier 3**: The Advanced Algorithm (Differential Evolution Implementation) — [`P8-Tier-3_executed.ipynb`](./P8-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Real-valued encoding of crane assignments
  - Population-based search with multiple candidate solutions


### **Tier 4**: The AI/ML/RL Augmentation Method (Transfer Learning Implementation) — [`P8-Tier-4_executed.ipynb`](./P8-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Source domains have abundant historical QCAP data
  - Target domain has limited operational data


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P8-Tier-5_executed.ipynb`](./P8-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Real-time integration of multiple data sources
  - Continuous simulation of terminal operations


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 8)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 7**: The Static Berth Allocation Problem
- **Problem 9**: The Quay Crane Scheduling Problem
- **Problem 10**: The Dual-Cycling Quay Crane Problem
- **Problem 28**: The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)
