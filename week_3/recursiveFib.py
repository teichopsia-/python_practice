def fiboRecur(n):
    '''
    assumes x is an int >= 0
    returns Fibonnacci of n
    '''
    assert type(n) == int and n >= 0
    if n <= 1:
        return 1
    return fiboRecur(n - 1) + fiboRecur(n - 2)
