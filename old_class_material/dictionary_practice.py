animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


{'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}

def howMany(animals):
    """
    returns the number of values in a dictionary
    which holds lists of values
    """
    #            len(animals)      = 4
    #            len(animals['d']) = 3
    count = 0
    for key, val in animals.items():
        for k in val:
            count += 1
    return count
    
# another way to solve this
for value in animals.values():
    result += len(value)
    
# and another one
for key in animals.keys():
    result += len(animals[key])

animals = {'a': ['aardvark'], 'c': ['coati'], 'b': ['baboon'], 'd': ['donkey', 'dog', 'dingo']}

def biggest(animals):
    """
    Returns the maximum value of a key in a dictionary
    """
    return max(animals, key=animals.get)
    # Correct answer
    result = None
    biggestValue = 0
    for key in animals.keys():
        if len(animals[key]) >= biggestValue:
            result = key
            biggestValue = len(animals[key])
    return result
        
