def getPrimes(n):
    "Get all primes up to n"
    all_prime_numbers = list(range(0, n + 1))
    all_prime_numbers[1] = 0
    for i in range(len(all_prime_numbers)):
        if all_prime_numbers[i] != 0:
            for m in range(i * i, n + 1, i):
                all_prime_numbers[m] = 0

    c = all_prime_numbers.count(0)
    for i in range(c):
        all_prime_numbers.remove(0)
    return all_prime_numbers


x = 10000
print('De lijst met priemgetallen: ', getPrimes(x))