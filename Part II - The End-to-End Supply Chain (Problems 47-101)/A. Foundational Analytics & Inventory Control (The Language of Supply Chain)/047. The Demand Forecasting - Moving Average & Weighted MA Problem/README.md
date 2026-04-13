# 47. The Demand Forecasting - Moving Average & Weighted MA Problem

## 📋 Problem Overview

RetailCo operates a nationwide chain of 500 stores selling consumer electronics. The demand planning team needs to forecast weekly sales for a popular smartphone model to optimize inventory levels across their distribution network. Historical sales data shows significant variability: weekly demand ranges from 2,000 to 8,500 units, with clear seasonal patterns around holidays and product launch cycles.

The company currently uses simple intuition-based ordering, leading to frequent stockouts during peak periods and excess inventory during slow periods. The CFO estimates that each stockout costs $150 in lost margin and customer goodwill, while each unit of excess inventory costs $8 per week in holding costs. With 52 weeks of historical sales data available, the analytics team must develop a systematic forecasting approach.

The challenge is to balance responsiveness to recent demand trends with stability against random fluctuations. Moving average methods offer simplicity and interpretability, but the team must determine: How many periods should be included in the average? Should recent periods be weighted more heavily? How can forecast accuracy be measured and improved over time?

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P47-Tier-1_executed.ipynb`](./P47-Tier-1_executed.ipynb)
- Derives simple moving average (SMA) and weighted moving average (WMA) formulas
- Analyzes forecast error metrics (MAD, MSE, MAPE)
- Compares different window sizes and weighting schemes

### **Tier 2**: Classic Heuristic — [`P47-Tier-2_executed.ipynb`](./P47-Tier-2_executed.ipynb)
- Implements adaptive window selection heuristic
- Develops rules for choosing optimal averaging periods
- Evaluates performance across different demand patterns

### **Tier 3**: Advanced Algorithm — [`P47-Tier-3_executed.ipynb`](./P47-Tier-3_executed.ipynb)
- Applies optimization to determine optimal weights
- Implements cross-validation for parameter tuning
- Develops ensemble forecasting with multiple averages

### **Tier 4**: AI/ML Augmentation — [`P47-Tier-4_executed.ipynb`](./P47-Tier-4_executed.ipynb)
- Uses neural networks to learn optimal weighting patterns
- Implements time series decomposition with ML
- Develops hybrid models combining classical and ML approaches

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 47)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 48**: The Demand Forecasting - Exponential Smoothing Problem
- **Problem 49**: The Causal & Regression-Based Forecasting Problem
- **Problem 50**: The New Product Forecasting Problem
- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
