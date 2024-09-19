from time import time
from itertools import product, permutations
from copy import deepcopy


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def read_operation(series):
    for i in range(3):
        result = 0
        operator = series.pop(1)
        if operator == '+':
            result += add(series.pop(0), series.pop(0))
        elif operator == '-':
            result += subtract(series.pop(0), series.pop(0))
        elif operator == '*':
            result += multiply(series.pop(0), series.pop(0))
        elif operator == '/':
            result += divide(series.pop(0), series.pop(0))
        series = [result] + series
    if int(series[0]) == series[0] and series[0] > 0:
        return int(series.pop())


def read_operation_with_parenthesis(serie):
    count = 0
    while '/' in serie:
        result = 0
        div_index = serie.index('/')
        serie.pop(div_index)
        result += divide(serie.pop(div_index-1), serie.pop(div_index-1))
        serie.insert(div_index-1, result)
        count += 1
    for i in range(3 - count):
        result = 0
        operator = serie.pop(1)
        if operator == '+':
            result += add(serie.pop(0), serie.pop(0))
        elif operator == '-':
            result += subtract(serie.pop(0), serie.pop(0))
        elif operator == '*':
            result += multiply(serie.pop(0), serie.pop(0))
        elif operator == '/':
            result += divide(serie.pop(0), serie.pop(0))
        serie = [result] + serie
    if int(serie[0]) == serie[0] and serie[0] > 0:
        return int(serie.pop())


start = time()
max_index = 0
operators = ['+', '-', '*', '/']
op_perm = list(list(comb) for comb in product(operators, repeat=3))
for x in range(1, 10):
    for y in range(x+1, 10):
        for z in range(y + 1, 10):
            for w in range(z + 1, 10):
                numbers = [x, y, z, w]
                num_perm = list(map(list, permutations(numbers)))
                operation = []
                results = []
                for num in num_perm:
                    for op in op_perm:
                        operation = deepcopy(num)
                        for n in range(3):
                            operation.insert(2*n+1, op[n])
                        res = read_operation(deepcopy(operation))
                        if res is not None:
                            results.append(res)
                        if '/' in operation:
                            res = read_operation_with_parenthesis(operation)
                        if res is not None:
                            results.append(res)
                results = sorted(set(results))
                for val in results:
                    if val - results.index(val) != 1:
                        if val > max_index:
                            max_index = val
                            max_series = numbers
                        break
print(''.join(str(value) for value in max_series))

end = time()
print("Time elapsed", end-start, "seconds")
