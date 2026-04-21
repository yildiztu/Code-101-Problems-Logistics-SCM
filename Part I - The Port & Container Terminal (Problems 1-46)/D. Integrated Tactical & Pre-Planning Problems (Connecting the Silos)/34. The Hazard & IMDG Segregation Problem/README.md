# 34. The Hazard \& IMDG Segregation Problem

## 📋 Problem Overview

Picture the MSV *Atlantic Carrier*, a container vessel crossing the North Atlantic with 2,400 TEUs aboard, including 340 containers carrying dangerous goods across all nine IMDG classes. The vessel's cargo planning team must ensure that incompatible hazardous materials---from Class 1 explosives to Class 8 corrosives---maintain proper segregation distances throughout the 14-day journey. A single segregation violation could result in catastrophic chemical reactions, regulatory violations, port rejections, or environmental disasters.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mixed-Integer Programming Formulation) — [`P34-Tier-1_executed.ipynb`](./P34-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each container must be assigned to exactly one position
  - Each position can hold at most one container


### **Tier 2**: The Classic Heuristic (Priority-Based Placement Algorithm) — [`P34-Tier-2_executed.ipynb`](./P34-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Containers are placed sequentially based on priority scores
  - Higher priority containers (with more restrictions) are placed first


### **Tier 3**: The Advanced Algorithm (Particle Swarm Optimization Implementation) — [`P34-Tier-3_executed.ipynb`](./P34-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Each particle represents a complete assignment of containers to positions
  - Particles move through solution space guided by personal and global best solutions


### **Tier 4**: The AI/ML/RL Augmentation Method (Deep Q-Network Implementation) — [`P34-Tier-4_executed.ipynb`](./P34-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Container placement is treated as a sequential decision-making problem
  - Agent learns through trial and error with reward feedback


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P34-Tier-5_executed.ipynb`](./P34-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Physical vessel has IoT sensors monitoring container integrity and environmental conditions
  - Digital model maintains real-time 3D representation with physics simulation


### **Tier 8**: The Value-Aligned & Ethical Framework — [`P34-Tier-8_executed.ipynb`](./P34-Tier-8_executed.ipynb)
- **Learning Goals**:
  - Algorithmic decisions must satisfy both safety optimization and ethical constraints
  - Multiple ethical dimensions: consequentialist, deontological, and virtue ethics


### **Tier 9**: The Quantum Leap (Quantum Approximate Optimization Algorithm) — [`P34-Tier-9_executed.ipynb`](./P34-Tier-9_executed.ipynb)
- **Learning Goals**:
  - QAOA maps segregation problem to Quadratic Unconstrained Binary Optimization (QUBO) formulation
  - Quantum superposition allows simultaneous exploration of all possible solutions


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 34)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 27**: The Integrated Berth & Crane Allocation Problem (BAP-QCAP)
- **Problem 28**: The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)
- **Problem 29**: The Integrated Quay Crane & Yard Truck Scheduling Problem
