# Condensed version for academic presentation
# This pseudocode outlines the core logic of a Deep Q-Network (DQN) agent for container stacking optimization in a reinforcement learning environment.
# It focuses on state encoding, action selection, experience replay, and reward calculation, abstracting away implementation details for clarity.

class StackingDQNAgent:
    def __init__(self, state_size, action_size):
        # Initialize agent parameters
        self.memory = deque(maxlen=10000)  # Experience replay buffer
        self.epsilon = 1.0  # Exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.q_network = self.build_model(state_size, action_size)  # Main Q-network
        self.target_network = self.build_model(state_size, action_size)  # Target network for stability
        self.optimizer = Adam optimizer for q_network

    def build_model(self, state_size, action_size):
        # Define neural network: Input -> Hidden layers -> Output Q-values
        return Sequential network with layers approximating Q-function

    def encode_state(self, stack_config, arriving_container, departure_schedule):
        # Encode state as vector: stack heights, upcoming departures, container features, balance metrics
        state_vector = [heights of stacks] + [next 5 departure times] + [container dept_time, weight] + [avg_height, height_variance]
        return state_vector

    def get_valid_actions(self, stack_config, max_tiers):
        # Return indices of stacks not at max capacity
        return [stack_idx for stack_idx, stack in enumerate(stack_config) if len(stack) < max_tiers]

    def act(self, state, valid_actions):
        # Epsilon-greedy action selection
        if random() < epsilon:  # Explore
            return random valid_action
        else:  # Exploit: compute Q-values, mask invalids, select max
            q_values = q_network(state)
            masked_q = set invalid actions to -inf
            return argmax(masked_q)

    def remember(self, state, action, reward, next_state, done):
        # Store experience tuple in replay buffer
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size=32):
        # Train on batch from replay buffer
        if len(memory) < batch_size: return
        batch = sample random batch
        # Compute targets: rewards + gamma * max_next_q * (1 - done)
        current_q = q_network(states).gather(actions)
        next_q = target_network(next_states).max()
        targets = rewards + gamma * next_q * (1 - dones)
        loss = MSE(current_q, targets)
        # Backpropagate and update network
        optimizer.step()
        # Decay epsilon
        self.epsilon = max(epsilon_min, epsilon * epsilon_decay)

    def update_target_network(self):
        # Periodically copy Q-network weights to target network
        self.target_network.load_state_dict(self.q_network.state_dict())

class StackingEnvironment:
    def __init__(self, containers, stacks, max_tiers):
        self.containers = containers  # List of (id, dept_time, weight)
        self.stacks = stacks  # Number of stacks
        self.max_tiers = max_tiers

    def reset(self):
        # Reset to initial state: empty stacks, start at first container
        self.stack_config = [[] for _ in range(stacks)]
        self.container_index = 0
        self.total_reshuffles = 0
        return self.get_state()

    def get_state(self):
        # Return state dict: current stacks, next container, future departures
        if container_index >= len(containers): return None
        arriving = containers[container_index]
        departures = [c[1] for c in containers[container_index:]]
        return {'stack_config': stack_config, 'arriving_container': arriving, 'departure_schedule': departures}

    def step(self, action):
        # Execute action: place container in stack_idx, compute reward, advance to next
        if container_index >= len(containers): return None, 0, True
        container = containers[container_index]
        stack_idx = action
        if len(stack_config[stack_idx]) >= max_tiers: return get_state(), -10, False  # Penalty for invalid
        stack_config[stack_idx].append(container)
        reward = self.calculate_reward(stack_idx, container)
        self.container_index += 1
        done = container_index >= len(containers)
        return get_state(), reward, done

    def calculate_reward(self, stack_idx, container):
        # Reward function: penalize potential reshuffles, variance, weight instability; reward balance and stability
        stack = stack_config[stack_idx]
        reward = 0
        # Penalize for blocking earlier departures in stack
        for existing in stack[:-1]:
            if container[1] < existing[1]: reward -= 5
        # Penalize height variance for imbalance
        reward -= variance([len(s) for s in stack_config]) * 0.1
        # Reward weight stability (lighter on top)
        if len(stack) > 1:
            if container[2] <= stack[-2][2]: reward += 1
            else: reward -= 2
        return reward