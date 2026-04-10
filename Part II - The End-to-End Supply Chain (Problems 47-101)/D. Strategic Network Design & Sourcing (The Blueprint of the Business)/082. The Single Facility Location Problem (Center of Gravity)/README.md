# 082. The Single Facility Location Problem (Center of Gravity)

## 📋 Problem Overview

MegaCorp, a major consumer electronics retailer, operates five retail stores across a metropolitan area and needs to establish a new distribution center to serve all locations efficiently. Each store has different weekly demand volumes, and the company wants to minimize the total transportation cost by optimizing the distribution center's location. The stores are located at coordinates (2,3), (8,1), (6,7), (12,4), and (4,9) with weekly demands of 150, 200, 180, 160, and 110 units respectively. Transportation cost is directly proportional to both distance and demand volume, making this a classic weighted facility location problem where the optimal position minimizes the sum of weighted distances to all demand points.

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method (Mathematical Formulation) — [`P82-Tier-1_executed.ipynb`](./P82-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method (Mathematical Formulation)

### **Tier 2**: The Classic Heuristic (Geometric Iterative Refinement) — [`P82-Tier-2_executed.ipynb`](./P82-Tier-2_executed.ipynb)
- Implements The Classic Heuristic (Geometric Iterative Refinement)

### **Tier 3**: The Advanced Algorithm (Particle Swarm Optimization) — [`P82-Tier-3_executed.ipynb`](./P82-Tier-3_executed.ipynb)
- Implements The Advanced Algorithm (Particle Swarm Optimization)

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 82)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 83**: The Multi-Facility Location - p-Median Problem
- **Problem 84**: The Multi-Facility Location - p-Center Problem
- **Problem 85**: The Uncapacitated Facility Location Problem
