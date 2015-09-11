def isIn(char, aStr):
    """
    Using bisection search, determine if a character
    is in a string, as long as it is sorted in 
    alphabetical order.
    """
    # Base case: if aStr is empty, no character to be found 
 
    if aStr == "":
        return False
    # Base case: if aStr is of length 1, check if characters
    # are equal.
    if len(aStr) == 1:
        return aStr == char
        
    middle_of_string = len(aStr) / 2 # + 1 character
    middle_character = aStr[middle_of_string]
    if char == middle_character:
        return True
    # Recursive case: if the character is smaller than the middle
    # character, recursively search on the first half of aStr
    elif char < middle_character:
        return isIn(char, aStr[:middle_of_string])
    # otherwise, check the larger middle
    else:
        return isIn(char, aStr[middle_of_string + 1:])
        
