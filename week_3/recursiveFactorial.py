def fact(n):
    '''
    assumes that n is an int > 0
    return n! iteratively
    '''
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result
    

def factR(n):
    '''
    assumes that n is an int > 0
    return n! recursively
    '''
    if n == 1:
        return n
    else:
        return n * factR(n - 1)
