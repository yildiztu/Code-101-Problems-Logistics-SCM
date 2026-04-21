# 03. The Manual Reefer Monitoring Problem

## 📋 Problem Overview

Terminal supervisor Maria Rodriguez faces a daunting challenge at the Port of Valencia's Container Terminal. With 2,400 refrigerated containers currently in the yard, her team of 18 inspectors must perform mandatory temperature checks every 4 hours around the clock. The recent implementation of stricter EU regulations requires detailed documentation of every inspection, including timestamp, container ID, temperature readings, alarm status, and inspector identification.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P3-Tier-1_executed.ipynb`](./P3-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each container must be inspected exactly once per inspection cycle
  - Inspectors have limited working capacity per shift


### **Tier 2**: The Classic Heuristic (Priority-Based Greedy Algorithm) — [`P3-Tier-2_executed.ipynb`](./P3-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Inspectors can be assigned containers sequentially based on priority scoring
  - Multi-criteria evaluation balances urgency, safety, and workload considerations


### **Tier 3**: The Advanced Algorithm (Simulated Annealing Metaheuristic) — [`P3-Tier-3_executed.ipynb`](./P3-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Simulated annealing can escape local optima through controlled stochastic exploration
  - Temperature schedule controls the balance between exploration and exploitation


### **Tier 4**: The AI/ML/RL Augmentation Method (Deep Q-Network) — [`P3-Tier-4_executed.ipynb`](./P3-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Reinforcement Learning can learn optimal inspection policies through experience
  - Deep Q-Network can handle complex state spaces with continuous variables


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 3)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 2**: The Container Stacking Rules Problem
- **Problem 4**: The FCFS Berth Scheduling Problem
