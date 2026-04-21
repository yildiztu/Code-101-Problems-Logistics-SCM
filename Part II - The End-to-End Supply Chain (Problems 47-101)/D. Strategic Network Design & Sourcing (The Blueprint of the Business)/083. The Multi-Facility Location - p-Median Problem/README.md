# 83. The Multi-Facility Location: p-Median Problem

## 📋 Problem Overview

Consider a major e-commerce company planning to establish exactly 5 regional distribution centers across a network of 20 potential locations to serve 50 major metropolitan markets. Each potential facility location has different operational costs, while each customer market has specific demand volumes and geographic constraints. The challenge lies in selecting the optimal 5 locations that minimize the total demand-weighted transportation cost while ensuring each customer market is served by its nearest distribution center.

This scenario encapsulates the essence of the p-median problem: given a fixed number of facilities to locate, how do we position them to minimize the aggregate service cost across all customers? Unlike the uncapacitated facility location problem where the number of facilities is a decision variable, the p-median problem constrains us to locate exactly \(p\) facilities, making it particularly relevant for budget-constrained strategic planning scenarios.

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method (Dynamic Programming Formulation) — [`P83-Tier-1_executed.ipynb`](./P83-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method (Dynamic Programming Formulation)

### **Tier 2**: The Classic Heuristic (Improvement-Based Local Search) — [`P83-Tier-2_executed.ipynb`](./P83-Tier-2_executed.ipynb)
- Implements The Classic Heuristic (Improvement-Based Local Search)

### **Tier 3**: The Advanced Algorithm (Tabu Search Implementation) — [`P83-Tier-3_executed.ipynb`](./P83-Tier-3_executed.ipynb)
- Implements The Advanced Algorithm (Tabu Search Implementation)

### **Tier 4**: The AI/ML/RL Augmentation Method (Ensemble Learning Framework) — [`P83-Tier-4_executed.ipynb`](./P83-Tier-4_executed.ipynb)
- Implements The AI/ML/RL Augmentation Method (Ensemble Learning Framework)

### **Tier 9**: The Quantum Leap (Quadratic Unconstrained Binary Optimization) — [`P83-Tier-9_executed.ipynb`](./P83-Tier-9_executed.ipynb)
- Implements The Quantum Leap (Quadratic Unconstrained Binary Optimization)

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 83)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 82**: The Single Facility Location Problem (Center of Gravity)
- **Problem 84**: The Multi-Facility Location - p-Center Problem
- **Problem 85**: The Uncapacitated Facility Location Problem
