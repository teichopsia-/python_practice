s = 'azcbobobegghakl'

def alph(s):
    if len(s) <= 1:
        return s
    checker = s[0]
    final = ''
    for char in range(1, len(s)):
        if len(checker) > len(final):
            final = checker
        if s[char] >= s[char-1]:
            checker += s[char]
        else:
            checker = s[char]
    print 'Longest substring in alphabetical order is: {}'.format(final)
