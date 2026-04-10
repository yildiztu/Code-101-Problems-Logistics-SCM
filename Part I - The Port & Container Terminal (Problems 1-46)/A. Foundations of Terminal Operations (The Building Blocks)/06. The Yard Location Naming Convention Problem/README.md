# 06. The Yard Location Naming Convention Problem

## 📋 Problem Overview

Pacific Gateway Terminal operates a 45-hectare container yard handling over 2.5 million TEUs annually. The facility contains 8,500 ground storage positions organized across 12 blocks, each with varying numbers of rows, bays, and tiers. Currently, the terminal uses an inconsistent naming system where different areas employ different conventions: Block A uses alphanumeric codes like ``A7-15-3'', Block B uses sequential numbers like ``2847'', while the newest expansion area uses GPS coordinates.

## 🎯 Solution Approaches

### **Tier 1**: The Pen & Paper Method (Mathematical Formulation) — [`P6-Tier-1_executed.ipynb`](./P6-Tier-1_executed.ipynb)
- **Learning Goals**:
  - Each physical location must have a unique identifier
  - Identifiers should be concise and easy to read


### **Tier 2**: The Classic Heuristic (Python Implementation) — [`P6-Tier-2_executed.ipynb`](./P6-Tier-2_executed.ipynb)
- **Learning Goals**:
  - Greedy choices at each level lead to globally acceptable solutions
  - Hierarchical structure (Block → Row → Position → Tier) is optimal for human comprehension


### **Tier 3**: The Advanced Algorithm (Metaheuristic Implementation) — [`P6-Tier-3_executed.ipynb`](./P6-Tier-3_executed.ipynb)
- **Learning Goals**:
  - Evolutionary computation can find near-optimal solutions to complex naming problems
  - Multiple conflicting objectives can be balanced through weighted fitness functions


## 📚 Resources

- **Source Book**: [Part I - The Port & Container Terminal](https://www.amazon.com/dp/B0FV7ZK9D5) (Problem 6)
- **Video Tutorial**: [IntelliBoost YouTube - Part I Course](https://www.youtube.com/playlist?list=PL6O8rFz-5oZq3HSNoYg_nruGbDq1lUNfu)
- **Jupyter Notebooks**: All tiers available in this directory


## 🔗 Related Problems

- **Problem 1**: The Single Crane Lift Sequence Problem
- **Problem 2**: The Container Stacking Rules Problem
- **Problem 3**: The Manual Reefer Monitoring Problem
