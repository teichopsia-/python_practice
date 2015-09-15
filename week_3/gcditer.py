# Couldn't figure this one out.

def gcdIter(a, b):
    '''
    a, b: positive integers
    returns a positive integer, the greates common divisor of a & b
    '''
    testValue = min(a, b)
    
    # keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
        print 'test Value: {}'.format(testValue)
    return testValue
