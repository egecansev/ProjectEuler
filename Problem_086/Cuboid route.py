from time import time
from numpy import gcd


def is_shortest(p, q, r):
    if r >= q >= p:
        return True
    else:
        return False


start = time()
ppt = []
trips = []
sol_lim = 10**6
error_margin = 10       # ADJUST IT TO FIND THE RIGHT SOLUTION - OPTIMAL VALUE IS 10
m = 2
count = 0
while count <= sol_lim*error_margin:
    for n in range(1, m):
        if gcd(m, n) == 1 and (m % 2)*(n % 2) != 1:
            x = m * m - n * n
            y = 2 * m * n
            ppt.append([sorted([x, y]), 1])
            ppt.sort(key=lambda s: s[0][1])

            for primitive in ppt:
                while primitive[0][1] * primitive[1] <= ppt[-1][0][1]:

                    a = primitive[0][0] * primitive[1]
                    b = primitive[0][1] * primitive[1]
                    for i in range(1, a):
                        j = a - i
                        k = b
                        if i > j:
                            break
                        if is_shortest(i, j, k):
                            trips.append([i, j, k])
                            count += 1
                    for i in range(1, b):
                        j = b - i
                        k = a
                        if i > j:
                            break
                        if is_shortest(i, j, k):
                            trips.append([i, j, k])
                            count += 1
                    primitive[1] += 1

    m += 1

print(sorted(trips, key=lambda s: int(s[2]))[sol_lim][2])

end = time()
print("Time elapsed", end-start, "seconds")
