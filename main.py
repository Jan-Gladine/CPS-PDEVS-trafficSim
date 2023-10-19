from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

from pypdevs.simulator import Simulator
from TrafficSystem import TrafficSystem

sim = Simulator(TrafficSystem())
sim.setVerbose()
sim.setTerminationTime(1000)
sim.setClassicDEVS()
sim.simulate()
