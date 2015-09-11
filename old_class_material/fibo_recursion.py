def fibo(n):
    """
    Fibonacci using recursion
    """
    global numCalls
    numCalls += 1
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
        
def testFib(n):
    global numCalls

    for i in range(n+1):
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibo(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(10)
