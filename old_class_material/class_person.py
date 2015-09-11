try:
    import datetime
except ImportError:
    raise ImportError('datetime not available')

class Person(object):
    """ A person class with certain properties """

    def __init__(self, name):
        """ A persons name and birthday """
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def getLastName(self):
        """ return self's last name """
        return self.lastName
        
    def setBirthday(self, month, day, year):
        """ set self's birthday to birthDate """
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        """ returns self's current age in days """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        """ return True if self's name is lexicographically less
        than other's name, and False otherwise """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
        
    #other methods 
    def __str__(self):
        """ return self's name """
        return self.name

