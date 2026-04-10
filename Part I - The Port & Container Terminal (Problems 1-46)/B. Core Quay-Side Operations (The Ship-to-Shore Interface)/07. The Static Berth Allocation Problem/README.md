# 07. The Static Berth Allocation Problem

## 📋 Problem Overview

Every morning at 06:00 hours, the Port of Singapore Authority faces a critical decision point. A fleet of container vessels—ranging from small feeders to massive ultra-large container vessels (ULCVs)—awaits berth allocation across the terminal's extensive quay infrastructure. The terminal operations manager must assign each vessel to an appropriate berth segment, considering vessel size constraints, handling equipment availability, and service priorities.

## 🎯 Solution Approaches

### **Tier 1**: Mixed Integer Programming (MIP) Formulation — [`P7-Tier-1_executed.ipynb`](./P7-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Understand how to model **spatial and temporal constraints** in maritime logistics
  - Learn **discretization techniques** for continuous time problems
- **Outputs**:
  - An optimal berth allocation plan for a small port instance
  - A Gantt chart visualization of ship schedules


### **Tier 2**: Advanced Heuristic Algorithms — [`P7-Tier-2_executed.ipynb`](./P7-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Understand **local search** techniques for combinatorial optimization
  - Learn **insertion heuristics** with look-ahead capabilities
- **Outputs**:
  - Multiple heuristic solutions with performance comparisons
  - Convergence analysis showing solution improvement over iterations


### **Tier 3**: Metaheuristic Algorithms — [`P7-Tier-3_executed.ipynb`](./P7-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Understand **population-based search** with Genetic Algorithms
  - Master **neighborhood search** with Simulated Annealing
- **Outputs**:
  - Genetic Algorithm solutions with convergence analysis
  - Simulated Annealing solutions with temperature schedules


### **Tier 4**: Advanced Optimization & Decision Intelligence — [`P7-Tier-4_executed.ipynb`](./P7-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Master **stochastic optimization** under uncertainty
  - Learn **robust optimization** for risk-averse decision making
- **Outputs**:
  - Stochastic programming solutions with scenario analysis
  - Robust optimization solutions with uncertainty sets


### **Tier 9**: The Quantum Leap (Computational Supremacy) — [`P7-Tier-9_executed.ipynb`](./P7-Tier-9_executed.ipynb)
- **Learning Goals**:
  - Quantum computing paradigm with QAOA implementation
  - Problem reformulated as QUBO (Quadratic Unconstrained Binary Optimization)


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 7)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
- **Problem 10**: The Dual-Cycling Quay Crane Problem
