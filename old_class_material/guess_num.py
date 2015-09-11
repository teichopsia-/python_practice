user_num = int(raw_input('Please think of a number between 0 and 100! '))

low = 0
high = 100
guess = (high + low) / 2

while True:

    question = 'is your secret number ' + str(guess) + '? '
    print question
    print 
    check = raw_input('Enter \'h\' to indicate the guess is too high. Enter \'l\' \
to indicate the guess is too low. Enter \'c\' \
to indicate I guessed correctly. ')
    print    
    if check == 'c':
        print "Game over. Your secret number was: " + str(guess)
        break    
    elif check == 'h':
        high = guess
    elif check == 'l':
        low = guess
    else:
        print('Please enter a valid choice')
        print
    guess = (high + low) / 2
