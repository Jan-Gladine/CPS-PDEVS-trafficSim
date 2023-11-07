import random

from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

import Optimizer
from Optimizer import generate_random_population, objective_function

from pypdevs.simulator import Simulator
from TrafficSystem import TrafficSystem

import random
from deap import base, creator, tools, algorithms

# Create a fitness function and a fitness class
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Initialize your toolbox
toolbox = base.Toolbox()
toolbox.register("individual", tools.initRepeat, creator.Individual, Optimizer.generate_individual, n=5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", Optimizer.objective_function)
# Register the selection operator (e.g., tournament selection)
toolbox.register("select", tools.selTournament, tournsize=3)
# Register the crossover (mate) operator (e.g., two-point crossover)
toolbox.register("mate", tools.cxTwoPoint)
# Register a mutation operator (e.g., Gaussian mutation with a specified standard deviation)
toolbox.register("mutate", Optimizer.mutate_individual)
# You can also register other genetic operators like mutation and crossover here.
population = toolbox.population(10)

algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.1, ngen=100, stats=None, verbose=True)
best_individual = tools.selBest(population, k=1)[0]
best_fitness = best_individual.fitness.values[0]
print("Best individual:", best_individual)
print("Best fitness value:", best_fitness)

