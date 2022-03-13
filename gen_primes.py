#!/usr/bin/env python3

# Write a generator, gen_primes, that returns the sequence of prime
# numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...


def gen_primes():
    count = 2
    while count:
        for num in range(2, count):
            if not count % num:
                break
        else:
            yield count
        count += 1


prime = gen_primes()
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
