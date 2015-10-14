class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)
        
    def getX(self):
        #Getter method for a Coordinate object's x coordinate.
        #Getter methods are better practice than just accessing an 
        #   attribute directly
        return self.x
        
    def getY(self):
        return self.y
      
    def __eq__(self, other):
        #first make sure they are of the same type
        assert type(other) == type(self)
        #return self.getX == other.getX and self.getY == other.getY
        return self.x == other.x and self.y == other.y
           
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ', ' +str(self.getY()) + ')'
    
    def distance(self, other):
        import math
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
c = Coordinate(4, 7)
print c.x, c.y

origin = Coordinate(34, 95)
print origin.x, origin.y

isinstance(c, Coordinate)

c.distance(origin) #using a method with two instances
