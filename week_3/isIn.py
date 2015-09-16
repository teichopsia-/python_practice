# Couldn't figure this one out.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
        return aStr == char
    
    # Base case: See if the character is in the middle of aStr
    midIndex = len(aStr) / 2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
        
    # Recursive case: If the test character is smaller than the middle
    # character, recursively search on the first half of aStr
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex + 1:])
