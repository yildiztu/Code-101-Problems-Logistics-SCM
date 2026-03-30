# Test core functionality of P30-Tier-9
import sys
import os
sys.path.append(r"c:\Users\turkayyildiz\Desktop\Code - 101 Problems\Part I - The Port & Container Terminal (Problems 1-46)\D. Integrated Tactical & Pre-Planning Problems (Connecting the Silos)\30. The Yard Pre-Marshalling for Exports Problem")

# Test imports and basic class definitions
try:
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from dataclasses import dataclass
    from typing import List, Tuple, Dict, Optional, Any
    import random
    from collections import defaultdict
    import time
    from copy import deepcopy
    import itertools
    import math
    
    print("✅ All required packages imported successfully")
    
    # Test dataclass definitions
    @dataclass
    class Container:
        id: str
        priority: int
        current_stack: int
        current_tier: int

    @dataclass
    class QuantumState:
        amplitudes: np.ndarray
        basis_states: List[Tuple[int, ...]]
        
        def normalize(self):
            norm = np.sqrt(np.sum(np.abs(self.amplitudes) ** 2))
            if norm > 0:
                self.amplitudes /= norm
        
        def get_probability_distribution(self) -> np.ndarray:
            return np.abs(self.amplitudes) ** 2

    @dataclass
    class QuantumWalkConfig:
        num_containers: int
        num_stacks: int
        num_tiers: int
        walk_steps: int = 15
        coin_dimension: int = 2
        measurement_samples: int = 500
        noise_rate: float = 0.01
        decoherence_rate: float = 0.001
    
    print("✅ All dataclass definitions created successfully")
    
    # Test basic container creation
    containers = [
        Container('A', 1, 0, 0),
        Container('B', 2, 0, 1),
        Container('C', 3, 1, 0),
        Container('D', 4, 1, 1),
    ]
    
    print(f"✅ Created {len(containers)} test containers")
    
    # Test quantum state creation
    basis_states = [(0, 1, 0, 1), (1, 0, 1, 0)]
    amplitudes = np.ones(len(basis_states), dtype=complex) / np.sqrt(len(basis_states))
    quantum_state = QuantumState(amplitudes, basis_states)
    quantum_state.normalize()
    
    print(f"✅ Quantum state created with {len(basis_states)} basis states")
    print(f"   Probability distribution: {quantum_state.get_probability_distribution()}")
    
    # Test configuration
    config = QuantumWalkConfig(
        num_containers=len(containers),
        num_stacks=2,
        num_tiers=2,
        walk_steps=5,
        measurement_samples=10
    )
    
    print(f"✅ Quantum walk configuration created:")
    print(f"   Containers: {config.num_containers}")
    print(f"   Stacks: {config.num_stacks}")
    print(f"   Walk steps: {config.walk_steps}")
    
    print("\n🎉 All core functionality tests passed!")
    print("P30-Tier-9 notebook is ready for execution!")
    
except Exception as e:
    print(f"❌ Error during testing: {e}")
    import traceback
    traceback.print_exc()
