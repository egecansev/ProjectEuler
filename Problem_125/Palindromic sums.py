from time import time


def is_palindrome(n):
    n = str(n)
    for m in range(len(n) // 2):
        if n[m] != n[-(m+1)]:
            return False
    return True


start = time()
limit = 10**8
solutions = []
pyramid_numbers = []
for i in range(int(limit**0.5) + 1):
    pyramid_numbers.append(i * (i + 1) * (2 * i + 1) // 6)
pyramid_numbers.reverse()
for i in range(len(pyramid_numbers)):
    for j in range(i + 2, len(pyramid_numbers)):
        number = pyramid_numbers[i] - pyramid_numbers[j]
        if number > limit:
            break
        if is_palindrome(number):
            solutions.append(number)
print(sum(set(solutions)))
end = time()
print('Time elapsed', end - start, 'seconds')
