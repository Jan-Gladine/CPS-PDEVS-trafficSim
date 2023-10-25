import random

from pypdevs.DEVS import *
from trafficInterface import RED, GREEN, ORANGE, TO_JAM, TO_FLUID, ROAD_UP, ROAD_DOWN, ROAD_LEFT, ROAD_RIGHT


class TrafficLightState:

    def __init__(self, color_hor, name, green_time_hor, green_time_vert, orange_time):
        self.name = name
        self.color_hor = color_hor
        if color_hor == RED:
            self.color_vert = GREEN
        else:
            self.color_vert = RED
        self.greenTime_hor = green_time_hor
        self.greenTime_vert = green_time_vert
        self.orangeTime = orange_time
        self.passing_car = 0
        self.car = None
        self.elapsed = 0
        self.time_on = 0

    def __str__(self):
        theRv = "*** " + self.name + " horizontal color = " + str(self.color_hor) + " vertical color = " + str(
            self.color_vert)
        return theRv

    def internal(self):
        if self.passing_car == 1:
            self.passing_car = 0
            return
        if self.color_vert == ORANGE:
            self.color_hor = GREEN
            self.color_vert = RED
            self.elapsed = 0
            return
        if self.color_hor == GREEN:
            self.color_hor = ORANGE
            self.elapsed = 0
            return
        if self.color_vert == GREEN:
            self.color_vert = ORANGE
            self.elapsed = 0
            return
        if self.color_hor == ORANGE:
            self.color_hor = RED
            self.color_vert = GREEN
            self.elapsed = 0
            return

    def output_control_hor(self):
        if self.passing_car != 1:
            if self.color_hor == GREEN:
                return TO_JAM
            if (self.color_hor == RED) & (self.color_vert == ORANGE):
                return TO_FLUID
        return None

    def output_control_vert(self):
        if self.passing_car != 1:
            if self.color_vert == GREEN:
                return TO_JAM
            if (self.color_vert == RED) & (self.color_hor == ORANGE):
                return TO_FLUID
        return None

    def calculate_time_advance(self):
        rv = None
        if self.passing_car == 1:
            return 0
        if self.color_hor == GREEN:
            rv = self.greenTime_hor - self.elapsed
        if self.color_vert == GREEN:
            rv = self.greenTime_vert - self.elapsed
        if (self.color_hor == ORANGE) | (self.color_vert == ORANGE):
            rv = self.orangeTime - self.elapsed
        return rv

    def car_enters(self, car, elapsed_time):
        self.elapsed += elapsed_time
        self.passing_car = 1
        self.car = car

    def car_output_control(self):
        car = self.car
        self.car = None
        return car


def select_random_out():
    value = random.randint(0, 100)
    if value < 25:
        return ROAD_UP
    if 25 <= value < 50:
        return ROAD_DOWN
    if 50 <= value < 75:
        return ROAD_LEFT
    if value >= 75:
        return ROAD_RIGHT


class TrafficLightModel(AtomicDEVS):
    def __init__(self, state, name):
        AtomicDEVS.__init__(self, name)
        if isinstance(state, TrafficLightState):
            self.state = state
        else:
            print("error in init of trafficLightModel")
            exit(1)
        self.OUT_JAM_HOR = self.addOutPort("out_going_jam_horizontal")
        self.OUT_JAM_VERT = self.addOutPort("out_going_jam_vertical")
        self.IN_CAR = self.addInPort("incoming_car")
        self.OUT_CAR_LEFT = self.addOutPort("outgoing_car_left")
        self.OUT_CAR_RIGHT = self.addOutPort("outgoing_car_right")
        self.OUT_CAR_UP = self.addOutPort("outgoing_car_up")
        self.OUT_CAR_DOWN = self.addOutPort("outgoing_car_down")

    def intTransition(self):
        self.state.internal()
        return self.state

    def extTransition(self, inputs):
        car = None
        if self.IN_CAR in inputs:
            car = inputs[self.IN_CAR]
        if car is not None:
            self.state.car_enters(car, self.elapsed)
        return self.state

    def outputFnc(self):
        control_hor = self.state.output_control_hor()
        control_vert = self.state.output_control_vert()
        car_output = self.state.car_output_control()
        rv = {}
        if car_output is not None:
            output = select_random_out()
            if output == ROAD_DOWN:
                rv[self.OUT_CAR_DOWN] = car_output
            if output == ROAD_UP:
                rv[self.OUT_CAR_UP] = car_output
            if output == ROAD_LEFT:
                rv[self.OUT_CAR_LEFT] = car_output
            if output == ROAD_RIGHT:
                rv[self.OUT_CAR_RIGHT] = car_output
        if control_hor is not None:
            rv[self.OUT_JAM_HOR] = control_hor
        if control_vert is not None:
            rv[self.OUT_JAM_VERT] = control_vert
        return rv

    def timeAdvance(self):
        return self.state.calculate_time_advance()

