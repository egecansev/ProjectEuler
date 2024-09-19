from time import time
from itertools import combinations
from urllib import request


def equal_length_subsets_check(A, a, b):
    combs = list(combinations(A, a + b))
    combos = []
    for comb in combs:
        combo = list(combinations(comb, a))
        for combined in combo:
            aux_combined = []
            for item in comb:
                if item not in combined:
                    aux_combined.append(item)
            if (tuple(aux_combined), combined) in combos:
                break
            if sum(combined) == sum(aux_combined):
                return False
    return True


def inequal_length_subsets_check(A):
    for i in range(1, (len(A) + 1) // 2):
        left = A[0]
        right = 0
        for j in range(1, i + 1):
            left += A[j]
            right += A[-j]
        if left <= right:
            return False
    return True


def is_special_sum_set(A):
    if not inequal_length_subsets_check(A):
        return False
    for i in range(2, len(A)//2 + 1):
        if not equal_length_subsets_check(A, i, i):
            return False
    return True


start = time()
total = 0
data = request.urlopen("https://projecteuler.net/project/resources/p105_sets.txt")
for line in data:
    sum_set = sorted(list(map(int, line.decode("utf-8").rstrip("\n").split(','))))
    if is_special_sum_set(sum_set):
        total += sum(sum_set)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
