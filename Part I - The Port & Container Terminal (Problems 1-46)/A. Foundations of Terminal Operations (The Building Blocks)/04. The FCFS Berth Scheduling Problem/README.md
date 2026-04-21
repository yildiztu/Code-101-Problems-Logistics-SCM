# 04. The FCFS Berth Scheduling Problem

## 📋 Problem Overview

The Mediterranean Hub Terminal operates four berths along a 1,200-meter quay, serving container vessels ranging from feeder ships carrying 500 TEU to ultra-large container vessels (ULCV) with capacities exceeding 20,000 TEU. Terminal management faces increasing pressure from shipping lines demanding adherence to published schedules while maximizing berth utilization and minimizing vessel waiting times.

## 🎯 Solution Approaches

### **Tier 1**: Network Flow Formulation (Mathematical Pen & Paper Method) — [`P4-Tier-1_executed.ipynb`](./P4-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Vessels must be served in first-come-first-served (FCFS) order
  - Each berth has physical constraints (length, draft capacity)


### **Tier 2**: Priority-Based FCFS Algorithm (Classic Heuristic) — [`P4-Tier-2_executed.ipynb`](./P4-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Vessels are served primarily in FCFS order but with limited priority-based flexibility
  - Priority scores combine vessel size, revenue, customer tier, and urgency factors


### **Tier 3**: PSO for FCFS-Constrained Berth Scheduling (Advanced Algorithm) — [`P4-Tier-3_executed.ipynb`](./P4-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Particles represent complete berth scheduling solutions in continuous search space
  - FCFS constraints are maintained through specialized position decoding procedures


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 4)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 2**: The Container Stacking Rules Problem
- **Problem 3**: The Manual Reefer Monitoring Problem
