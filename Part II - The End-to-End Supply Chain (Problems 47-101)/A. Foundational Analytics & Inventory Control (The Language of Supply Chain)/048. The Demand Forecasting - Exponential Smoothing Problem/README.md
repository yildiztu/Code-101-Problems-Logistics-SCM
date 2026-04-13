# 48. The Demand Forecasting - Exponential Smoothing Problem

## 📋 Problem Overview

PharmaDist manages pharmaceutical distribution for 300 independent pharmacies across the Midwest region. One critical product is insulin pens, with weekly demand averaging 4,200 units but showing high variability (standard deviation of 950 units) due to prescription patterns, seasonal illness trends, and insurance coverage cycles.

The current forecasting system uses a 4-week moving average, but this approach has proven too slow to respond to sudden demand shifts - particularly problematic for a life-critical medication where stockouts can have serious health consequences. Last quarter, the company experienced 8 stockout incidents, each affecting an average of 12 pharmacies and requiring expensive emergency shipments at 3x normal transportation costs.

The supply chain director has tasked the analytics team with implementing exponential smoothing methods that can better balance trend responsiveness with noise filtering. The team must determine optimal smoothing parameters (alpha for level, beta for trend) and decide whether to use simple, double, or triple exponential smoothing given the product's demand characteristics. Success will be measured by forecast accuracy (MAPE, MAD) and service level improvements.

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P48-Tier-1_executed.ipynb`](./P48-Tier-1_executed.ipynb)
- Derives simple, double, and triple exponential smoothing formulas
- Analyzes smoothing parameter selection (alpha, beta, gamma)
- Compares forecast accuracy across different methods

### **Tier 2**: Classic Heuristic — [`P48-Tier-2_executed.ipynb`](./P48-Tier-2_executed.ipynb)
- Implements Holt-Winters seasonal smoothing
- Develops adaptive smoothing parameter adjustment
- Evaluates performance on seasonal demand patterns

### **Tier 3**: Advanced Algorithm — [`P48-Tier-3_executed.ipynb`](./P48-Tier-3_executed.ipynb)
- Applies optimization to find optimal smoothing parameters
- Implements state-space models for exponential smoothing
- Develops robust forecasting with outlier detection

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 48)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 47**: The Demand Forecasting - Moving Average & Weighted MA Problem
- **Problem 49**: The Causal & Regression-Based Forecasting Problem
- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
- **Problem 56**: The Safety Stock & Reorder Point (Q,r) Policy Problem
