# 54. The Production Order Quantity (POQ) Problem

## 📋 Problem Overview

Manufacturing companies face a fundamental challenge: determining the optimal batch size for production runs that minimizes total costs while meeting customer demand. Unlike traditional inventory ordering where products arrive instantaneously, production involves a continuous process where items are manufactured at a specific rate over time. This creates a unique inventory buildup pattern that requires specialized optimization approaches.

Consider a pharmaceutical company producing tablets for a popular medication. The production line can manufacture 500 tablets per day, but daily demand is only 200 tablets. The company incurs setup costs of \$800 each time they start a production run, and holding costs of \$2 per tablet per year. The annual demand is 60,000 tablets. The critical question becomes: what production batch size minimizes the total cost of setup and inventory holding while ensuring continuous supply?

## 🎯 Solution Approaches

### **Tier 1**: The Pen \& Paper Method — [`P54-Tier-1_executed.ipynb`](./P54-Tier-1_executed.ipynb)
- Implements The Pen \& Paper Method

### **Tier 2**: The Classic Heuristic — [`P54-Tier-2_executed.ipynb`](./P54-Tier-2_executed.ipynb)
- Implements The Classic Heuristic

### **Tier 3**: The Advanced Algorithm — [`P54-Tier-3_executed.ipynb`](./P54-Tier-3_executed.ipynb)
- Implements The Advanced Algorithm

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 54)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 51**: The Classic Economic Order Quantity (EOQ) Problem
- **Problem 52**: The EOQ with Quantity Discounts Problem
- **Problem 53**: The EOQ with Planned Shortages Problem
