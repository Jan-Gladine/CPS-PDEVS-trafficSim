from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY

import trafficInterface
from car import Car
from trafficInterface import JAMMED_OUTPUT, FULL_JAM, JAMMED, FLUID, FULL_JAM_OUTPUT, JAMMED_TO_FULL_JAM


class CarGeneratorModel(AtomicDEVS):
    def __init__(self, name, number_of_cars):
        AtomicDEVS.__init__(self, name)
        self.state = number_of_cars
        self.car_out = self.addOutPort("car_our")
        self.jam_in = self.addInPort("jam_in")
        self.current_time = 0
        self.next_time = 0

    def timeAdvance(self):
        if self.state > 0:
            self.next_time = 10
            return self.next_time
        else:
            return INFINITY

    def intTransition(self):
        self.current_time += self.next_time
        return self.state-1

    def extTransition(self, inputs):
        self.state=0
        return self.state

    def outputFnc(self):
        return {self.car_out : Car(0, self.current_time)}