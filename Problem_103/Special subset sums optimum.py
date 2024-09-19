from time import time
from itertools import combinations


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


def successor(n, l):
    idx = []
    for j in range(len(l)):
        if l[j] < l[0] - 1:
            idx.append(j)
    if not idx:
        return False

    i = idx[0]
    l[1:i+1] = [l[i]+1] * (len(l[1:i+1]))
    l[0] = n - sum(l[1:])
    return True


def partitions(n, k, candidate):
    if candidate:
        l = list(reversed(candidate))
        l[0] += 1
        for i in range(1, len(l)):
            if l[-i] > 0:
                l[-i] -= 1
                break
    else:
        l = [0]*k
        l[0] = n
    while successor(n, l):
        if len(l) == len(set(l)) and 0 not in l and is_special_sum_set(sorted(l)):
            return sorted(l)
    return


def optimal_special_sum_set(n, length, near_optimal):
    total = 10**9
    start_val = length
    while True:
        solution = partitions(length, n, near_optimal)
        if solution and sum(solution) < total:
            optimal = solution
        length -= 2
        if near_optimal and length > 100:
            if solution:
                for i in range(len(near_optimal) - 1):
                    near_optimal[i] = solution[i] - 1
                near_optimal[-1] += len(near_optimal) - 1 - 2
            else:
                for i in range(len(near_optimal) - 1):
                    near_optimal[i] = near_optimal[i] - 1
                near_optimal[-1] += len(near_optimal) - 1 - 2
        if 1 == length or start_val - length > 3:
            return optimal


def opt_spe(n):
    j = 3
    near_optimum = []
    for i in range(2, n + 1):
        optimum = optimal_special_sum_set(i, j, near_optimum)
        j = (len(optimum) + 1) * optimum[len(optimum) // 2] + sum(optimum)
        near_optimum = generate_near_optimum(optimum)
    return ''.join([str(x) for x in optimum])


def generate_near_optimum(optimum):
    b = optimum[len(optimum) // 2]
    near_optimum = [b]
    for a in optimum:
        near_optimum.append(a + b)
    return near_optimum


start = time()
print(opt_spe(7))
end = time()
print('Time elapsed', end - start, 'seconds')
