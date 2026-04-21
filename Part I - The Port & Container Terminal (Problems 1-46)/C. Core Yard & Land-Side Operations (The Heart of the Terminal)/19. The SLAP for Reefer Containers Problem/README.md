# 19. The SLAP for Reefer Containers Problem

## 📋 Problem Overview

Container Terminal Delta operates 24/7 handling over 500 reefer containers daily, ranging from pharmaceutical shipments requiring precise $-20°C$ storage to fresh produce needing controlled atmosphere conditions. The terminal features 150 reefer power points distributed across six storage blocks, each with different power capacities, monitoring capabilities, and accessibility levels.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation (Mixed-Integer Programming) — [`P19-Tier-1_executed.ipynb`](./P19-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each reefer container must be assigned to exactly one storage location
  - Storage locations have limited power capacity and temperature ranges


### **Tier 2**: Classic Heuristic (First-Fit Decreasing Algorithm) — [`P19-Tier-2_executed.ipynb`](./P19-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Containers are sorted by energy consumption in descending order (FFD strategy)
  - Each container is assigned to the first feasible location based on power and temperature


### **Tier 3**: Advanced Algorithm (Ant Colony Optimization) — [`P19-Tier-3_executed.ipynb`](./P19-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Ant colony uses pheromone trails to learn good container-location assignments
  - Multiple ants (20) construct solutions in parallel each iteration


### **Tier 4**: AI/ML/RL Augmentation (Deep Reinforcement Learning) — [`P19-Tier-4_executed.ipynb`](./P19-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Deep Q-Network (DDQN) learns optimal assignment policies through experience
  - Environment provides state information and rewards for assignment decisions


### **Tier 5**: Integrated Digital Twin (System-of-Systems Simulation) — [`P19-Tier-5_executed.ipynb`](./P19-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Digital Twin creates real-time virtual replica of reefer terminal ecosystem
  - Multi-layer architecture: Physical → Connectivity → Data → Application


### **Tier 6**: Autonomous Self-Optimizing Ecosystem (Distributed Intelligence) — [`P19-Tier-6_executed.ipynb`](./P19-Tier-6_executed.ipynb)
- **Learning Goals**:
  - Multi-agent system with autonomous container and location agents
  - Contract Net Protocol for distributed negotiation and coordination


### **Tier 8**: Value-Aligned & Ethical Framework (Constitutional AI) — [`P19-Tier-8_executed.ipynb`](./P19-Tier-8_executed.ipynb)
- **Learning Goals**:
  - Multi-stakeholder value optimization beyond pure cost minimization
  - Constitutional AI with ethical principles and fairness constraints


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 19)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 16**: The Storage Location Assignment Problem (SLAP)
- **Problem 17**: The Container Reshuffling (Remarshalling) Problem
- **Problem 18**: The Yard Crane (RTG_RMG) Scheduling Problem
