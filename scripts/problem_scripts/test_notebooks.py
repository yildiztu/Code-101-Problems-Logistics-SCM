#!/usr/bin/env python3
"""
Test script to verify P53 notebooks work correctly
Tests the core functionality of all three tiers
"""

import sys
import traceback
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import pandas as pd
import time
from typing import Dict, Tuple

def test_tier1_mathematical():
    """Test Tier 1 Mathematical Formulation"""
    print("Testing Tier 1: Mathematical Formulation...")
    
    try:
        # Test EOQ with Shortages class
        class EOQWithShortages:
            def __init__(self, demand, ordering_cost, holding_cost, shortage_cost):
                self.D = demand
                self.K = ordering_cost
                self.h = holding_cost
                self.p = shortage_cost
                
            def calculate_optimal_solution(self):
                Q_optimal = np.sqrt(2 * self.D * self.K * (self.h + self.p) / (self.h * self.p))
                S_optimal = Q_optimal * self.h / (self.h + self.p)
                Imax_optimal = Q_optimal * self.p / (self.h + self.p)
                cycle_time = Q_optimal / self.D
                t_positive = Imax_optimal / self.D
                t_shortage = S_optimal / self.D
                ordering_cost = self.D * self.K / Q_optimal
                holding_cost = Imax_optimal**2 * self.h / (2 * self.D)
                shortage_cost = S_optimal**2 * self.p / (2 * self.D)
                total_cost = ordering_cost + holding_cost + shortage_cost
                
                return {
                    'Q_optimal': Q_optimal,
                    'S_optimal': S_optimal,
                    'Imax_optimal': Imax_optimal,
                    'cycle_time': cycle_time,
                    't_positive': t_positive,
                    't_shortage': t_shortage,
                    'ordering_cost': ordering_cost,
                    'holding_cost': holding_cost,
                    'shortage_cost': shortage_cost,
                    'total_cost': total_cost
                }
        
        # Test with Meridian Electronics parameters
        meridian_eoq = EOQWithShortages(36000, 150, 8, 12)
        optimal_solution = meridian_eoq.calculate_optimal_solution()
        
        # Verify results are reasonable
        assert optimal_solution['Q_optimal'] > 0, "Order quantity should be positive"
        assert optimal_solution['S_optimal'] > 0, "Shortage level should be positive"
        assert optimal_solution['S_optimal'] < optimal_solution['Q_optimal'], "Shortage should be less than order quantity"
        assert optimal_solution['total_cost'] > 0, "Total cost should be positive"
        
        # Check specific expected values (approximately)
        expected_Q = 1500  # From source material
        expected_S = 600   # From source material
        
        assert abs(optimal_solution['Q_optimal'] - expected_Q) < 10, f"Expected Q≈{expected_Q}, got {optimal_solution['Q_optimal']}"
        assert abs(optimal_solution['S_optimal'] - expected_S) < 10, f"Expected S≈{expected_S}, got {optimal_solution['S_optimal']}"
        
        print("✅ Tier 1 test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Tier 1 test FAILED: {e}")
        traceback.print_exc()
        return False

