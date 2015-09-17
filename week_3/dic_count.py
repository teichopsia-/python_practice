animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print howMany(animals)
# 6

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for a in aDict:
        for b in aDict[a]:
            count += 1
    return count
    
### Other was of solving the problem ###


def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result
    
def howMany2(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

