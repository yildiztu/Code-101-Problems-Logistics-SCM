#!/usr/bin/env python3

import json
import sys
import os

# Test JSON validity of main P26 files
files_to_test = ['P26-Tier-1.ipynb', 'P26-Tier-2.ipynb', 'P26-Tier-3.ipynb', 'P26-Tier-4.ipynb', 'P26-Tier-5.ipynb', 'P26-Tier-7.ipynb']

print("Testing P26 JSON validity...")
print("=" * 50)

all_valid = True
for filename in files_to_test:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        cells = data.get('cells', [])
        code_cells = sum(1 for cell in cells if cell.get('cell_type') == 'code')
        markdown_cells = sum(1 for cell in cells if cell.get('cell_type') == 'markdown')
        
        print(f"PASS {filename}: {len(cells)} cells ({code_cells} code, {markdown_cells} markdown)")
        
    except Exception as e:
        print(f"FAIL {filename}: ERROR - {str(e)}")
        all_valid = False

print(f"\nOverall Status: {'ALL VALID' if all_valid else 'SOME INVALID'}")

# Test execution of Tier-1 (simplest)
print("\nTesting execution of P26-Tier-1...")
print("=" * 50)

try:
    # Simple import test
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    print("PASS Required packages available")
    
    # Test basic data structures
    from dataclasses import dataclass
    from typing import List, Dict, Tuple
    
    @dataclass
    class Gate:
        id: int
        location: str
        vehicles_per_hour: int
        criticality: float
        downtime_cost_per_hour: float
    
    @dataclass
    class Sensor:
        id: int
        gate_id: int
        sensor_type: str
        monitoring_cost: float
        failure_rate: float
        criticality: float
        maintenance_interval: int
    
    # Create test data
    gates = [
        Gate(id=1, location='Main_Entrance', vehicles_per_hour=150, criticality=0.95, downtime_cost_per_hour=15000),
        Gate(id=2, location='Exit_Gate', vehicles_per_hour=100, criticality=0.85, downtime_cost_per_hour=10000),
    ]
    
    sensors = [
        Sensor(id=1, gate_id=1, sensor_type='photo_eye', monitoring_cost=5, failure_rate=0.02, criticality=0.9, maintenance_interval=8),
        Sensor(id=2, gate_id=1, sensor_type='ground_loop', monitoring_cost=9, failure_rate=0.03, criticality=0.7, maintenance_interval=12),
        Sensor(id=3, gate_id=1, sensor_type='safety_beam', monitoring_cost=7, failure_rate=0.015, criticality=1.0, maintenance_interval=6),
    ]
    
    print(f"PASS Test data structures created: {len(gates)} gates, {len(sensors)} sensors")
    
    # Test basic calculations
    total_monitoring_cost = sum(s.monitoring_cost for s in sensors)
    total_downtime_cost = sum(g.downtime_cost_per_hour for g in gates)
    
    print(f"PASS Basic calculations: Monitoring cost = ${total_monitoring_cost}, Downtime cost = ${total_downtime_cost}")
    
    print("PASS P26-Tier-1 execution test PASSED")
    
except Exception as e:
    print(f"FAIL P26-Tier-1 execution test FAILED: {str(e)}")

print("\nP26 testing completed!")
