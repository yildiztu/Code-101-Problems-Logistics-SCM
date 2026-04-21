# 80. The International Freight Mode Selection Problem (Air vs. Ocean)

## 📋 Problem Overview

GlobalTech manufactures consumer electronics in Shenzhen, China, and distributes to retail partners across North America and Europe. The logistics team faces a critical recurring decision: which transportation mode to use for shipping 40-foot containers of smartphones from Shenzhen to Los Angeles?

**Ocean Freight Option**: 18-day transit time, $3,200 per container, high reliability (98% on-time), but requires 3-week advance booking and offers limited flexibility for rush orders.

**Air Freight Option**: 2-day transit time, $18,500 per container equivalent, moderate reliability (92% on-time due to weather/capacity constraints), can be booked with 48-hour notice.

Each container holds products valued at $2.8 million (wholesale). The finance team estimates inventory carrying costs at 25% annually, meaning each day in transit costs approximately $1,918 in tied-up capital. However, faster delivery enables higher product availability, reducing stockout risk during peak demand periods.

The challenge extends beyond simple cost comparison. The team must consider: demand variability and forecast accuracy, product lifecycle (smartphones depreciate 2% per week), seasonal peaks, customer service level commitments, and the option value of maintaining flexibility. Should they use a single mode consistently, or develop a hybrid strategy based on product characteristics and market conditions?

## 🎯 Solution Approaches

### **Tier 1**: Mathematical Formulation — [`P80-Tier-1_executed.ipynb`](./P80-Tier-1_executed.ipynb)
- Formulates mode selection as cost-service trade-off optimization
- Models inventory carrying costs and transit time impacts
- Analyzes total landed cost for air vs. ocean freight

### **Tier 2**: Classic Heuristic — [`P80-Tier-2_executed.ipynb`](./P80-Tier-2_executed.ipynb)
- Implements decision rules based on product value and urgency
- Develops threshold-based mode selection criteria
- Evaluates hybrid strategies for different product categories

### **Tier 3**: Genetic Algorithm — [`P80-Tier-3_executed.ipynb`](./P80-Tier-3_executed.ipynb)
- Population-based metaheuristic for global optimization
- Discovers non-intuitive optimal shipment patterns
- Analyzes convergence and solution quality vs heuristics

### **Tier 4**: Reinforcement Learning — [`P80-Tier-4_executed.ipynb`](./P80-Tier-4_executed.ipynb)
- Deep Q-learning for adaptive policy development
- Learns from market disruptions and volatility patterns
- Enables dynamic decision-making under uncertainty

### **Tier 5**: Digital Twin — [`P80-Tier-5_executed.ipynb`](./P80-Tier-5_executed.ipynb)
- Real-time IoT integration with 2.3M daily data points
- Predictive analytics for disruption forecasting
- Scenario testing and what-if analysis capabilities

### **Tier 7**: Human-AI Partnership — [`P80-Tier-7_executed.ipynb`](./P80-Tier-7_executed.ipynb)
- Symbiotic collaboration between experts and AI systems
- Explainable AI with transparent reasoning processes
- Trust development and learning from human feedback

### **Tier 8**: Ethical Framework — [`P80-Tier-8_executed.ipynb`](./P80-Tier-8_executed.ipynb)
- Multi-stakeholder utility optimization
- Environmental and social impact assessment
- Constitutional AI with ethical constraint compliance

## 📚 Resources

- **Source Book**: [Part II - The End-to-End Supply Chain](https://www.amazon.com/dp/B0FV89XJZ5) (Problem 80)
- **Video Tutorial**: [IntelliBoost YouTube - Part II Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZrSfjIOvYVg8fLeajqjNn-z)
- **Jupyter Notebooks**: All tiers available in this directory

## 🔗 Related Problems

- **Problem 71**: The Classic Vehicle Routing Problem (VRP)
- **Problem 78**: The Freight Consolidation & LTL Optimization Problem
- **Problem 79**: The Intermodal Transportation Problem
- **Problem 82**: The Single Facility Location Problem (Center of Gravity)
