# 57. The Periodic Review (Base-Stock) Policy Problem

## 📋 Problem Overview

MedSupply Distribution operates a regional distribution center serving 150 hospitals across the southeastern United States. The company manages over 2,000 critical medical supply items, ranging from basic consumables like syringes and bandages to specialized equipment components. Due to supplier constraints and logistics efficiency requirements, MedSupply can only place orders with their primary suppliers on specific days of the week - typically Monday mornings for most suppliers.

The challenge lies in determining optimal inventory policies for each product category. Consider their high-volume syringe inventory: demand averages 12,000 units per week with a standard deviation of 2,400 units, following a roughly normal distribution. The supplier has a lead time of 0.5 weeks, and MedSupply aims to maintain a 95\% service level (stockout probability of 5\%). The company reviews inventory every Monday and must decide how many units to order to bring total inventory (on-hand plus on-order) up to the base-stock level.

## 🎯 Solution Approaches

### **Tier 1**: Newsvendor Model & Base-Stock Calculation — [`P57-Tier-1_executed.ipynb`](./P57-Tier-1_executed.ipynb)
- Derives optimal base-stock level using newsvendor framework
- Calculates safety stock for periodic review with lead time
- Analyzes service level vs. cost trade-offs

### **Tier 2**: Simulation-Based Policy Evaluation — [`P57-Tier-2_executed.ipynb`](./P57-Tier-2_executed.ipynb)
- Simulates periodic review system with stochastic demand
- Evaluates policy performance across multiple scenarios
- Compares base-stock policies with different review periods

### **Tier 3**: Dynamic Programming Optimization — [`P57-Tier-3_executed.ipynb`](./P57-Tier-3_executed.ipynb)
- Formulates multi-period inventory problem as DP
- Computes optimal ordering policies under uncertainty
- Analyzes state-dependent base-stock levels

### **Tier 4**: Machine Learning for Demand Patterns — [`P57-Tier-4_executed.ipynb`](./P57-Tier-4_executed.ipynb)
- Applies ML to identify demand patterns and seasonality
- Implements adaptive base-stock policies with learning
- Develops predictive models for lead time variability

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 57)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
- **Problem 52**: The EOQ with Quantity Discounts Problem
- **Problem 53**: The EOQ with Planned Shortages Problem
