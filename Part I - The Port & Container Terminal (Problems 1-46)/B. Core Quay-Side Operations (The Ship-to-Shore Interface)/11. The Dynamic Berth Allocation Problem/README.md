# 11. The Dynamic Berth Allocation Problem

## 📋 Problem Overview

Port Metropolis handles over 2,000 vessel calls annually across its 12 discrete berths, with vessels ranging from 1,000 TEU feeders to 24,000 TEU ultra-large container vessels (ULCVs). The terminal operates under dynamic conditions where vessel arrivals are subject to weather delays, port congestion at previous stops, and schedule adjustments. Each berth has different specifications: Berths 1-3 accommodate vessels up to 8,000 TEU with 3 quay cranes each, Berths 4-8 handle mid-size vessels up to 15,000 TEU with 4-5 cranes, and Berths 9-12 are dedicated to ULCVs with 6-8 high-productivity cranes each.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P11-Tier-1_executed.ipynb`](./P11-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Vessel arrival times are known in advance
  - Each berth can handle only one vessel at a time


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P11-Tier-2_executed.ipynb`](./P11-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Vessel arrival times and deadlines are known
  - Processing times vary by vessel-berth combination


### **Tier 3**: The Advanced Algorithm (Genetic Algorithm Implementation) — [`P11-Tier-3_executed.ipynb`](./P11-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Solutions can be encoded as chromosomes (e.g., permutation of vessels)
  - Evolution (selection, crossover, mutation) improves solution quality over generations


### **Tier 4**: The AI/ML/RL Augmentation Method — [`P11-Tier-4_executed.ipynb`](./P11-Tier-4_executed.ipynb)
- **Learning Goals**:
  - The problem can be modeled as a Markov Decision Process (MDP)
  - State captures system status (vessel queue, berth availability)


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P11-Tier-5_executed.ipynb`](./P11-Tier-5_executed.ipynb)
- **Learning Goals**:
  - The port system is dynamic and subject to uncertainty (weather, delays)
  - Multiple subsystems interact (berths, cranes, yard)


### **Tier 7**: Human-AI Symbiotic Partnership (The Centaur Model) — [`P11-Tier-7_executed.ipynb`](./P11-Tier-7_executed.ipynb)
- **Learning Goals**:
  - Human operators provide contextual knowledge and strategic oversight
  - AI systems deliver computational optimization and pattern recognition


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 11)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 7**: The Static Berth Allocation Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
