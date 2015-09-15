def iterPower(base, exp):
    '''
    multiplies base by itself exp times
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
