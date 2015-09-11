numbers = [1, 3, 5, 7, 9]

def suming(lst):
    count = 0
    for n in lst:
        count += n
    return count
    
def sum_list(numList):
    if len(numList) == 1:
        return numList[0]
    return numList[0] + sum_list(numList[1:])
    
def fib(n):
    """
    recursive fibonacci
    """
    if n <= 1:
        return 1
    return n + fib(n - 1)
    
    
def oddTuples(aTup):
    """
    Returns every other element in a tuple
    """
    newATup = aTup[1::2]
    return newTup
