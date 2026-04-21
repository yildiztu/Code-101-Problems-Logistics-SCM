# 15. The Vessel Re-stow Problem (Transshipment)

## 📋 Problem Overview

At the Port of Singapore, the world's second-largest container transshipment hub, the mega-vessel EVER\_GIVEN\_2 arrives with 18,000 TEU capacity, carrying containers from multiple European origins destined for various Asian ports including Hong Kong, Shanghai, Busan, and Tokyo. The vessel's current stow configuration was optimized for the European loading sequence, but now requires comprehensive re-stowing to accommodate new containers being loaded in Singapore while ensuring optimal discharge sequences for the remaining Asian ports.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mixed-Integer Programming Formulation) — [`P15-Tier-1_executed.ipynb`](./P15-Tier-1_executed.ipynb)
- **Outputs**:
  - - **Total moves**: Determined by the optimization algorithm
  - **Total cost**: Calculated based on the number of moves


### **Tier 2**: The Classic Heuristic (Constructive Priority-Based Algorithm) — [`P15-Tier-2_executed.ipynb`](./P15-Tier-2_executed.ipynb)
- **Outputs**:
  - - **Computational efficiency**: O(n log n) complexity with sub-second execution times
  - **Solution quality**: Significant improvement over random assignment (48% reduction in moves)


### **Tier 3**: The Advanced Algorithm (Ant Colony Optimization) — [`P15-Tier-3_executed.ipynb`](./P15-Tier-3_executed.ipynb)
- **Outputs**:
  - - **Convergence behavior**: ACO showed steady improvement over iterations
  - **Solution quality**: Competitive with heuristic methods, potential for better solutions


### **Tier 4**: The AI/ML/RL Augmentation (Deep Reinforcement Learning) — [`P15-Tier-4_executed.ipynb`](./P15-Tier-4_executed.ipynb)
- **Outputs**:
  - - **Learning progression**: Clear improvement in episode rewards and reduction in container moves
  - **Policy convergence**: Agent learned to balance exploration and exploitation effectively


### **Tier 5**: The Integrated Digital Twin (System-of-Systems Simulation) — [`P15-Tier-5_executed.ipynb`](./P15-Tier-5_executed.ipynb)
- **Outputs**:
  - - **Real-time monitoring**: 500+ IoT sensors providing continuous vessel state data
  - **Predictive analytics**: Early detection of anomalies and optimization opportunities


### **Tier 7**: The Human-AI Symbiotic Partnership (The Centaur Model) — [`P15-Tier-7_executed.ipynb`](./P15-Tier-7_executed.ipynb)
- **Outputs**:
  - - **Partnership development**: Trust scores improved from initial 0.6-0.7 to 0.7-0.8 range
  - **Decision quality**: 92% quality score vs 78% (AI-only) and 82% (human-only)


### **Tier 9**: The Quantum Leap (Quantum Approximate Optimization Algorithm) — [`P15-Tier-9_executed.ipynb`](./P15-Tier-9_executed.ipynb)
- **Outputs**:
  - - **Quantum circuit implementation**: QAOA with depth 3 using 8 qubits for vessel re-stow optimization
  - **Convergence behavior**: Steady improvement in solution cost over 100 optimization iterations


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 15)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 7**: The Static Berth Allocation Problem
- **Problem 8**: The Quay Crane Assignment Problem
- **Problem 9**: The Quay Crane Scheduling Problem
