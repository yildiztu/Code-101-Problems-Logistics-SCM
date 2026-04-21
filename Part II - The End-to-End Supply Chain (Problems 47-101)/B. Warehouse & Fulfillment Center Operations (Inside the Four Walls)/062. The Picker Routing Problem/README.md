# 62. The Picker Routing Problem

## 📋 Problem Overview

Consider a modern e-commerce fulfillment center with thousands of storage locations organized in a rectangular grid of parallel aisles. A picker receives an order containing multiple items scattered throughout the warehouse and must determine the most efficient path to collect all items and return to the depot. The warehouse layout consists of parallel picking aisles connected by cross-aisles, creating a network where the picker can change aisles only at intersection points.

## 🎯 Solution Approaches

### **Tier 1**: Markov Decision Process Formulation — [`P62-Tier-1_executed.ipynb`](./P62-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Warehouse layout with defined distance matrix between locations
  - Picker starts and ends at depot location (0)


### **Tier 2**: Divide and Conquer Heuristic — [`P62-Tier-2_executed.ipynb`](./P62-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Warehouse can be naturally partitioned into smaller sections
  - Items are distributed across multiple warehouse regions


### **Tier 3**: Firefly Algorithm Implementation — [`P62-Tier-3_executed.ipynb`](./P62-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Firefly brightness is inversely proportional to route distance
  - Brighter fireflies (shorter routes) attract dimmer ones


### **Tier 4**: Imitation Learning Approach — [`P62-Tier-4_executed.ipynb`](./P62-Tier-4_executed.ipynb)
- **Learning Goals**:
  - Expert demonstrations are available for training
  - Warehouse state can be represented as feature vectors


### **Tier 5**: Integrated Digital Twin — [`P62-Tier-5_executed.ipynb`](./P62-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Real-time synchronization between physical and virtual warehouse
  - IoT sensors provide continuous picker and inventory data


### **Tier 9** — [`P62-Tier-9_executed.ipynb`](./P62-Tier-9_executed.ipynb)
- **Learning Goals**:
  - represents the cutting edge of computational optimization:
  - - **Quantum Speedup**: Theoretical √n! speedup vs exponential complexity


## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 62)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 59**: The Warehouse Layout Design Problem
- **Problem 60**: The Warehouse Slotting Optimization Problem
- **Problem 61**: The Order Batching Problem
