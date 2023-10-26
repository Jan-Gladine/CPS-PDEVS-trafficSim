from random import random

from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY
from Optimizer import generate_random_population, objective_function

from pypdevs.simulator import Simulator
from TrafficSystem import TrafficSystem

from deap import algorithms, creator, base, tools

initial_population = generate_random_population(50)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0, 1)  # Adjust the bounds accordingly
toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_float,), n=3)

algorithms.eaSimple(initial_population, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, stats=None, verbose=True)

