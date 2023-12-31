FLUID = 0
JAMMED = 1
FULL_JAM = 2
JAMMED_OUTPUT = 3
FULL_JAM_OUTPUT = 4
JAMMED_TO_FULL_JAM = 5

ROAD_LEFT = 0
ROAD_RIGHT = 1
ROAD_UP = 2
ROAD_DOWN = 3

JAM_CAR_SPOT_AVAILABLE = 0
TO_JAM = 1
TO_FLUID = 2

RED = "RED"
GREEN = "GREEN"
ORANGE = "ORANGE"


def calculate_time_from_distance_speed(speed, distance):
    """
    t = d/v
    :param speed: speed in km/h
    :param distance: the distance to travel
    :return time in seconds
    """
    return distance / (speed * (5 / 18))


def calculate_distance_from_time_speed(speed, time):
    """
    d = v*t
    :param speed: speed in km/h
    :param time: the time in seconds
    :return distance: the distance to travel
    """
    return speed * (5 / 18) * time
