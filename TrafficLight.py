from pypdevs.DEVS import *
from trafficInterface import RED, GREEN, ORANGE, TO_JAM, TO_FLUID


class TrafficLightState:

    def __init__(self, color_hor, name, red_time, green_time, orange_time):
        self.name = name
        self.color_hor = color_hor
        if color_hor == RED:
            self.color_vert = GREEN
        else:
            self.color_vert = RED
        self.redTime = red_time
        self.greenTime = green_time
        self.orangeTime = orange_time

    def __str__(self):
        theRv = "*** " + self.name + " horizontal color = " + str(self.color_hor) + " vertical color = " + str(self.color_vert)
        return theRv

    def internal(self):
        if self.color_vert == ORANGE:
            self.color_hor = GREEN
            self.color_vert = RED
            return
        if self.color_hor == GREEN:
            self.color_hor = ORANGE
            return
        if self.color_vert == GREEN:
            self.color_vert = ORANGE
            return
        if self.color_hor == ORANGE:
            self.color_hor = RED
            self.color_vert = GREEN
            return

    def output_control_hor(self):
        if self.color_hor == GREEN:
            return TO_JAM
        if (self.color_hor == RED) & (self.color_vert == ORANGE):
            return TO_FLUID
        else:
            return None

    def output_control_vert(self):
        if self.color_vert == GREEN:
            return TO_JAM
        if (self.color_vert == RED) & (self.color_hor == ORANGE):
            return TO_FLUID
        else:
            return None

    def calculate_time_advance(self):
        if (self.color_hor == GREEN) | (self.color_vert == GREEN):
            return self.greenTime
        if (self.color_hor == ORANGE) | (self.color_vert == ORANGE):
            return self.orangeTime


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

    def intTransition(self):
        self.state.internal()
        return self.state

    def outputFnc(self):
        control_hor = self.state.output_control_hor()
        control_vert = self.state.output_control_vert()
        rv = {}
        if control_hor is not None:
            rv[self.OUT_JAM_HOR] = control_hor
        if control_vert is not None:
            rv[self.OUT_JAM_VERT] = control_vert
        return rv

    def timeAdvance(self):
        return self.state.calculate_time_advance()
