def lenIter(aStr):
    '''
    aStr: a str
    returns: int, the length of aStr
    '''
    assert isinstance(aStr, str), 'Wrong argument type'
    count = 0
    for letter in aStr:
        count += 1
    return count
