from time import time


def get_digit_sum(n):
    total = 0
    divisor = 10
    while n:
        total += n % divisor
        n //= divisor
    return total


def get_interesting_solution(n):
    count = 0
    digits = 2
    while True:
        for i in range(2, digits * 9 + 1):
            j = i
            power = 2
            while j < 10 ** (digits - 1):
                j = i ** power
                power += 1
            while j < 10 ** digits:
                if get_digit_sum(j) == i:
                    count += 1
                    if count == n:
                        return j
                j = i ** power
                power += 1
        digits += 1


start = time()
print(get_interesting_solution(30))
end = time()
print('Time elapsed', end - start, 'seconds')
