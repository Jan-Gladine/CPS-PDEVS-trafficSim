from pypdevs.DEVS import *


class CarSink(AtomicDEVS):
    def __init__(self, name):
        AtomicDEVS.__init__(self, name)
        self.sim_time = 0
        self.cars = {}
        self.IN_CAR = self.addInPort("car_inputs")

    def extTransition(self, inputs):
        self.sim_time += self.elapsed
        if self.IN_CAR in inputs:
            car = inputs[self.IN_CAR]
            self.cars[car] = self.sim_time

    def get_statistics(self):
        return self.sim_time/self.cars.__sizeof__()
