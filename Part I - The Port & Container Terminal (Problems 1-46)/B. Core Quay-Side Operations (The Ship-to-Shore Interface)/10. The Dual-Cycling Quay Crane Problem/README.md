# 10. The Dual-Cycling Quay Crane Problem

## 📋 Problem Overview

In a bustling container terminal, quay cranes represent the critical bottleneck that determines overall port productivity. Traditional single-cycle operations involve a crane performing either an unload or a load operation before returning to its starting position, often with an empty spreader. The dual-cycling paradigm fundamentally transforms this approach by coordinating unload and load operations such that a crane can pick up an import container from the vessel, transport it to the yard, and immediately pick up an export container for loading onto the vessel in a continuous productive cycle.

## 🎯 Solution Approaches

### **Tier 1**: Markov Decision Process (MDP) Formulation — [`P10-Tier-1_executed.ipynb`](./P10-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Stochastic operation times with potential delays
  - Finite set of crane positions and container states


### **Tier 2**: The Classic Heuristic (Divide and Conquer Decomposition) — [`P10-Tier-2_executed.ipynb`](./P10-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Natural hierarchical structure in container operations can be exploited
  - Independence properties emerge when proper decomposition boundaries are established


### **Tier 3**: The Advanced Algorithm (Firefly Algorithm with Light Intensity Attraction) — [`P10-Tier-3_executed.ipynb`](./P10-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Solutions can be represented as discrete permutations of operations
  - Attractiveness between solutions is proportional to their quality difference


### **Tier 4**: The AI/ML/RL Augmentation Method (Imitation Learning Framework) — [`P10-Tier-4_executed.ipynb`](./P10-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Expert operators (or optimal solvers) demonstrate high-quality decision patterns
  - State-action pairs can capture the essence of crane scheduling decisions


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P10-Tier-5_executed.ipynb`](./P10-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Real-time synchronization between physical and digital systems (<50ms latency)
  - 1Hz update frequency for all subsystem state synchronization


### **Tier 9**: The Quantum Leap (Quantum Approximate Optimization Algorithm) — [`P10-Tier-9_executed.ipynb`](./P10-Tier-9_executed.ipynb)
- **Learning Goals**:
  - Quantum hardware with sufficient qubits for problem encoding (288 qubits for 3 cranes, 8 containers, 12 time slots)
  - QAOA circuit depth p=2 for balance between expressiveness and hardware constraints


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 10)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 7**: The Static Berth Allocation Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
