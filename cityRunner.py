from pypdevs.simulator import Simulator

import Optimizer
from TrafficSystem import TrafficSystem


traffic = TrafficSystem([[36, 5, 39], [48, 4, 52], [51, 7, 36], [60, 9, 51], [51, 7, 34]])
sim = Simulator(traffic)
sim.setTerminationTime(1000)
sim.setVerbose()
sim.setClassicDEVS()
sim.simulate()
print(traffic.sink.get_statistics())

