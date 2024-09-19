from time import time
from itertools import permutations


def is_prime(n):
    for j in range(2, round(n/2)):
        if n % j == 0:
            return False
    return True


start = time()
digit = []
pre = []
post = []
dummy = []
flag = 0
for i in range(1, 10):
    digit.append(str(i))
while True:
    pre = list(permutations(digit, len(digit)))
    for i in range(len(pre)):
        pre[i] = "".join(pre[i])
    pre = sorted(pre)
    for i in range(len(pre)):
        number = int(pre.pop())
        if number % 2 == 1:
            if is_prime(number):
                print(number)
                flag = 1
                break
    digit.pop()
    if flag:
        break
end = time()
print('Time elapsed', end - start, 'seconds')
