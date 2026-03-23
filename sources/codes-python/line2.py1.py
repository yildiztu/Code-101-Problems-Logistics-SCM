# Condensed version for academic presentation

# Priority-based stacking heuristic for container assignment
# Inputs: containers (list of [id, departure_time, weight]), stacks (num), max_tiers (max per stack)
# Outputs: stack_assignment (dict: id -> (stack, tier)), total_reshuffles (expected reshuffles)

def priority_based_stacking(containers, stacks, max_tiers):
    # Initialize empty stacks and assignment dict
    stack_config = [[] for _ in range(stacks)]  # list of lists: each sublist is [(id, dept_time)]
    stack_assignment = {}
    
    for container_id, dept_time, weight in containers:
        best_stack = -1
        best_score = inf
        
        # Evaluate each stack for placement
        for stack_idx in range(stacks):
            if len(stack_config[stack_idx]) >= max_tiers: continue  # skip full stacks
            
            # Compute score based on reshuffles, balance, stability
            score = calculate_placement_score(container_id, dept_time, weight, stack_idx, stack_config)
            if score < best_score:
                best_score = score
                best_stack = stack_idx
        
        # Assign to best stack if found
        if best_stack != -1:
            tier = len(stack_config[best_stack])
            stack_config[best_stack].append((container_id, dept_time))
            stack_assignment[container_id] = (best_stack, tier)
    
    # Compute total expected reshuffles across all stacks
    total_reshuffles = calculate_total_reshuffles(stack_config)
    return stack_assignment, total_reshuffles

# Multi-criteria score: penalizes early departures (reshuffles), height imbalance, weight instability
def calculate_placement_score(container_id, dept_time, weight, stack_idx, stack_config):
    score = 0.0
    stack = stack_config[stack_idx]
    
    # Penalty for violating LIFO (departure time order)
    for _, existing_dept in stack:
        if dept_time < existing_dept: score += 10.0
    
    # Penalty for unbalanced heights (favor even stack utilization)
    stack_height = len(stack)
    avg_height = sum(len(s) for s in stack_config) / len(stack_config)
    score += abs(stack_height - avg_height) * 2.0
    
    # Penalty for weight instability (heavier should be below)
    if stack:
        top_weight = get_container_weight(stack[-1])
        if weight > top_weight: score += 5.0
    
    return score

# Note: get_container_weight and calculate_total_reshuffles assumed implemented (not shown for brevity)