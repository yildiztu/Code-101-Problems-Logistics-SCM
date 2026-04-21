# 18. The Yard Crane (RTG/RMG) Scheduling Problem

## 📋 Problem Overview

At the Port of Rotterdam's Maasvlakte II terminal, the morning shift begins with a complex scheduling challenge. Twenty-six Rail Mounted Gantry Cranes (RMGCs) must coordinate the movement of over 2,400 containers across 68 storage blocks. Each crane operates within its designated corridor, unable to cross paths with its neighbors due to the non-crossing constraint---a fundamental limitation that transforms what might seem like a simple assignment problem into a sophisticated routing and scheduling challenge[2][3].

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P18-Tier-1_executed.ipynb`](./P18-Tier-1_executed.ipynb)
- **Learning Goals**:
  - - $J = \{1, 2, \ldots, n\}$: Set of jobs (container operations)
  - $K = \{1, 2, \ldots, m\}$: Set of available cranes


### **Tier 2**: The Classic Heuristic (Cheapest Insertion Algorithm) — [`P18-Tier-2_executed.ipynb`](./P18-Tier-2_executed.ipynb)
- **Learning Goals**:
  - - **Partial Route Construction**: Start with empty crane routes and build incrementally
  - **Cost Evaluation**: For each unscheduled job, evaluate insertion costs across all cranes and positions


### **Tier 3**: The Advanced Algorithm (Grasshopper Optimization Algorithm) — [`P18-Tier-3_executed.ipynb`](./P18-Tier-3_executed.ipynb)
- **Learning Goals**:
  - The position update equation for grasshopper $i$ is: $$X_i^{t+1} = c \left( \sum_{j=1, j \neq i}^{N} c \frac{|x_j^t - x_i^t|}{d_{ij}} \hat{u}_{ij} s(d_{ij}) \right) + \hat{T}$$
  - $c$ is the decreasing coefficient controlling exploration/exploitation


### **Tier 4**: The AI/ML/RL Augmentation Method (Neural Architecture Search) — [`P18-Tier-4_executed.ipynb`](./P18-Tier-4_executed.ipynb)
- **Learning Goals**:
  - **Current crane positions and orientations**: Real-time location data
  - **Pending job queue with priorities and time windows**: Workload information


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P18-Tier-5_executed.ipynb`](./P18-Tier-5_executed.ipynb)
- **Learning Goals**:
  - and predictive optimization across interconnected terminal subsystems.
  - 1. **Physical Assets Layer**: Cranes, containers, vehicles, equipment 2. **Connectivity Layer**: IoT sensors, communication networks, data protocols 3. **Data Processing Layer**: Real-time analytics, 


### **Tier 6**: The Autonomous & Self-Optimizing Ecosystem (Distributed Intelligence) — [`P18-Tier-6_executed.ipynb`](./P18-Tier-6_executed.ipynb)
- **Learning Goals**:
  - - **Autonomous Decision Making**: Independent job selection and scheduling
  - **Inter-Agent Communication**: Direct negotiation and information sharing


### **Tier 7**: The Human-AI Symbiotic Partnership (The Centaur Model) — [`P18-Tier-7_executed.ipynb`](./P18-Tier-7_executed.ipynb)
- **Learning Goals**:
  - a framework where human operators and AI systems work in perfect harmony, each compensating for the other's weaknesses while amplifying their strengths.
  - - **Contextual Intelligence**: Deep understanding of terminal operations and constraints


### **Tier 9**: The Quantum Leap (QUBO Formulation) — [`P18-Tier-9_executed.ipynb`](./P18-Tier-9_executed.ipynb)
- **Learning Goals**:
  - - **Exponential State Space**: Quantum superposition allows simultaneous exploration of 2^n configurations
  - **Quantum Tunneling**: Ability to escape local optima through quantum barrier penetration


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 18)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 16**: The Storage Location Assignment Problem (SLAP)
- **Problem 17**: The Container Reshuffling (Remarshalling) Problem
- **Problem 19**: The SLAP for Reefer Containers Problem
