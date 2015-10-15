class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once.
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []
        
    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)
            
    def member(self, e):
        """ Assumes e is an integer. Returns True if e is in self """
        return e in self.vals
    
    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raise ValueError if e is not in sel f
        """
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, other):
        """ Return a new intSet containing elements that 
        appear in both sets
        """
        # Initialize a new inteSet()
        commonValueSet = intSet()
        for val in self.vals:
            # check if each value is a member of the other set
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet
    
    def __len__(self):
        """ Returns the legnth of the set """
        return len(self.vals)
    
    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
