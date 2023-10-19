from pypdevs.DEVS import *
from trafficInterface import RED, GREEN, ORANGE, TO_JAM, TO_FLUID


class TrafficLightState:

    def __init__(self, color, name):
        self.name = name
        self.color = color

    def __str__(self):
        theRv = "*** " + self.name + " state = " + str(self.color)
        return theRv

    def internal(self):
        if self.color == RED:
            self.color = GREEN
            return
        if self.color == GREEN:
            self.color = ORANGE
            return
        if self.color == ORANGE:
            self.color = RED
            return

    def output_control(self):
        if self.color == GREEN:
            return TO_JAM
        if self.color == RED:
            return TO_FLUID
        else:
            return None

    def calculate_time_advance(self):
        if self.color == RED:
            return 70
        if self.color == GREEN:
            return 60
        if self.color == ORANGE:
            return 10


class TrafficLightModel(AtomicDEVS):
    def __init__(self, state, name):
        AtomicDEVS.__init__(self, name)
        if isinstance(state, TrafficLightState):
            self.state = state
        else:
            print("error in init of trafficLightModel")
            exit(1)
        self.OUT_JAM = self.addOutPort("out_going_jam")

    def intTransition(self):
        self.state.internal()
        return self.state

    def outputFnc(self):
        control = self.state.output_control()
        rv = {}
        if control is not None:
            rv[self.OUT_JAM] = control
        return rv

    def timeAdvance(self):
        return self.state.calculate_time_advance()
