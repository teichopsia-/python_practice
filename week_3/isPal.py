pali = 'Able was I ere I saw Elba'

def isPalindrome(word):
    '''
    Returns True if a word or a phrase is a palindrome
    '''
    
    word = word.lower().replace(' ', '')
    
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and isPalindrome(word[1:-1])
