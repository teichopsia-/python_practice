def genFib():
    fib_1 = 1
    fib_2 = 0
    while True:
        next = fib_1 + fib_2
        yield next
        fib_2 = fib_1
        fib_1 = next

foo = genFib()
foo.next() #call each time to get the enxt one.

for n in genFib():
    count += 1
    print n
    if count > 100:
        break

