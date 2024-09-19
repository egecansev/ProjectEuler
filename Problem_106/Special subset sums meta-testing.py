from time import time
from itertools import combinations


def multiplicative_combination_check(A, a):
    count = 0
    combos = []
    combo = list(combinations(A, a))
    for combined in combo:
        aux_combined = []
        for item in A:
            if item not in combined:
                aux_combined.append(item)
        if (tuple(aux_combined), combined) in combos:
            break
        combos.append((combined, tuple(aux_combined)))
        right = []
        left = []
        for p in range(len(combined)):
            for item in combined[p]:
                left.append(item)
            for item in aux_combined[p]:
                right.append(item)
        if len(left) < len(right):
            length = len(left)
            for p in range(length):
                if left[length - p - 1] in right:
                    right.remove(left[length - p - 1])
                    left.pop(length - p - 1)
            if len(left) != 0 and len(right) != 0:
                count += 1
        elif len(left) > len(right):
            length = len(right)
            for p in range(length):
                if right[length - p - 1] in left:
                    left.remove(right[length - p - 1])
                    right.pop(length - p - 1)
            if len(left) != 0 and len(right) != 0:
                count += 1
        else:
            if sorted(left) != sorted(right):
                count += 1
    return count


def factorial(p):
    multiplication = 1
    if p == 0:
        return 1
    while p:
        multiplication *= p
        p -= 1
    return multiplication


def calculate_combination(p, r):
    return factorial(p) // (factorial(r) * factorial(p - r))


start = time()
n = 12
m = n
sum_set = range(n)
total = 0
if n % 2:
    n -= 1
for i in range(1, n // 2):
    numbers = []
    for j in range(2*(i+1)):
        number = []
        for k in range(j):
            number.append('e' + str(k+1))
        numbers.append(number)
    total += calculate_combination(m, 2*(i+1)) * multiplicative_combination_check(numbers, i + 1)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