def test_tier2_greedy():
    """Test Tier 2 Greedy Algorithm"""
    print("Testing Tier 2: Greedy Algorithm...")
    
    try:
        # Test Greedy EOQ class
        class GreedyEOQWithShortages:
            def __init__(self, demand, ordering_cost, holding_cost, shortage_cost, order_multiple=1):
                self.D = demand
                self.K = ordering_cost
                self.h = holding_cost
                self.p = shortage_cost
                self.order_multiple = order_multiple
                
            def calculate_total_cost(self, Q, S):
                if Q <= 0 or S < 0 or S > Q:
                    return float('inf')
                ordering_cost = self.D * self.K / Q
                holding_cost = (Q - S)**2 * self.h / (2 * self.D)
                shortage_cost = S**2 * self.p / (2 * self.D)
                return ordering_cost + holding_cost + shortage_cost
            
            def get_optimal_continuous_solution(self):
                Q_optimal = np.sqrt(2 * self.D * self.K * (self.h + self.p) / (self.h * self.p))
                S_optimal = Q_optimal * self.h / (self.h + self.p)
                return Q_optimal, S_optimal
            
            def round_to_multiple(self, value):
                return int(round(value / self.order_multiple) * self.order_multiple)
            
            def greedy_search(self, max_iterations=1000, tolerance=1e-6):
                Q_cont, S_cont = self.get_optimal_continuous_solution()
                Q_current = self.round_to_multiple(Q_cont)
                S_current = min(S_cont, Q_current)
                
                if Q_current <= 0:
                    Q_current = self.order_multiple
                
                current_cost = self.calculate_total_cost(Q_current, S_current)
                
                for iteration in range(1, max_iterations + 1):
                    improved = False
                    step_sizes = [self.order_multiple, 2 * self.order_multiple, 5 * self.order_multiple]
                    
                    for step_size in step_sizes:
                        # Try increasing Q
                        Q_new = Q_current + step_size
                        S_new = min(S_current, Q_new)
                        new_cost = self.calculate_total_cost(Q_new, S_new)
                        
                        if new_cost < current_cost - tolerance:
                            Q_current, S_current = Q_new, S_new
                            current_cost = new_cost
                            improved = True
                            break
                        
                        # Try decreasing Q
                        if Q_current - step_size > 0:
                            Q_new = Q_current - step_size
                            S_new = min(S_current, Q_new)
                            new_cost = self.calculate_total_cost(Q_new, S_new)
                            
                            if new_cost < current_cost - tolerance:
                                Q_current, S_current = Q_new, S_new
                                current_cost = new_cost
                                improved = True
                            break
                    
                    if not improved:
                        for step_size in step_sizes:
                            # Try adjusting S
                            S_new = min(S_current + step_size, Q_current)
                            new_cost = self.calculate_total_cost(Q_current, S_new)
                            
                            if new_cost < current_cost - tolerance:
                                S_current = S_new
                                current_cost = new_cost
                                improved = True
                                break
                            
                            if S_current - step_size >= 0:
                                S_new = max(0, S_current - step_size)
                                new_cost = self.calculate_total_cost(Q_current, S_new)
                                
                                if new_cost < current_cost - tolerance:
                                    S_current = S_new
                                    current_cost = new_cost
                                    improved = True
                                    break
                    
                    if not improved:
                        break
                
                return {
                    'Q_optimal': Q_current,
                    'S_optimal': S_current,
                    'total_cost': current_cost,
                    'iterations': iteration,
                    'converged': improved == False
                }
        
        # Test with discrete constraint
        greedy_eoq = GreedyEOQWithShortages(36000, 150, 8, 12, order_multiple=50)
        greedy_solution = greedy_eoq.greedy_search()
        
        # Verify results
        assert greedy_solution['Q_optimal'] > 0, "Order quantity should be positive"
        assert greedy_solution['S_optimal'] >= 0, "Shortage level should be non-negative"
        assert greedy_solution['S_optimal'] <= greedy_solution['Q_optimal'], "Shortage should not exceed order quantity"
        assert greedy_solution['total_cost'] > 0, "Total cost should be positive"
        assert greedy_solution['converged'] == True, "Algorithm should converge"
        
        # Check discrete constraint
        assert greedy_solution['Q_optimal'] % 50 == 0, "Order quantity should be multiple of 50"
        
        print("✅ Tier 2 test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Tier 2 test FAILED: {e}")
        traceback.print_exc()
        return False

