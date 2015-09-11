def mult1(a, b):
    """
    multiply a number by adding it n times using a for loop
    """
    i = b
    result = 0
    for x in range(i):
        result += a
    return result
    
#print    
#print(mult1(4, 3), "mult1")
#print

def mult2(a, b):
    """
    multiply a number by adding it n times
    """
    result = 0
    for x in range(b):
        result += a
    return result
    
#print(mult2(2, 3), "mult2")        

def mult3(a, b):
    """
    multiply a number by adding it n times using a while loop
    """
    i = b
    result = 0
    while i > 0:
        i -= 1
        result += a
    return result
    
#print
#print(mult3(2, 3), "mult3")

def mult4(a, b):
    """
    multiply a number by adding it n times using a while loop
    """
    result = 0
    while b > 0:
        b -= 1
        result += a
    return result
    
def iterPower(base, exp):
    """
    returns the exponential base using mutliplication
    """
    result = 1
    while exp > 0:
        exp -= 1
        result *= base
    return result

print
print(iterPower(5, 2), "iterPower")
