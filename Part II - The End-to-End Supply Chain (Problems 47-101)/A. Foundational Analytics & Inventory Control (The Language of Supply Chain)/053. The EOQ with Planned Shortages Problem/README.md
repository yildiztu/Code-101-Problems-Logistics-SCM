# 53. The EOQ with Planned Shortages Problem

## 📋 Problem Overview

In the highly competitive landscape of modern supply chain management, the traditional Economic Order Quantity (EOQ) model's assumption of zero stockouts often proves too restrictive and economically suboptimal. The Meridian Electronics Distribution Center faces this exact challenge while managing semiconductor components for major technology manufacturers.

The distribution center supplies critical microprocessors with an annual demand of 36,000 units, experiencing significant seasonal fluctuations and supply chain uncertainties. While the traditional EOQ model would require maintaining sufficient inventory to never experience stockouts, Meridian has discovered that their customers are increasingly willing to accept planned shortages in exchange for lower overall costs, particularly for non-critical components with predictable delivery windows.

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method (Mixed-Integer Programming Formulation) — [`P53-Tier-1_executed.ipynb`](./P53-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method (Mixed-Integer Programming Formulation)

### **Tier 2**: The Classic Heuristic (Greedy Construction Algorithm) — [`P53-Tier-2_executed.ipynb`](./P53-Tier-2_executed.ipynb)
- Implements The Classic Heuristic (Greedy Construction Algorithm)

### **Tier 3**: The Advanced Algorithm (Simulated Annealing Metaheuristic) — [`P53-Tier-3_executed.ipynb`](./P53-Tier-3_executed.ipynb)
- Implements The Advanced Algorithm (Simulated Annealing Metaheuristic)

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 53)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
- **Problem 52**: The EOQ with Quantity Discounts Problem
- **Problem 54**: The Production Order Quantity (POQ) Problem
