# 05. Problem Title

## 📋 Problem Overview

Pacific Coast Distribution Center operates a major import-export facility serving the Los Angeles metropolitan area, processing over 2,000 truck movements daily through a constrained gate infrastructure. The facility currently experiences severe congestion during peak hours, with truck waiting times exceeding 45 minutes and gate utilization rates dropping below 60\% during off-peak periods[1][4].

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P5-Tier-1_executed.ipynb`](./P5-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Trucks flow through processing stations with limited capacity and defined service rates
  - Gate system can be modeled as a directed graph with nodes and arcs


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P5-Tier-2_executed.ipynb`](./P5-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Trucks arrive with known priorities and processing requirements
  - Gate resources have different service rates and availability


### **Tier 3**: The Advanced Algorithm (Metaheuristic Implementation) — [`P5-Tier-3_executed.ipynb`](./P5-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Gate scheduling exhibits complex nonlinear relationships
  - Multiple objectives conflict: minimize waiting times, maximize throughput, balance utilization


### **Tier 4**: The Machine Learning Approach (Reinforcement Learning) — [`P5-Tier-4_executed.ipynb`](./P5-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Gate assignment can be modeled as a sequential decision-making problem
  - Reinforcement learning can discover optimal policies through trial and error


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P5-Tier-5_executed.ipynb`](./P5-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Terminal operations can be modeled as interconnected system components
  - Real-time data streams continuously update the virtual model


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 5)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 2**: The Container Stacking Rules Problem
- **Problem 3**: The Manual Reefer Monitoring Problem
