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
# You can also register other genetic operators like mutation and crossover here.
population = toolbox.population(10)

algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, stats=None, verbose=True)

