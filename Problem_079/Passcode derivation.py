from time import time
from urllib import request


def is_always():
    visited = []
    for code in codes:
        if code:
            flag = 1
            suspect = code[0]
            if suspect not in visited:
                for code in codes:
                    if suspect in code:
                        if code.index(suspect) != 0:
                            flag = 0
                            visited.append(suspect)
                            break
                if flag:
                    return suspect


start = time()
data = request.urlopen("https://projecteuler.net/project/resources/p079_keylog.txt")
global codes
codes = []
password = ''
for line in data:
    code = str(line)[2:5]
    codes.append(code)
while codes:
    first = is_always()
    password += first
    for code in codes:
        codes[codes.index(code)] = code.strip(first)
    codes = list(filter(None, codes))
print(password)
end = time()
print("Time elapsed", end-start, "seconds")
