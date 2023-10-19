from pypdevs.DEVS import *

from carGenerator import CarGeneratorModel
from roadsection import *
from TrafficLight import *
from trafficInterface import GREEN
from jamGenerator import JamGeneratorModel


class TrafficSystem(CoupledDEVS):
    def __init__(self):
        CoupledDEVS.__init__(self, "system")
        self.road1 = self.addSubModel(RoadSectionModel(RoadSectionState(1000, 70, "road1"), "road1"))
        self.gen = self.addSubModel(CarGeneratorModel("gen", 20))
        self.traffic_light = self.addSubModel(TrafficLightModel(TrafficLightState(GREEN, "light1"), "light1"))
        self.connectPorts(self.gen.car_out, self.road1.IN_CAR)
        self.connectPorts(self.road1.OUT_JAM, self.gen.jam_in)
        self.connectPorts(self.traffic_light.OUT_JAM, self.road1.IN_NEXT_JAM)

    def select(self, imm):
        if self.road1 in imm:
            return self.road1
        else:
            return imm[0]