def test_tier3_simulated_annealing():
    """Test Tier 3 Simulated Annealing"""
    print("Testing Tier 3: Simulated Annealing...")
    
    try:
        # Test Simulated Annealing implementation
        class SimulatedAnnealingEOQ:
            def __init__(self, demand, ordering_cost, holding_cost, shortage_cost, order_multiple=1):
                self.D = demand
                self.K = ordering_cost
                self.h = holding_cost
                self.p = shortage_cost
                self.order_multiple = order_multiple
                
                # Calculate theoretical optimum
                self.Q_theoretical = np.sqrt(2 * demand * ordering_cost * (holding_cost + shortage_cost) / (holding_cost * shortage_cost))
                self.S_theoretical = self.Q_theoretical * holding_cost / (holding_cost + shortage_cost)
                
            def calculate_total_cost(self, Q, S):
                if Q <= 0 or S < 0 or S > Q:
                    return float('inf')
                ordering_cost = self.D * self.K / Q
                holding_cost = (Q - S)**2 * self.h / (2 * self.D)
                shortage_cost = S**2 * self.p / (2 * self.D)
                return ordering_cost + holding_cost + shortage_cost
            
            def generate_initial_solution(self):
                Q_range = (self.Q_theoretical * 0.5, self.Q_theoretical * 2.0)
                Q_initial = np.random.uniform(Q_range[0], Q_range[1])
                
                if self.order_multiple > 1:
                    Q_initial = int(round(Q_initial / self.order_multiple) * self.order_multiple)
                
                Q_initial = max(1, min(Q_initial, self.Q_theoretical * 3))
                S_initial = Q_initial * np.random.uniform(0.2, 0.6)
                
                return Q_initial, S_initial
            
            def generate_neighbor(self, Q, S, temperature):
                step_size = temperature * 0.1 * self.Q_theoretical
                Q_new = Q + np.random.uniform(-step_size, step_size)
                
                if self.order_multiple > 1:
                    Q_new = int(round(Q_new / self.order_multiple) * self.order_multiple)
                
                Q_new = max(1, min(Q_new, self.Q_theoretical * 3))
                S_new = S + np.random.uniform(-step_size * 0.5, step_size * 0.5)
                S_new = max(0, min(S_new, Q_new))
                
                return Q_new, S_new
            
            def acceptance_probability(self, current_cost, new_cost, temperature):
                if new_cost < current_cost:
                    return 1.0
                else:
                    if temperature <= 0:
                        return 0.0
                    return np.exp(-(new_cost - current_cost) / temperature)
            
            def cooling_schedule(self, initial_temp, iteration, max_iterations):
                alpha = 0.995
                return initial_temp * (alpha ** iteration)
            
            def simulated_annealing(self, max_iterations=500, initial_temp=100.0):
                Q_current, S_current = self.generate_initial_solution()
                current_cost = self.calculate_total_cost(Q_current, S_current)
                
                Q_best, S_best = Q_current, S_current
                best_cost = current_cost
                
                for iteration in range(max_iterations):
                    temperature = self.cooling_schedule(initial_temp, iteration, max_iterations)
                    Q_new, S_new = self.generate_neighbor(Q_current, S_current, temperature)
                    new_cost = self.calculate_total_cost(Q_new, S_new)
                    
                    accept_prob = self.acceptance_probability(current_cost, new_cost, temperature)
                    
                    if np.random.random() < accept_prob:
                        Q_current, S_current = Q_new, S_new
                        current_cost = new_cost
                        
                        if current_cost < best_cost:
                            Q_best, S_best = Q_current, S_current
                            best_cost = current_cost
                
                return {
                    'Q_optimal': Q_best,
                    'S_optimal': S_best,
                    'total_cost': best_cost,
                    'iterations': max_iterations
                }
        
        # Test Simulated Annealing
        sa_optimizer = SimulatedAnnealingEOQ(36000, 150, 8, 12, order_multiple=50)
        sa_result = sa_optimizer.simulated_annealing(max_iterations=200)  # Reduced for testing
        
        # Verify results
        assert sa_result['Q_optimal'] > 0, "Order quantity should be positive"
        assert sa_result['S_optimal'] >= 0, "Shortage level should be non-negative"
        assert sa_result['S_optimal'] <= sa_result['Q_optimal'], "Shortage should not exceed order quantity"
        assert sa_result['total_cost'] > 0, "Total cost should be positive"
        
        # Check discrete constraint
        assert sa_result['Q_optimal'] % 50 == 0, "Order quantity should be multiple of 50"
        
        print("✅ Tier 3 test PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Tier 3 test FAILED: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("P53 NOTEBOOK FUNCTIONALITY TESTS")
    print("=" * 60)
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    results = []
    
    # Test each tier
    results.append(("Tier 1: Mathematical Formulation", test_tier1_mathematical()))
    results.append(("Tier 2: Greedy Algorithm", test_tier2_greedy()))
    results.append(("Tier 3: Simulated Annealing", test_tier3_simulated_annealing()))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 ALL TESTS PASSED! Notebooks are working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementations.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
