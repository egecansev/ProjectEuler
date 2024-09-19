import time
from itertools import permutations


start = time.time()
group = []
probabilities = []
solution = 0
comb = [7, 8, 9, 10]
remaining = [1, 2, 3, 4, 5]
perm_top = list(permutations(comb))
perm_bottom = list(permutations(remaining))
probabilities.append([perm_top, perm_bottom])

for prob in probabilities:
    for perm in prob[0]:
        a = 6
        b = perm[0]
        c = perm[1]
        d = perm[2]
        e = perm[3]
        top = [a, b, c, d, e]
        for bottom in remaining:
            f = bottom
            top = [a, b, c, d, e]
            top.append(f)
            h = f + a - b
            if h > 9 or h < 1 or h in top:
                continue
            top.append(h)
            j = h + c - d
            if j > 9 or j < 1 or j in top:
                continue
            top.append(j)
            g = j + e - a
            if g > 9 or g < 1 or g in top:
                continue
            top.append(g)
            i = g + b - c
            if i > 9 or i < 1 or i in top:
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
print("Time elapsed", time.time() - start, "seconds")
