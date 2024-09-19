from time import time
from collections import Counter


def eq(a, b, c, n):
    return 2 * (a*b+b*c+a*c) + 4 * (n-1) * (a+b+c+n-2)


start = time()
limit = 20000
target = 1000
values = []
for i in range(1, (limit - 1)//2):
    for j in range(1, i+1):
        if 2*(i*j+i+j) > limit:
            break
        for k in range(1, j+1):
            if 2 * (i * j + i * k + j * k) > limit:
                break
            for m in range(1, limit):
                val = eq(i, j, k, m)
                if val > limit:
                    break
                values.append(val)

print(min([key for key, val in Counter(values).items() if val == target]))
end = time()
print('Time elapsed', end - start, 'seconds')
