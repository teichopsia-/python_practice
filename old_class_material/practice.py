def max(x, y):
    if x > y:
        return x
    else:
        return y
        
z = max(3, 4)

def a(x, y, z):
    if x:
        return y
    else: 
        return z
        
def b(q, r):
    return a(q > r, q, r)
    
def odd(x):
    return x % 2 == 1
    
    
def isVowel(char):
    """ char: a single letter of any case. It can be upper or lower
    returns True if char is a vowel and False otherwise.
    """
    if char == 'A' or char == 'a' or char == 'E' \
    or char == 'e' or char == 'I' or char == 'i' \
    or char == 'O' or char == 'o' or char == 'U' \
    or char == 'u':
        return True
    else:
        return False
        
        
def isVowel2(char):
    """ char: a single letter of any case. It can be upper or lower
    returns True if char is a vowel and False otherwise.
    """
    if char in 'aeiou' or char in 'AEIOU':
        return True
    return False
    
    
def isVowel3(char):
    """ char: a single letter of any case. It can be upper or lower
    returns True if char is a vowel and False otherwise.
    """
    return char.lower in 'aeiou'
    
    
def isVowel4(char):
    """ char: counts the number of vowels in a string """
    count = 0
    for c in char:
        if c in 'aeiou':
            count += 1
    return "Number of vowels: ", count
    
    
def isVowel4(char):
    """ char: number of times the word bob occurs in a string """
    numBobs = 0
    for i in range(1, len(s)-1):
        if s[i-1:i+2] == 'bob':
            numBobs += 1
    print 'Number of times bob occurs is:', numBobs
    
    
def longest(word):
    """ Longest substring in alphabetical order """
    
    curString = s[0]
    longest = s[0]
    for i in range(1, len(s)):
        if s[i] >= curString[-1]:
            curString += s[i]
            if len(curString) > len(longest):
                longest = curString
        else:
            curString = s[i]
    print 'Longest substring in alphabetical order is:', longest
