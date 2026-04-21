# 36. The Berth \& Quay Length Design Problem

## 📋 Problem Overview

Mediterranean Logistics Hub (MLH) is planning a major expansion of its container terminal facilities. The port authority must decide on the optimal length of new quay infrastructure and the number of berths to construct. The challenge lies in the inherent uncertainty of future vessel traffic patterns, changing ship sizes in the global fleet, and evolving trade routes.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Robust Optimization Formulation) — [`P36-Tier-1_executed.ipynb`](./P36-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Vessel arrival rates are uncertain and follow probability distributions
  - Service times vary based on vessel size and cargo volume


### **Tier 2**: The Classic Heuristic (Constraint Propagation with Backtracking) — [`P36-Tier-2_executed.ipynb`](./P36-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Equipment selection constraints can be represented as logical relationships
  - Constraint propagation can significantly reduce the search space


### **Tier 2** — [`P37-Tier-2_executed.ipynb`](./P37-Tier-2_executed.ipynb)

### **Tier 3**: The Advanced Algorithm (Firefly Algorithm Implementation) — [`P36-Tier-3_executed.ipynb`](./P36-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Each firefly represents a complete berth configuration solution
  - Brightness (light intensity) corresponds to solution quality (inverse of total cost)


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P36-Tier-5_executed.ipynb`](./P36-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Digital twin integrates multiple interconnected subsystems (vessel traffic, cargo handling, yard operations, environmental monitoring)
  - Real-time sensor data continuously updates the digital model every 30 seconds


### **Tier 7**: The Human-AI Symbiotic Partnership (The Centaur Model) — [`P36-Tier-7_executed.ipynb`](./P36-Tier-7_executed.ipynb)
- **Learning Goals**:
  - Human experts provide strategic vision, stakeholder management, and creative problem-solving
  - AI systems provide computational optimization, pattern recognition, and rapid scenario analysis


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 36)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 27**: The Integrated Berth & Crane Allocation Problem (BAP-QCAP)
- **Problem 28**: The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)
- **Problem 29**: The Integrated Quay Crane & Yard Truck Scheduling Problem
