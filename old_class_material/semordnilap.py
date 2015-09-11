def semordnilapWrapper(str1, str2):
    # a single length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False
    
    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
        
    return semordnilap(str1, str2)
    
def semordnilap(str1, str2):
    """
    checks if two words can be read backwords, like a palindrom
    """
    # if strings are not the same length, False
    if len(str1) != len(str2):
        return False

    # Base case: if the strings are each of length 1, check if they're equal
    if len(str1) == 1:
        return str1 == str2
        
    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False
    
    
