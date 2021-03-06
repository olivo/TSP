import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 +
                         (self.y - other_point.y)**2)

    def str(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
