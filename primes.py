"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isItPrime(y):
    for i in range(2, 8):
        if y % i == 0:
            return True
        else:
            return False

def primes(number_of_primes):
    list = []
    y = 0
    while(len(list) < number_of_primes):
        y += 1
        if isItPrime(y):
            primes.append(y)
    return list
