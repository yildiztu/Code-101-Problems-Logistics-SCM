# 24. The Static Truck Appointment System Problem

## 📋 Problem Overview

Consider the bustling Port of Los Angeles, where over 15,000 truck transactions occur daily across multiple terminals. The Metropolitan Container Terminal faces a persistent challenge: trucks arrive in unpredictable waves throughout the day, creating severe bottlenecks during peak hours (typically 8-10 AM and 2-4 PM) while leaving resources underutilized during off-peak periods. These congestion patterns result in trucks waiting up to 2-3 hours during peak times, leading to increased operational costs, driver frustration, air pollution, and strained community relations.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P24-Tier-1_executed.ipynb`](./P24-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each truck request has a preferred time slot and priority weight
  - Each time slot has a fixed processing capacity


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P24-Tier-2_executed.ipynb`](./P24-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Requests are processed in order of preferred time (earliest deadline first)
  - Greedy assignment strategy with capacity checking


### **Tier 3**: The Advanced Algorithm (Metaheuristic Implementation) — [`P24-Tier-3_executed.ipynb`](./P24-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Artificial ants construct complete assignment solutions iteratively
  - Pheromone trails guide subsequent ants toward promising assignments


### **Tier 4**: The AI/ML/RL Augmentation Method — [`P24-Tier-4_executed.ipynb`](./P24-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Historical appointment data is available for training
  - Patterns exist in successful vs unsuccessful assignments


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P24-Tier-5_executed.ipynb`](./P24-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Real-time data synchronization with physical terminal operations
  - IoT sensors, GPS tracking, and RFID systems provide continuous data streams


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 24)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 16**: The Storage Location Assignment Problem (SLAP)
- **Problem 17**: The Container Reshuffling (Remarshalling) Problem
- **Problem 18**: The Yard Crane (RTG_RMG) Scheduling Problem
