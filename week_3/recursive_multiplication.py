def recurMul(a, b):
    ''' 
    Recursive algorithm that multiplies a * b
    '''
    # Base case for when there are no more computations.
    if b == 1:     
        return a
    else:
        # Recursive function reducing the problem by 1
        return a + recurMul(a, b - 1)
