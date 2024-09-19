from math import sqrt
import time

start = time.time()
count = 0
for m in range(2,10001):
    a0 = int(sqrt(m))
    if int(a0*a0) == m:
        continue
    guttus = []
    k = 1
    n = a0
    counter = 0
    while True:
        x = int(k/(sqrt(m)-n))
        y = (m-n*n)/k
        z = -(n-x*(m-n*n)/k)
        a = x
        k = int(y)
        n = int(z)
        guttus.append(a)
        if guttus[-1] == 2 * a0:
            if len(guttus) % 2:
                count += 1
            break
end = time.time()
print(count)
print("Time elapsed is ", end - start, " seconds")
