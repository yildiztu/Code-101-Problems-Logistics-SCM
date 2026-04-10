# 02. The Container Stacking Rules Problem

## 📋 Problem Overview

Maritime container terminals face a perpetual challenge: how to stack incoming containers in yard bays to minimize the number of reshuffles required when containers need to be retrieved for loading onto outbound vessels. Each reshuffle represents lost productivity, increased fuel consumption, and potential delays in vessel departure schedules.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical formulation (made runnable via exhaustive search) — [`P2-Tier-1_executed.ipynb`](./P2-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Understand how **departure times** create a natural “retrieval order”.
  - Learn a simple and concrete definition of **blocking** and **reshuffles**.
- **Outputs**:
  - An optimal stacking plan for a small example instance.
  - The number of reshuffles implied by that plan.


### **Tier 2**: Priority-based constructive heuristic (runnable) — [`P2-Tier-2_executed.ipynb`](./P2-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Build a simple but practical stacking rule from scratch.
  - Understand how scoring criteria (blocking risk, height balance, weight stability) change decisions.
- **Outputs**:
  - A step-by-step placement table (container → chosen stack/tier → score details)
  - Final stack configuration


### **Tier 3**: Genetic Algorithm (GA) for near-optimal stacking — [`P2-Tier-3_executed.ipynb`](./P2-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Understand how to encode a stacking plan as a **chromosome**.
  - Define a clear **fitness function** (lower reshuffles is better).


### **Tier 4**: Reinforcement Learning (RL) augmentation (runnable, no heavy deps) — [`P2-Tier-4_executed.ipynb`](./P2-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Understand the RL loop: state → action → reward → next state.
  - See how a reward based on **reshuffle risk** can guide learning.
- **Outputs**:
  - Training curves (episode penalty / reshuffles)
  - A greedy evaluation run (eps=0) on the example arrival order


### **Tier 8**: Value-aligned & ethical framework (runnable demo) — [`P2-Tier-8_executed.ipynb`](./P2-Tier-8_executed.ipynb)
- **Learning Goals**:
  - Translate values into measurable scores.
  - Understand constraint-based filtering (fairness thresholds).


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 2)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 3**: The Manual Reefer Monitoring Problem
- **Problem 4**: The FCFS Berth Scheduling Problem
