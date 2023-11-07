from pypdevs.DEVS import *

from Carsink import CarSink
from carGenerator import CarGeneratorModel
from roadsection import *
from TrafficLight import *
from trafficInterface import GREEN
from jamGenerator import JamGeneratorModel


class TrafficSystem(CoupledDEVS):
    def __init__(self, light_times):
        CoupledDEVS.__init__(self, "system")

        # creation central road sections
        self.road1 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road1"), "road left-right 1"))

        self.road2 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road2"), "road right-left 1"))

        self.road3 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED,  "road3"), "road left-right 2"))

        self.road4 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road4"), "road right-left 2"))

        self.road5 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road5"), "road left-right 1"))

        self.road6 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road6"), "road right-left 1"))

        self.road7 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road7"), "road left-right 2"))

        self.road8 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road8"), "road right-left 2"))

        # creation outer road sections
        self.road9 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, JAMMED, "road9"), "road up-down 2"))

        self.road10 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, FLUID, "road10"), "road down-up 2"))

        self.road11 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, JAMMED, "road11"), "road up-down 1"))

        self.road12 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, FLUID, "road12"), "road down-up 1"))

        self.road13 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, FLUID, "road13"), "road up-down 2"))

        self.road14 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, JAMMED, "road14"), "road down-up 2"))

        self.road15 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, FLUID, "road15"), "road up-down 1"))

        self.road16 = self.addSubModel(
            RoadSectionModel(RoadSectionState(2000, 70, JAMMED, "road16"), "road down-up 1"))

        self.road17 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road17"), "road up-down 2"))

        self.road18 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road18"), "road down-up 2"))

        self.road19 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, JAMMED, "road19"), "road up-down 1"))

        self.road20 = self.addSubModel(
            RoadSectionModel(RoadSectionState(1000, 70, FLUID, "road20"), "road down-up 1"))

        self.sink = self.addSubModel(CarSink("sink"))

        # car generator + traffic light creation
        self.gen = self.addSubModel(CarGeneratorModel("gen", 20))
        self.traffic_light1 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light1", light_times[0][0], light_times[0][2], light_times[0][1]), "light1"))
        self.traffic_light2 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light2", light_times[1][0], light_times[1][2], light_times[1][1]), "light2"))
        self.traffic_light3 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light3", light_times[2][0], light_times[2][2], light_times[2][1]), "light1"))
        self.traffic_light4 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light4", light_times[3][0], light_times[3][2], light_times[3][1]), "light2"))
        self.traffic_light5 = self.addSubModel(
            TrafficLightModel(TrafficLightState(GREEN, "light5", light_times[4][0], light_times[4][2], light_times[4][1]), "light2"))

        # generator ports
        self.connectPorts(self.gen.car_out, self.road17.IN_CAR)
        self.connectPorts(self.gen.car_out, self.road18.IN_CAR)
        self.connectPorts(self.gen.car_out, self.road19.IN_CAR)
        self.connectPorts(self.gen.car_out, self.road20.IN_CAR)

        # road connection ports light 1
        self.connectPorts(self.road2.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.road6.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.road4.OUT_CAR, self.traffic_light1.IN_CAR)
        self.connectPorts(self.road8.OUT_CAR, self.traffic_light1.IN_CAR)

        self.connectPorts(self.traffic_light1.OUT_CAR_RIGHT, self.road5.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_LEFT, self.road1.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_DOWN, self.road3.IN_CAR)
        self.connectPorts(self.traffic_light1.OUT_CAR_UP, self.road7.IN_CAR)

        # road connection ports light 2
        self.connectPorts(self.road7.OUT_CAR, self.traffic_light2.IN_CAR)
        self.connectPorts(self.road10.OUT_CAR, self.traffic_light2.IN_CAR)
        self.connectPorts(self.road15.OUT_CAR, self.traffic_light2.IN_CAR)
        self.connectPorts(self.road17.OUT_CAR, self.traffic_light2.IN_CAR)

        self.connectPorts(self.traffic_light2.OUT_CAR_RIGHT, self.road16.IN_CAR)
        self.connectPorts(self.traffic_light2.OUT_CAR_LEFT, self.road9.IN_CAR)
        self.connectPorts(self.traffic_light2.OUT_CAR_DOWN, self.road8.IN_CAR)
        self.connectPorts(self.traffic_light2.OUT_CAR_UP, self.sink.IN_CAR)

        # road connection ports light 3
        self.connectPorts(self.road5.OUT_CAR, self.traffic_light3.IN_CAR)
        self.connectPorts(self.road14.OUT_CAR, self.traffic_light3.IN_CAR)
        self.connectPorts(self.road16.OUT_CAR, self.traffic_light3.IN_CAR)
        self.connectPorts(self.road18.OUT_CAR, self.traffic_light3.IN_CAR)

        self.connectPorts(self.traffic_light3.OUT_CAR_UP, self.road15.IN_CAR)
        self.connectPorts(self.traffic_light3.OUT_CAR_LEFT, self.road6.IN_CAR)
        self.connectPorts(self.traffic_light3.OUT_CAR_DOWN, self.road13.IN_CAR)
        self.connectPorts(self.traffic_light3.OUT_CAR_RIGHT, self.sink.IN_CAR)

        # road connection ports light 4
        self.connectPorts(self.road12.OUT_CAR, self.traffic_light4.IN_CAR)
        self.connectPorts(self.road3.OUT_CAR, self.traffic_light4.IN_CAR)
        self.connectPorts(self.road13.OUT_CAR, self.traffic_light4.IN_CAR)
        self.connectPorts(self.road19.OUT_CAR, self.traffic_light4.IN_CAR)

        self.connectPorts(self.traffic_light4.OUT_CAR_UP, self.road4.IN_CAR)
        self.connectPorts(self.traffic_light4.OUT_CAR_LEFT, self.road11.IN_CAR)
        self.connectPorts(self.traffic_light4.OUT_CAR_RIGHT, self.road14.IN_CAR)
        self.connectPorts(self.traffic_light4.OUT_CAR_DOWN, self.sink.IN_CAR)

        # road connection ports light 5
        self.connectPorts(self.road11.OUT_CAR, self.traffic_light5.IN_CAR)
        self.connectPorts(self.road1.OUT_CAR, self.traffic_light5.IN_CAR)
        self.connectPorts(self.road9.OUT_CAR, self.traffic_light5.IN_CAR)
        self.connectPorts(self.road20.OUT_CAR, self.traffic_light5.IN_CAR)

        self.connectPorts(self.traffic_light5.OUT_CAR_UP, self.road10.IN_CAR)
        self.connectPorts(self.traffic_light5.OUT_CAR_RIGHT, self.road2.IN_CAR)
        self.connectPorts(self.traffic_light5.OUT_CAR_DOWN, self.road12.IN_CAR)
        self.connectPorts(self.traffic_light5.OUT_CAR_LEFT, self.sink.IN_CAR)

        # traffic light 1 ports
        self.connectPorts(self.traffic_light1.OUT_JAM_HOR, self.road2.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_HOR, self.road6.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_VERT, self.road8.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light1.OUT_JAM_VERT, self.road4.IN_NEXT_JAM)

        # traffic light 2 ports
        self.connectPorts(self.traffic_light2.OUT_JAM_HOR, self.road10.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light2.OUT_JAM_HOR, self.road15.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light2.OUT_JAM_VERT, self.road7.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light2.OUT_JAM_VERT, self.road17.IN_NEXT_JAM)

        # traffic light 3 ports
        self.connectPorts(self.traffic_light3.OUT_JAM_HOR, self.road5.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light3.OUT_JAM_HOR, self.road18.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light3.OUT_JAM_VERT, self.road16.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light3.OUT_JAM_VERT, self.road14.IN_NEXT_JAM)

        # traffic light 4 ports
        self.connectPorts(self.traffic_light4.OUT_JAM_HOR, self.road12.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light4.OUT_JAM_HOR, self.road13.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light4.OUT_JAM_VERT, self.road19.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light4.OUT_JAM_VERT, self.road3.IN_NEXT_JAM)

        # traffic light 5 ports
        self.connectPorts(self.traffic_light5.OUT_JAM_HOR, self.road1.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light5.OUT_JAM_HOR, self.road20.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light5.OUT_JAM_VERT, self.road9.IN_NEXT_JAM)
        self.connectPorts(self.traffic_light5.OUT_JAM_VERT, self.road11.IN_NEXT_JAM)

    def select(self, imm):
        if self.road1 in imm:
            return self.road1
        else:
            return imm[0]
