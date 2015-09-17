def applyToEach(L, f):
    '''
    assumes L is a list, f a function
    mutates L by replacing each element,
    e, of L by f(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
        print L[i]

testList = [1, -4, 8, -9] 

def add(a):
    return a + 1
    
def double(a):
    return abs(a * a)
        
L = [1, -2, 3.4]

applyToEach(L, abs)
print L

applyToEach(L, int)
print L

applyToEach(testList , add)
print L

applyToEach(L, fib)
print L

def applyFuncs(L, x):
    for f in L:
        print(f(x))
        
applyFuncs([abs, int, fact, fib], 4)
# would return the following.
#4
#4
#24
#5


# Map does the same as the above function
map(abs, [1, -2, 3, -4])


L1 = [1, 28, 36]
L2 = [2, 57, 9]
map(min, L1, L2)

# returns [1, 28, 9]
