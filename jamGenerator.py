from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

import trafficInterface
from car import Car
from trafficInterface import JAMMED_OUTPUT, FULL_JAM, JAMMED, FLUID, FULL_JAM_OUTPUT, JAMMED_TO_FULL_JAM


class JamGeneratorModel(AtomicDEVS):
    def __init__(self,name,start, stop):
        AtomicDEVS.__init__(self,name)
        self.state = FLUID
        self.JAM_OUT = self.addOutPort("jam_out")
        self.current_time = 0
        self.next_time = 0
        self.start = start
        self.stop = stop

    def timeAdvance(self):
        if self.state is FLUID:
            if self.current_time <= self.start:
                self.next_time = self.start
                return self.start
            else:
                return INFINITY
        else:
            self.next_time = self.stop - self.start
            return self.stop - self.start

    def intTransition(self):
        self.current_time += self.next_time
        if self.state is FLUID:
            self.state = JAMMED
        else:
            self.state = FLUID
        return self.state

    def outputFnc(self):
        if self.state is FLUID:
            return {self.JAM_OUT : trafficInterface.TO_JAM}
        else:
            return {self.JAM_OUT : trafficInterface.TO_FLUID}
