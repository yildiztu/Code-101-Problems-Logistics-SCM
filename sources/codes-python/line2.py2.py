# Condensed version for academic presentation
# This pseudocode outlines a Genetic Algorithm for minimizing container reshuffles in stacking configurations.
# It uses a chromosome where each gene represents the preferred stack for a container.
# Core logic: Initialize population, evaluate fitness (reshuffles + penalties), evolve via selection, crossover, and mutation.

class StackingGeneticAlgorithm:
    def __init__(self, containers, stacks, max_tiers, population_size=100, generations=500):
        # Set parameters: containers list, number of stacks, max tiers per stack, population size, generations
        self.containers = containers  # List of (id, dept_time, weight)
        self.stacks = stacks
        self.max_tiers = max_tiers
        self.population_size = population_size
        self.generations = generations
        self.chromosome_length = len(containers)
    
    def initialize_population(self):
        # Generate initial population: each chromosome is a list of random stack preferences (0 to stacks-1) for each container
        population = []
        for _ in range(self.population_size):
            chromosome = [random.randint(0, self.stacks - 1) for _ in self.containers]
            population.append(chromosome)
        return population
    
    def fitness_function(self, chromosome):
        # Decode chromosome to stack config, calculate reshuffles, add penalties for exceeding max_tiers
        # Fitness = 1 / (1 + reshuffles + penalty)
        stack_config = self.decode_chromosome(chromosome)
        reshuffles = self.calculate_reshuffles(stack_config)  # Assume this method computes reshuffles based on retrieval order
        penalty = sum(max(0, len(stack) - self.max_tiers) * 100 for stack in stack_config)
        return 1.0 / (1.0 + reshuffles + penalty)
    
    def decode_chromosome(self, chromosome):
        # Sort containers by departure time, place each in preferred stack or first available alternative if full
        stack_config = [[] for _ in range(self.stacks)]
        sorted_containers = sorted(enumerate(self.containers), key=lambda x: x[1][1])  # By dept_time
        for idx, (container_id, dept_time, weight) in sorted_containers:
            preferred = chromosome[idx]
            if len(stack_config[preferred]) < self.max_tiers:
                stack_config[preferred].append((container_id, dept_time, weight))
            else:
                for stack_idx in range(self.stacks):
                    if len(stack_config[stack_idx]) < self.max_tiers:
                        stack_config[stack_idx].append((container_id, dept_time, weight))
                        break
        return stack_config
    
    def crossover(self, parent1, parent2):
        # Single-point crossover: split at random point, swap tails
        point = random.randint(1, self.chromosome_length - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    
    def mutate(self, chromosome, mutation_rate=0.1):
        # Mutate each gene with probability mutation_rate: replace with random stack index
        mutated = chromosome.copy()
        for i in range(len(mutated)):
            if random.random() < mutation_rate:
                mutated[i] = random.randint(0, self.stacks - 1)
        return mutated
    
    def tournament_selection(self, population, fitness_scores, tournament_size=3):
        # Select winners from random tournaments based on fitness
        selected = []
        for _ in range(len(population)):
            indices = random.sample(range(len(population)), tournament_size)
            winner = max(indices, key=lambda x: fitness_scores[x])
            selected.append(population[winner])
        return selected
    
    def evolve(self):
        # Evolutionary loop: initialize, evaluate, select, crossover/mutate for generations
        population = self.initialize_population()
        best_fitness_history = []
        for gen in range(self.generations):
            fitness_scores = [self.fitness_function(chrom) for chrom in population]
            best_fitness = max(fitness_scores)
            best_fitness_history.append(best_fitness)
            selected = self.tournament_selection(population, fitness_scores)
            new_population = []
            for i in range(0, len(selected), 2):
                if i + 1 < len(selected):
                    child1, child2 = self.crossover(selected[i], selected[i+1])
                    child1 = self.mutate(child1)
                    child2 = self.mutate(child2)
                    new_population.extend([child1, child2])
            population = new_population[:self.population_size]
        # Return best chromosome and fitness history
        final_fitness = [self.fitness_function(chrom) for chrom in population]
        best_idx = argmax(final_fitness)
        return population[best_idx], best_fitness_history

# Note: calculate_reshuffles method is assumed to be implemented elsewhere, simulating container retrieval and counting reshuffles.