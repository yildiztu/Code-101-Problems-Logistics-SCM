# 23. The AGV Dispatching & Battery Management Problem

## 📋 Problem Overview

At the Port of Rotterdam's automated container terminal, a fleet of 25 Automated Guided Vehicles (AGVs) operates 24/7 to transport containers between quay cranes and yard stacks. Each AGV has a battery capacity of 100 kWh, consuming approximately 0.8 kWh per kilometer traveled. The terminal features 6 strategically placed charging stations, each capable of charging 4 AGVs simultaneously.

During peak operations, the terminal handles up to 180 container moves per hour across 8 active quay cranes. Each transport task has a pickup location (quay crane), delivery location (yard block), priority level (based on vessel departure times), and time window constraints. AGVs must be dispatched efficiently while ensuring they never run out of battery during a task, requiring intelligent routing to charging stations when battery levels drop below safety thresholds.

The challenge is to minimize total travel distance, reduce waiting times at both pickup and delivery points, and maintain high AGV availability through smart battery management - all while respecting the physical constraints of the terminal layout and the operational requirements of vessel loading/unloading schedules.

## 🎯 Solution Approaches

### **Tier 1**: Vehicle Routing Formulation (Mathematical Model) — [`P23-Tier-1_executed.ipynb`](./P23-Tier-1_executed.ipynb)
- Implements Vehicle Routing Formulation (Mathematical Model)

### **Tier 2**: Battery-Aware Cheapest Insertion Heuristic — [`P23-Tier-2_executed.ipynb`](./P23-Tier-2_executed.ipynb)
- Implements Battery-Aware Cheapest Insertion Heuristic

### **Tier 3**: Ant Colony Optimization — [`P23-Tier-3-BACKUP_executed.ipynb`](./P23-Tier-3-BACKUP_executed.ipynb)
- Implements Ant Colony Optimization

### **Tier 4**: Deep Reinforcement Learning — [`P23-Tier-4_executed.ipynb`](./P23-Tier-4_executed.ipynb)
- Implements Deep Reinforcement Learning

### **Tier 5**: Digital Twin Simulation — [`P23-Tier-5_executed.ipynb`](./P23-Tier-5_executed.ipynb)
- Implements Digital Twin Simulation

### **Tier 6**: Multi-Agent System — [`P23-Tier-6_executed.ipynb`](./P23-Tier-6_executed.ipynb)
- Implements Multi-Agent System

### **Tier 7**: Advanced Metaheuristics — [`P23-Tier-7_executed.ipynb`](./P23-Tier-7_executed.ipynb)
- Implements Advanced Metaheuristics

### **Tier 8**: Hybrid Optimization — [`P23-Tier-8_executed.ipynb`](./P23-Tier-8_executed.ipynb)
- Implements Hybrid Optimization

### **Tier 9**: Quantum Computing — [`P23-Tier-9_executed.ipynb`](./P23-Tier-9_executed.ipynb)
- Implements Quantum Computing

## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 23)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 16**: The Storage Location Assignment Problem (SLAP)
- **Problem 18**: The Yard Crane (RTG/RMG) Scheduling Problem
- **Problem 22**: The Internal Vehicle (Terminal Truck) Dispatching Problem
- **Problem 27**: The Integrated Berth & Crane Allocation Problem (BAP-QCAP)
