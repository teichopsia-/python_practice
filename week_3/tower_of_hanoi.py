def printMove(fr, to):
    print 'move from: {}, to: {}'.format(fr, to)
    
def towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)
