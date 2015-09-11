def lenIter(aStr):
    """
    counts the number of characters in a string
    """
    count = 0
    for a in aStr:
        count += 1
    return count
    
def lenRecur(aStr):
    """
    count the length of a string using recursion
    """
    if aStr == '':
        return 0
    return 1 + lenRecur(aStr[1:])
    

    
