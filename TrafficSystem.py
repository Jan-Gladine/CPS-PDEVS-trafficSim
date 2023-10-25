from pypdevs.DEVS import *

from carGenerator import CarGeneratorModel
from roadsection import *
from TrafficLight import *
from trafficInterface import GREEN
from jamGenerator import JamGeneratorModel


class TrafficSystem(CoupledDEVS):
    def __init__(self):
        CoupledDEVS.__init__(self, "system")

        # creation horizontal road sections
        self.roadLeft1 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road left-right 1"), "road left-right 1"))

        self.roadLeft2 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road right-left 1"), "road right-left 1"))

        self.roadRight1 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID,  "road left-right 2"), "road left-right 2"))

        self.roadRight2 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road right-left 2"), "road right-left 2"))

        # creation vertical road sections
        self.roadUp1 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road up-down 2"), "road up-down 2"))

        self.roadUp2 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road down-up 2"), "road down-up 2"))

        self.roadDown1 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road up-down 1"), "road up-down 1"))

        self.roadDown2 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road down-up 1"), "road down-up 1"))

        self.gen = self.addSubModel(CarGeneratorModel("gen", 20))
        self.traffic_light1 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light1", 70, 60, 10), "light1"))
        self.traffic_light2 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light2", 70, 60, 10), "light2"))
        self.traffic_light3 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light3", 70, 60, 10), "light1"))
        self.traffic_light4 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light4", 70, 60, 10), "light2"))
        self.traffic_light5 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light5", 70, 60, 10), "light2"))

        # generator ports
        # self.connectPorts(self.gen.car_out, self.roadLeft1.IN_CAR)
        # self.connectPorts(self.gen.car_out, self.roadRight2.IN_CAR)
        # self.connectPorts(self.gen.car_out, self.roadUp1.IN_CAR)
        self.connectPorts(self.gen.car_out, self.roadDown2.IN_CAR)

        # road connection ports
        self.connectPorts(self.roadLeft1.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.roadRight2.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.roadUp1.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.roadDown2.OUT_CAR, self.traffic_light1.IN_CAR)

        self.connectPorts(self.traffic_light1.OUT_CAR_RIGHT, self.roadRight1.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_LEFT, self.roadLeft2.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_DOWN, self.roadDown1.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_UP, self.roadUp2.IN_CAR)

        # traffic light ports
        self.connectPorts(self.traffic_light1.OUT_JAM_HOR, self.roadLeft1.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_HOR, self.roadRight2.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_VERT, self.roadUp1.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_VERT, self.roadDown2.IN_NEXT_JAM)

    def select(self, imm):
        if self.roadLeft1 in imm:
            return self.roadLeft1
        else:
            return imm[0]
