# 09. The Quay Crane Scheduling Problem

## 📋 Problem Overview

At the Port of Rotterdam's Maasvlakte II terminal, the morning shift begins with the arrival of three ultra-large container vessels (ULCVs) simultaneously docking at adjacent berths. Each vessel carries between 18,000 to 22,000 twenty-foot equivalent units (TEUs), representing millions of euros in cargo value. The terminal operations center faces a critical challenge: how to optimally schedule the available quay cranes to minimize vessel turnaround time while ensuring operational safety and efficiency.

## 🎯 Solution Approaches

### **Tier 1**: Mixed-Integer Programming (made runnable via exhaustive search) — [`P9-Tier-1_executed.ipynb`](./P9-Tier-1_executed.ipynb)
- **Learning Goals**:
  - See how a QCSP-style instance can be written in code (bays, cranes, processing times).
  - Understand what the **makespan** is and how it depends on crane assignments and sequences.
- **Outputs**:
  - An optimal schedule for a small QCSP instance with 4 bays and 2 cranes.
  - A table showing, for each crane, which bays it processes and in which order.


### **Tier 2**: Classic Heuristic (Enhanced LPT) — [`P9-Tier-2_executed.ipynb`](./P9-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Understand why heuristics are needed for larger QCSP instances.
  - See how the **LPT rule** works: assign the most time-consuming bays first.
- **Outputs**:
  - A fast heuristic schedule for an 8-bay, 3-crane instance.
  - A table of crane assignments and per-crane completion times.


### **Tier 3**: Advanced Algorithm (Genetic Algorithm) — [`P9-Tier-3_executed.ipynb`](./P9-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Understand the **GA components** for QCSP: chromosome representation, fitness, crossover, mutation.
  - See how a population of schedules can be **evolved** over generations.
- **Outputs**:
  - A best-found schedule for a 10-bay, 3-crane instance using GA.
  - A **convergence plot** (best makespan vs generation).


### **Tier 4**: AI/ML/RL Augmentation (Deep Reinforcement Learning) — [`P9-Tier-4_executed.ipynb`](./P9-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Understand how to formulate QCSP as a **Markov Decision Process (MDP)**.
  - See how to define **state, action, and reward** for crane scheduling.
- **Outputs**:
  - A learned dispatching policy for an 8-bay, 3-crane instance using Q-learning.
  - An **episode vs reward** plot showing learning progress.


### **Tier 5**: Integrated Digital Twin (System-of-Systems Simulation) — [`P9-Tier-5_executed.ipynb`](./P9-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Understand the architecture of a **terminal Digital Twin** (data streams, modules, synchronization).
  - See how to model **interconnected subsystems** (quay cranes, yard cranes, vessels, trucks).
- **Outputs**:
  - A 7-day Digital Twin simulation for a terminal with 6 quay cranes, 2 vessels, and integrated yard operations.
  - **Baseline vs AI-optimized** schedules with system-wide KPIs.


### **Tier 6**: Autonomous & Self-Optimizing Ecosystem (Multi-Agent System) — [`P9-Tier-6_executed.ipynb`](./P9-Tier-6_executed.ipynb)
- **Learning Goals**:
  - Understand how to model terminal components as **autonomous agents** with local objectives.
  - Learn **auction-based task allocation** and **game-theoretic payoff functions**.
- **Outputs**:
  - A 3-vessel, 12-crane, 8-yard-block multi-agent simulation.
  - **Auction logs** showing bids, winners, and task allocations.


### **Tier 9**: The Quantum Leap (Quantum Approximate Optimization Algorithm) — [`P9-Tier-9_executed.ipynb`](./P9-Tier-9_executed.ipynb)
- **Learning Goals**:
  - Understand how to encode QCSP as a **QUBO** with binary variables.
  - Learn the **QAOA** structure: alternating cost and mixer Hamiltonians.
- **Outputs**:
  - A QUBO formulation for a 4-crane, 8-bay QCSP instance.
  - A **classical QAOA simulation** (using numpy) that finds a near-optimal schedule.


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 9)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 7**: The Static Berth Allocation Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 10**: The Dual-Cycling Quay Crane Problem
- **Problem 28**: The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)
