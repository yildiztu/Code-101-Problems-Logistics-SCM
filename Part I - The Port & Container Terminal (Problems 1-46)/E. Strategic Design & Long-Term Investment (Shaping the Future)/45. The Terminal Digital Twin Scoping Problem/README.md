# 45. The Terminal Digital Twin Scoping Problem

## 📋 Problem Overview

Mediterranean Container Terminal (MCT) operates a 2.4 million TEU capacity facility with 8 berths, 42 quay cranes, 180 yard cranes, and a 156-hectare container storage area organized into 48 blocks. The port authority has allocated \$15 million over three years for digital twin implementation, recognizing that full terminal digitization would cost over \$50 million and take seven years to complete.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P45-Tier-1_executed.ipynb`](./P45-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each terminal component can be either included (1) or excluded (0) from the digital twin
  - Sensors must be placed to provide adequate coverage for selected components


### **Tier 2**: The Classic Heuristic (Greedy Value-Density Algorithm) — [`P45-Tier-2_executed.ipynb`](./P45-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Components can be ranked by their value-density (value divided by implementation cost)
  - Greedy selection provides good approximations for this class of knapsack-like problems


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P45-Tier-5_executed.ipynb`](./P45-Tier-5_executed.ipynb)
- **Learning Goals**:
  - Terminal operations exist as a complex adaptive system with cascading interdependencies
  - Subsystem twins can communicate and coordinate in real-time


### **Tier 7**: The Human-AI Symbiotic Partnership (The Centaur Model) — [`P45-Tier-7_executed.ipynb`](./P45-Tier-7_executed.ipynb)
- **Learning Goals**:
  - Optimal digital twin scoping requires both human wisdom and AI analytical power
  - Human operators provide contextual knowledge, strategic vision, and adaptive creativity


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 45)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 40**: The Port Capacity & Expansion Timing Problem
- **Problem 41**: The Terminal Concession Bidding Problem
- **Problem 42**: The Peak Energy Consumption & Load Shifting Problem
