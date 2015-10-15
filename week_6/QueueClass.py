class Queue(object):
    def __init__(self):
    """ Initializes 1 attribute: a list to 
    keep track of the Q's elements
    """
        self.q = []
        
    def insert(self, e):
        self.q.append(e)
            
    def remove(self):
        try:
            return self.q.pop(0)
        except:
            raise ValueError()
