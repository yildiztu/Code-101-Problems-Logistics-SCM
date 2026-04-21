# 69. The Shortest Path Problem

## 📋 Problem Overview

GlobalLogistics Inc. operates a complex freight network spanning multiple transportation modes across North America. The company manages 15 major distribution hubs connected by various transportation links: truck routes, rail connections, air freight corridors, and intermodal facilities. Each connection has different associated costs including transportation time, fuel expenses, handling fees, and reliability factors.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P69-Tier-1_executed.ipynb`](./P69-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Network is represented as a directed graph G = (V, E)
  - Edge weights (costs/distances) are non-negative


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P69-Tier-2_executed.ipynb`](./P69-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Network edges have non-negative weights (required for Dijkstra's algorithm)
  - Priority queue implementation ensures efficient node selection


### **Tier 3**: The Advanced Algorithm (Metaheuristic Implementation) — [`P69-Tier-3_executed.ipynb`](./P69-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Complex shortest path problems with dynamic networks or multiple constraints
  - Traditional algorithms may be insufficient for large-scale or multi-objective problems


### **Tier 4**: The AI/ML/RL Augmentation Method — [`P69-Tier-4_executed.ipynb`](./P69-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Real-world routing involves uncertainty in travel times and costs
  - Historical data and current conditions can predict travel time distributions


## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 69)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 59**: The Warehouse Layout Design Problem
- **Problem 60**: The Warehouse Slotting Optimization Problem
- **Problem 61**: The Order Batching Problem
