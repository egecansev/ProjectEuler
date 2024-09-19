def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, is_prime) in enumerate(a):
        if is_prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False
