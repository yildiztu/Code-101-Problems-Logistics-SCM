# 12. The Berth Allocation with Tidal Windows Problem

## 📋 Problem Overview

Consider the Port of Hamburg, Europe's third-largest container port, where the Elbe River's tidal range reaches up to 3.7 meters, creating dramatic operational constraints that ripple through the entire supply chain[3]. Every 12 hours and 25 minutes, the tide completes its cycle, opening and closing narrow windows of opportunity for deep-draft vessels that require sufficient water depth to safely navigate the river channels.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P12-Tier-1_executed.ipynb`](./P12-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Tidal windows are predictable and follow regular patterns
  - Vessel draft requirements must be satisfied at service time


### **Tier 2**: The Classic Heuristic (Hill Climbing with Random Restarts) — [`P12-Tier-2_executed.ipynb`](./P12-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Local search can effectively navigate the solution space
  - Random restarts help escape local optima


### **Tier 3**: The Advanced Algorithm (Cuckoo Search Metaheuristic) — [`P12-Tier-3_executed.ipynb`](./P12-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Lévy flights provide efficient search space exploration
  - Nest abandonment mechanism helps escape local optima


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P12-Tier-5_executed.ipynb`](./P12-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Tidal predictions are dynamic and update in real-time
  - Operations are subject to stochastic disruptions


### **Tier 7**: The Human-AI Symbiotic Partnership (The Centaur Model) — [`P12-Tier-7_executed.ipynb`](./P12-Tier-7_executed.ipynb)
- **Learning Goals**:
  - AI excels at calculation and constraint checking
  - Humans excel at context understanding and edge case management


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 12)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 7**: The Static Berth Allocation Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
