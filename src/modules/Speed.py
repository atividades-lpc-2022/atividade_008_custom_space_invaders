class Speed:
    def __init__(self, x_speed: float, y_speed: float):
        self.x_speed = x_speed
        self.y_speed = y_speed

    def invert_x(self):
        self.x_speed *= -1

    def invert_y(self):
        self.y_speed *= -1
