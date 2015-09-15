def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    print 'b: {}, a % b: {}, a: {}, b: {}'.format(b, a % b, a, b)
    return gcdRecur(b, a % b)
