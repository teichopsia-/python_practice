class Queue(object):
    """ First in first out
    represented as a list
    """
    def __init__(self):
        """ creates an empty list """
        self.value = []
        
    def __str__(self):
        return str(self.value)
        
    def insert(self, var):
        """ inserts a new element """
        self.value.append(var)
            
    def remove(self):
        """ removes an item """
        if self.value == []:
            raise ValueError()
        else:
            var = self.value[0]
            self.value.remove(var)
            return var   
        # could also be written as:
        # return self.value.pop(0)
   #     try:
   #         self.value.remove(another_var)
   #     except:
   #         raise ValueError(str(another_var) + 'not found')
