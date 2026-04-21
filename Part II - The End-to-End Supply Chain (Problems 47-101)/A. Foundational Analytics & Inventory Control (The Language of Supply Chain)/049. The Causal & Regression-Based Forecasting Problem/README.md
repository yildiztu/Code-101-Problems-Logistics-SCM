# 49. The Causal \& Regression-Based Forecasting Problem

## 📋 Problem Overview

The Port of Singapore handles over 37 million TEU annually, making accurate throughput forecasting critical for resource allocation, staffing decisions, and infrastructure planning. Traditional time-series forecasting methods rely solely on historical patterns, treating external factors as unexplainable noise. However, port throughput is fundamentally driven by identifiable causal factors: global trade volumes, shipping schedules, economic indicators, seasonal patterns, fuel prices, and geopolitical events.

Consider the challenge facing the port operations team: they must forecast monthly container throughput for the next 12 months to optimize crane scheduling, yard space allocation, and workforce planning. Historical data shows significant variation that cannot be explained by simple seasonal patterns alone. During 2019, throughput dropped 15\% in Q4 due to trade tensions, while 2020 saw unprecedented volatility due to supply chain disruptions. Meanwhile, 2021-2022 experienced record highs driven by e-commerce growth and supply chain restocking.

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method (Multiple Linear Regression Formulation) — [`P49-Tier-1_executed.ipynb`](./P49-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method (Multiple Linear Regression Formulation)

### **Tier 2**: The Classic Heuristic (Stepwise Regression Builder) — [`P49-Tier-2_executed.ipynb`](./P49-Tier-2_executed.ipynb)
- Implements The Classic Heuristic (Stepwise Regression Builder)

### **Tier 3**: The Advanced Algorithm (Genetic Algorithm for Multivariate Model Selection) — [`P49-Tier-3_executed.ipynb`](./P49-Tier-3_executed.ipynb)
- Implements The Advanced Algorithm (Genetic Algorithm for Multivariate Model Selection)

### **Tier 4**: The AI/ML/RL Augmentation Method (Deep Ensemble Forecasting) — [`P49-Tier-4_executed.ipynb`](./P49-Tier-4_executed.ipynb)
- Implements The AI/ML/RL Augmentation Method (Deep Ensemble Forecasting)

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 49)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 47**: The Demand Forecasting - Moving Average & Weighted MA Problem
- **Problem 48**: The Demand Forecasting - Exponential Smoothing Problem
- **Problem 50**: The New Product Forecasting Problem
