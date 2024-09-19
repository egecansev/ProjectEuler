from math import sqrt
import time
from prior import offline


def repeats(string):
    for x in range(1, len(string)):
        substring = string[:x]

        if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
            # print(substring)
            return substring


start = time.time()
database = []
odds = []
evens =[]
[odds, evens] = offline()
count = 0
for m in range(2,10001):
    if m in odds:
        count = count + 1
        continue
    elif m in evens:
        continue
    else:
        a = int(sqrt(m))
        if int(a*a) == m:
            continue
        guttus = []
        k = 1
        n = a
        counter = 0
        while True:
            x = int(k/(sqrt(m)-n))
            y = (m-n*n)/k
            z = -(n-x*(m-n*n)/k)
            a = x
            k = int(y)
            n = int(z)
            guttus.append(a)
            counter = counter + 1
            if counter > 2*m:      #Check https://en.wikipedia.org/wiki/Periodic_continued_fraction
                break
        fractions = str(guttus).strip('[]')
        cycle = repeats(fractions)
        cycle = cycle.split()
        if cycle[0] == ",":
            cycle.pop(0)
        x = [m, len(cycle)]
        database.append(x)
        if len(cycle) % 2:
            count = count + 1
end = time.time()
print(count)
print("Time elapsed is ", end - start, " seconds")

