from time import time
from copy import deepcopy


def is_prime(n):
    if (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i*i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def get_number(n):
    num = ""
    for i in n:
        num += i
    return int(num)


def insert_digit(digs, main):
    num_len = len(digs)
    possible_indexes = [x for x in range(num_len + 1)]
    for b in range(10):
        if b != main:
            for index in possible_indexes:
                digs.insert(index, str(b))
                if len(digs) == length:
                    if is_prime(get_number(digs)):
                        return get_number(digs)
                else:
                    inner_solution = insert_digit(deepcopy(digs), main)
                    if inner_solution:
                        return inner_solution
                digs.remove(str(b))
    return None


def insert_digit_to_solve(digs, main):
    solutions = []
    num_len = len(digs)
    if main:
        possible_indexes = [x for x in range(num_len + 1)]
    else:
        possible_indexes = [0, num_len]
        for i in digs:
            if i != str(main):
                if digs.index(i):
                    possible_indexes.pop()
                else:
                    possible_indexes.pop(0)
    for b in range(10):
        if b != main:
            for index in possible_indexes:
                digs.insert(index, str(b))
                if len(digs) == length:
                    if digs[0] != "0" and is_prime(get_number(digs)):
                        solutions.append(get_number(digs))
                else:
                    solutions += insert_digit_to_solve(deepcopy(digs), main)
                digs.pop(index)
    return solutions


def get_M(n):
    for recursion_level in range(1, length):
        if n:
            digits = [str(n)] * (length - recursion_level)
            solution = insert_digit(deepcopy(digits), n)
            if solution:
                return length - recursion_level
        else:
            digits = [str(n)] * (length - recursion_level - 1)
            for a in range(1, 10):
                for b in range(1, 10):
                    if b % 2 == 0 or b == 5:
                        continue
                    digits.append(str(b))
                    digits.insert(0, str(a))
                    if len(digits) == length and is_prime(get_number(digits)):
                        return length - recursion_level - 1
                    digits.remove(str(b))
                    digits.remove(str(a))


def get_primes(recursion_level, n):
    digits = [str(n)] * recursion_level
    solutions = insert_digit_to_solve(deepcopy(digits), n)
    return solutions


start = time()
length = 10
M = []
total = 0
for j in range(10):
    M.append(get_M(j))
    sols = set(get_primes(M[j], j))
    total += sum(sols)
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
