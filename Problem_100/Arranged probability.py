from time import time


def solve_negative_pell_equation_for_n_equals_two():
    global solutions
    x = 3 * solutions[0] + 4 * solutions[1]
    y = 2 * solutions[0] + 3 * solutions[1]
    solutions = (x, y)
    if y > (2**0.5) * (10 ** 12):
        return y
    else:
        return solve_negative_pell_equation_for_n_equals_two()


start = time()
solutions = (7, 5)
print(int((solve_negative_pell_equation_for_n_equals_two() + 1) / 2))
end = time()
print('Time elapsed', end - start, 'seconds')
