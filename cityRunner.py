from pypdevs.simulator import Simulator

import Optimizer
from TrafficSystem import TrafficSystem


traffic = TrafficSystem(Optimizer.initial_generator())
sim = Simulator(traffic)
sim.setTerminationTime(1000)
sim.setVerbose()
sim.setClassicDEVS()
sim.simulate()

