# 01. The Single Crane Lift Sequence Problem

## 📋 Problem Overview

Picture a bustling container terminal at the Port of Rotterdam during peak operational hours. A massive container bay houses 24 containers arranged in a 6×4 grid configuration, with containers stacked up to 3 levels high. Each container has a specific weight, destination, and priority level. A single overhead crane, equipped with both single-spreader and dual-spreader capabilities, must clear the entire bay to make room for an incoming vessel's cargo.

## 🎯 Solution Approaches

### **Tier 1**: Dynamic Programming (DP) — [`P1-Tier-1_executed.ipynb`](./P1-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Understand what a DP *state* is in sequencing problems.
  - See how **mode switching** (single vs dual) changes the objective.
- **Outputs**:
  - An optimal lift plan for a small instance.
  - A table with per-step time contributions.


### **Tier 2**: A Classic Heuristic (WSPT-inspired) — [`P1-Tier-2_executed.ipynb`](./P1-Tier-2_executed.ipynb)
- **Learning Goals**:
  - See how to build a heuristic score that balances:   - urgency (priority)   - travel time   - handling time   - mode switching costs
  - Understand why dual lifts can be beneficial even if they require a setup.


### **Tier 3**: Genetic Algorithm (GA) for near-optimal sequencing — [`P1-Tier-3_executed.ipynb`](./P1-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Understand the GA loop: initialize → evaluate → select → crossover → mutate → repeat
  - See how a "chromosome" (an ordering) can be evaluated by simulating crane operations


### **Tier 4**: Reinforcement Learning (RL) augmentation (DQN-style, runnable) — [`P1-Tier-4_executed.ipynb`](./P1-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Fixed action list (single or dual lift options)
  - Epsilon-greedy exploration


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 1)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 2**: The Container Stacking Rules Problem
- **Problem 3**: The Manual Reefer Monitoring Problem
- **Problem 4**: The FCFS Berth Scheduling Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
