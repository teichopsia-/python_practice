def count7(N):
    '''
    N: a non-negative integer
    Using recursion, count and return the number of ocurrences 
    of the digit 7 in N
    '''
    n = str(N)
    if not n:
        return 0
    else:
        return (n[0] == "7") + count7(n[1:])
    

