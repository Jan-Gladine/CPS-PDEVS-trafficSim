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
    return (traffic.sink.get_statistics(),)


def generate_random_population(n):
    return [initial_generator() for _ in range(n)]


def mutate_individual(individual):
    # Iterate through the sublists of the individual
    for i in range(len(individual)):
        # Choose a random index within the sublist
        index_to_mutate = random.randint(0, len(individual[i]) - 1)
        # Mutate the element at the chosen index
        individual[i][index_to_mutate] = random.randint(decision_variables[index_to_mutate][0], decision_variables[index_to_mutate][1])  # You can adjust the mutation range as needed
    return (individual,)
