def lenRecur(aStr):
    '''
    aStr: a str
    returns: int, the length of aStr
    '''
    assert isinstance(aStr, str), 'Wrong argument type'
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])

