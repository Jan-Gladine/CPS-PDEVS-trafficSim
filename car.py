class Car(object):
    def __init__(self, speed_adapter, creation_time):
        self.speed_adapter = speed_adapter
        self.current_position_on_segment = 0
        self.creation_time = creation_time
        self.distance_done = 0

    def __str__(self):
        return "pos: " + str(self.current_position_on_segment) + " ct = " + str(self.creation_time) + " distance= " + str(self.distance_done)
