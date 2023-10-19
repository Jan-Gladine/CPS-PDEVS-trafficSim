

class InterSection:
    def __init__(self, length, max_speed, name):
        """
        Constructor for an intersection
        :param length: The length of the road-section in meters
        :param max_speed: The maximum speed allowed on the road_section
        :return: none
        """
        self.length = length
        self.max_speed = max_speed
        self.queue = []
        self.jam_queue = []
        self.name = name