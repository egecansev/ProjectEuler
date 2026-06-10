from time import time


def collatz(n):
    count = 1
    while True:
        if n == 1:
            return count
        elif n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        count += 1


start = time()
max_term = 0
max_num = 0
for i in range(500000, 1000000):
    temp = collatz(i)
    if max_term < temp:
        max_term = temp
        max_num = i
print(max_num)
end = time()
print('Time elapsed', end - start, 'seconds')
