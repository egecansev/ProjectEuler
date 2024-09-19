from time import time


def calculate_hypotenuse(x):
    global total
    a = (2 * x + 1)/3
    if int(a) == a:
        perimeter = 3 * a - 1
        if perimeter >= perimeter_limit:
            return 1
        total += perimeter
    a = (2 * x - 1) / 3
    if int(a) == a:
        perimeter = 3 * a + 1
        if perimeter >= perimeter_limit:
            return 1
        total += perimeter
    return 0


def solve_pell_equation():
    x = solutions[0][0] * solutions[-1][0] + n * solutions[0][1] * solutions[-1][1]
    y = solutions[0][0] * solutions[-1][1] + solutions[0][1] * solutions[-1][0]
    if calculate_hypotenuse(x):
        return 0
    else:
        solutions.append((x, y))
        return solve_pell_equation()


start = time()
total = 0
perimeter_limit = 10**9
solutions = [(2, 1)]
n = 3
solve_pell_equation()
new_total = 0
print(int(total))
end = time()
print("Time elapsed", end - start, "seconds")
