from pypdevs.DEVS import *

from carGenerator import CarGeneratorModel
from roadsection import *
from jamGenerator import JamGeneratorModel

class TrafficSystem(CoupledDEVS):
    def __init__(self):
        CoupledDEVS.__init__(self, "system")
        self.road1 = self.addSubModel(RoadSectionModel(RoadSectionState(1000,70, "road1"),"road1"))
        self.gen = self.addSubModel(CarGeneratorModel("gen",20))
        self.jammer = self.addSubModel(JamGeneratorModel("jamgen",100 , 200))
        self.connectPorts(self.gen.car_out, self.road1.IN_CAR)
        self.connectPorts(self.road1.OUT_JAM, self.gen.jam_in)
        self.connectPorts(self.jammer.JAM_OUT, self.road1.IN_NEXT_JAM)

    def select(self, imm):
        if self.road1 in imm:
            return self.road1
        else:
            return imm[0]