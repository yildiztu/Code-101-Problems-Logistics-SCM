# 56. The Safety Stock & Reorder Point (Q,r) Policy Problem

## 📋 Problem Overview

AutoParts Plus operates a regional distribution center supplying 85 automotive repair shops with replacement parts. One high-volume item is brake pad sets, with daily demand averaging 180 units (standard deviation of 45 units) following a roughly normal distribution. The supplier, located 800 miles away, has a lead time of 3 days with occasional delays extending to 5 days during peak shipping seasons.

Currently, the warehouse manager uses intuition-based reordering: "Order 2,000 units when inventory looks low." This informal approach has led to problems - last month saw 4 stockout incidents (each costing $250 in expedited shipping and lost customer goodwill) and average inventory of 1,200 units (holding cost of $2.50 per unit per year).

The operations director wants to implement a systematic (Q,r) policy: order a fixed quantity Q whenever inventory position drops to reorder point r. The challenge is determining optimal values that minimize total costs (ordering costs of $75 per order, holding costs, and stockout costs) while maintaining a 95% service level. The team must account for demand variability during lead time and decide whether to use continuous or periodic review.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P56-Tier-1_executed.ipynb`](./P56-Tier-1_executed.ipynb)
- Derives optimal (Q,r) policy using newsvendor model
- Calculates reorder point with lead time demand uncertainty
- Analyzes total cost minimization (ordering + holding + stockout)

### **Tier 2**: Classic Heuristic — [`P56-Tier-2_executed.ipynb`](./P56-Tier-2_executed.ipynb)
- Implements EOQ-based order quantity with safety stock
- Develops service level-driven reorder point calculation
- Evaluates continuous vs. periodic review policies

### **Tier 3**: Advanced Algorithm — [`P56-Tier-3_executed.ipynb`](./P56-Tier-3_executed.ipynb)
- Applies stochastic optimization for (Q,r) determination
- Implements simulation-based policy evaluation
- Develops adaptive policies with demand learning

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 56)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
- **Problem 52**: The EOQ with Quantity Discounts Problem
- **Problem 53**: The EOQ with Planned Shortages Problem
- **Problem 57**: The Periodic Review (Base-Stock) Policy Problem
