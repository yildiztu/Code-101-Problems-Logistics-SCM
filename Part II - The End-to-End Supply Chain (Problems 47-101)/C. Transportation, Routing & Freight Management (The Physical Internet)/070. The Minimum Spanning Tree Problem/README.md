# 70. The Minimum Spanning Tree Problem

## 📋 Problem Overview

GlobalLogistics Inc. is expanding its operations across a new geographic region consisting of eight major cities. The company needs to establish a distribution network that connects all cities while minimizing the total infrastructure investment cost. Each potential connection between cities has an associated cost based on distance, terrain difficulty, and regulatory requirements.

The cities are: Atlanta (A), Boston (B), Chicago (C), Denver (D), El Paso (E), Fresno (F), Houston (G), and Indianapolis (H). The cost matrix represents millions of dollars required to establish direct logistics corridors between city pairs.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P70-Tier-1_executed.ipynb`](./P70-Tier-1_executed.ipynb)
- **Learning Goals**:
  - We have 8 cities (vertices) that need to be connected
  - Each potential connection has an associated cost


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P70-Tier-2_executed.ipynb`](./P70-Tier-2_executed.ipynb)
- **Learning Goals**:
  - We can use greedy algorithms to find the optimal MST efficiently
  - Kruskal's algorithm with Union-Find data structure provides optimal solution


### **Tier 3**: The Advanced Algorithm (Genetic Algorithm Implementation) — [`P70-Tier-3_executed.ipynb`](./P70-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Genetic algorithms can explore the solution space effectively
  - Population-based evolution can find near-optimal solutions


## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 70)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 59**: The Warehouse Layout Design Problem
- **Problem 60**: The Warehouse Slotting Optimization Problem
- **Problem 61**: The Order Batching Problem
