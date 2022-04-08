from modules.Coordinate import Coordinate
from modules.Dimension import Dimension


class Element:
    def __init__(self, coordinate: Coordinate, dimension: Dimension):
        self.coordinate = coordinate
        self.dimension = dimension
