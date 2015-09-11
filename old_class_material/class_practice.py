import math

class Coordinate(object):
    """ class documentation """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "<" + str(self.x)+ ", " + str(self.y) + ">"
        
    def distance(self, other):
        return math.sqrt((self.x - other.x) + (self.y - other.y))
        
first = Coordinate(3, 5)
second = Coordinate(2, 5)

first.distance(second)
#this line invokes the distance procedure within the class
