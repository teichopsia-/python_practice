def iterMul(a, b):
    '''
    Multiplication by iterative addition
    '''
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
