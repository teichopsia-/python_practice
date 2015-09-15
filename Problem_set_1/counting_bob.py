s = 'azcbobobegghakl'

def bob(s):
    count = 0
    index = 0
    while index < len(s):
        index = s.find('bob', index)
        if index == -1:
            break
        #print('bob found at', index)
        index += 2
        count += 1

    print 'Number of times bob occurs is: {}'.format(count)
