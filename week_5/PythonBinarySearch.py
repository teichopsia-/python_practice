# An iterative "Pythonic" search procedure
def search(L, element):
    for i in L:
        if e == element:
            return True
    return False
    
# The recursive way:
def rSearch(L, element):
    if element == L[0]:
        return True
    if len(L) == 1:
        return False
    return rSearch(L[1:], element)
    
# A recursive "Pythonic" binary search procedure:
def rBinarySearch(L, element):
    if len(L) == 1:
        return element == L[0]
    mid = len(L) / 2
    if L[mid] > element:
        return rBinarySearch(L[:mid], element)
    if L[mid] < element:
        return rBinarySearch(L[mid:], element)
    return True
