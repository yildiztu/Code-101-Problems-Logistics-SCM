# 30. The Yard Pre-Marshalling for Exports Problem

## 📋 Problem Overview

At the bustling Port of Shanghai's export yard, containers destined for various global destinations are stacked in towering bays, each reaching heights of up to six tiers. These containers arrive with different departure schedules—some must be loaded onto vessels departing tomorrow, while others won't leave for weeks. The challenge emerges when containers with earlier departure dates (higher priority) are positioned below those with later departure dates (lower priority), creating what terminal operators call **mis-overlays**.

Consider Bay 7, where Container A (departing Monday) sits beneath Container B (departing Wednesday). When Monday arrives, the crane operator must first move Container B to access Container A, creating additional handling operations, increased vessel waiting times, and operational inefficiencies. These unnecessary moves can cascade across multiple containers, potentially doubling the total handling time.

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method (Network Flow Formulation) — [`P30-Tier-1-SOLUTION_executed.ipynb`](./P30-Tier-1-SOLUTION_executed.ipynb)
- Implements The Pen \& Paper Method (Network Flow Formulation)

### **Tier 1**: The Pen \& Paper Method (Network Flow Formulation) — [`P30-Tier-1_executed.ipynb`](./P30-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method (Network Flow Formulation)

### **Tier 2**: The Classic Heuristic (List Scheduling Algorithm) — [`P30-Tier-2-BACKUP_executed.ipynb`](./P30-Tier-2-BACKUP_executed.ipynb)
- Implements The Classic Heuristic (List Scheduling Algorithm)

### **Tier 2**: The Classic Heuristic (List Scheduling Algorithm) — [`P30-Tier-2-COMPLETE_executed.ipynb`](./P30-Tier-2-COMPLETE_executed.ipynb)
- Implements The Classic Heuristic (List Scheduling Algorithm)

### **Tier 2**: The Classic Heuristic (List Scheduling Algorithm) — [`P30-Tier-2-CORRECTED_executed.ipynb`](./P30-Tier-2-CORRECTED_executed.ipynb)
- Implements The Classic Heuristic (List Scheduling Algorithm)

### **Tier 2**: The Classic Heuristic (List Scheduling Algorithm) — [`P30-Tier-2_executed.ipynb`](./P30-Tier-2_executed.ipynb)
- Implements The Classic Heuristic (List Scheduling Algorithm)

### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P30-Tier-5_executed.ipynb`](./P30-Tier-5_executed.ipynb)
- Implements The Integrated Digital Twin (System-of-Systems Simulation)

### **Tier 9**: The Quantum Leap (Quantum Walk Algorithms) — [`P30-Tier-9_executed.ipynb`](./P30-Tier-9_executed.ipynb)
- Implements The Quantum Leap (Quantum Walk Algorithms)

## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 30)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 27**: The Integrated Berth & Crane Allocation Problem (BAP-QCAP)
- **Problem 28**: The Integrated Crane Assignment & Scheduling Problem (QCAP-QCSP)
- **Problem 29**: The Integrated Quay Crane & Yard Truck Scheduling Problem
