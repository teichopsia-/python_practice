def primeList(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    primes = []
    not_prime = []
    #numbers = range(2, N+1)
    
    for prime in range(2, N+1):
        if all(prime%i != 0 for i in range(2, prime)):
            primes.append(prime)
            
    
    return sorted(primes)
