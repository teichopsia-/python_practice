def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("Intermediate result for ", n, " * factorial(" , n-1, "): ", res)
        return res
        
print(factorial(5))

def iterative_factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
    
print
print(iterative_factorial(5))
