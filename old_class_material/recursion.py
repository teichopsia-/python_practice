def mult_rec(a, b):
    """
    multiply a number using addition
    """
    if b == 1:
        return a
    else:
        return a + mult_rec(a, b - 1)
        
        
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
        
print factorial(1)
print factorial(2)
print factorial(3)
print factorial(4)


def iterPower(base, exp):
    """
    returns the exponential base using recursive mutliplication
    """
    if exp < 1:
        return 1
    return base * iterPower(base, exp - 1)
    
print iterPower(3, 2), "iterPower"

def recurPowerNew(base, exp):
    """
    recursive multiplication depending if its odd or even
    """
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    return base * recurPowerNew(base, exp - 1)
    
def gcdIter(a, b):
    """
    a, b: positive integers
    returns a positive integer, the greatest common divisor of
    a and b
    """
    testValue = min(a, b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
        count += 1
    return testValue
    
print gcdIter(6, 28)


def gcdRecur(a, b):
    """
    returns the greatest common divisor of a & b
    """
    if b == 0:
        return a
    return gcdRecur(b, a % b)
        
