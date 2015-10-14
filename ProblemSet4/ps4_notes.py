### DEALING ###

# A player is dealt a hand of n letters chosen at random
# Assume n=7 for now

# The player arranges the hand into as many words as they want out of the 
# letters, using each letter at most once.

# Some letters may remain unused (these won't be scored)


### SCORING ###

# The score of the hand is the sum of the scores for each word formed.

# The score for a word is the sum of the points for letters in the word, multiplied
# by the length of the word, plus 50 points of all n letters are used on the first 
# word created.

# A is worth 1
# B = 3
# C = 3
# D = 2
# E = 1
# SCRABBLE_LETTER_VALUES maps each lowercase letter to its Scrabble letter value

# example: 'weed' is worth 32 points (4+1+1+2), then multiplied by 
# len(weed) to get (4+1+1+2) * 4 = 32

# example: if n=7 and you make the word 'waybill' on the first try, it would be 
# worth 155 points.
# 'waybill' (4+1+4+3+1+1+1)*7=105, plus 50 for using all n letters.
