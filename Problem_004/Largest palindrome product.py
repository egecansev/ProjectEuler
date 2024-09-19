from time import time


def is_palindrome(n):
    n = str(n)
    for m in range(len(n) // 2):
        if n[m] != n[-(m+1)]:
            return False
    return True


start = time()
digits = 3
max_palindrome = 0
numbers = list(reversed(range(10**(digits - 1), 10**digits)))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        number = numbers[i] * numbers[j]
        if number < max_palindrome:
            break
        elif is_palindrome(number) and max_palindrome < number:
            max_palindrome = number
print(max_palindrome)
end = time()
print('Time elapsed', end - start, 'seconds')
