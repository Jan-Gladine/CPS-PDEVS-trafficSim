import random
from TrafficSystem import TrafficSystem
from pypdevs.simulator import Simulator

decision_variables = [
    [20, 60],  # Variable 1 with bounds
    [3, 10],  # Variable 2 with bounds
    [20, 60],  # Variable 3 with bounds
]


def initial_generator():
    initial_population = []
    for _ in range(5):
        values = [random.randint(var[0], var[1]) for var in decision_variables]
        initial_population.append(values)
    return initial_population


def generate_individual():
    values = [random.randint(var[0], var[1]) for var in decision_variables]
    return values


def objective_function(light_times):
    traffic = TrafficSystem(light_times)
    sim = Simulator(traffic)
    sim.setTerminationTime(1000)
    sim.setClassicDEVS()
    sim.simulate()
    return traffic.sink.get_statistics()


def generate_random_population(n):
    return [initial_generator() for _ in range(n)]

