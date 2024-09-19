import time
from itertools import permutations, combinations
from copy import deepcopy

start = time.time()
group = []
probabilities = []
solution = 0
for i in range(1, 10):
    group.append(i)
combination_9_4 = list(combinations(group, 4))
for comb in combination_9_4:
    comb = list(comb)
    remaining = deepcopy(group)
    for junk in comb:
        remaining.remove(junk)
    comb.append(10)
    perm_top = list(permutations(comb))
    perm_bottom = list(permutations(remaining))
    probabilities.append([perm_top, perm_bottom])

for prob in probabilities:
    for perm in prob[0]:
        a = perm[0]
        b = perm[1]
        c = perm[2]
        d = perm[3]
        e = perm[4]

        for per in prob[1]:
            f = per[0]
            g = per[1]
            h = per[2]
            i = per[3]
            j = per[4]

            if a + f + g != b + g + h:
                continue
            else:
                if b + g + h != c + h + i:
                    continue
                else:
                    if c + h + i != d + i + j:
                        continue
                    else:
                        if d + i + j != e + j + f:
                            continue
            str1 = str(a) + str(f) + str(g)
            str2 = str(b) + str(g) + str(h)
            str3 = str(c) + str(h) + str(i)
            str4 = str(d) + str(i) + str(j)
            str5 = str(e) + str(j) + str(f)
            if (min(a, b, c, d, e)) == a:
                string = str1 + str2 + str3 + str4 + str5
            elif (min(a, b, c, d, e)) == b:
                string = str2 + str3 + str4 + str5 + str1
            elif (min(a, b, c, d, e)) == c:
                string = str3 + str4 + str5 + str1 + str2
            elif (min(a, b, c, d, e)) == d:
                string = str4 + str5 + str1 + str2 + str3
            else:
                string = str5 + str1 + str2 + str3 + str4
            if solution < int(string):
                solution = int(string)
print(solution)
print("Time elapsed", time.time()-start, "seconds")
