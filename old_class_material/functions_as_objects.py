# Immutable objects: int, float, str, tuple
# Mutable: Lists

x = [1, 2, [3, 'John', 4], 'Hi'] 

sum(range(len(x))


def applyToEach(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result
    
def square(a):
    return a * a
    
def halve(a):
    return a / 2
    
def inc(a):
    return a + 1
    
applyToEach([inc, square, halve, abs], -3)

