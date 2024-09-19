from time import time


def generate_pentagonal(n):
    return [int((3 * n * n - n) / 2), int((3 * n * n + n) / 2)]


def generate_partition(n):
    i = 0
    p = 0
    while i < n:
        pent_num = pentagonal_numbers[i]
        if n >= pent_num[0]:
            p += ((-1) ** i) * partitions[n - pent_num[0]]
        else:
            break
        if n >= pent_num[1]:
            p += ((-1) ** i) * partitions[n - pent_num[1]]
        else:
            break
        i += 1
    return p % 10 ** 6


start = time()
pentagonal_numbers = []
partitions = [1]
x = 1
while True:
    pentagonal_numbers.append(generate_pentagonal(x))
    partitions.append(generate_partition(x))
    if partitions[-1] % (10 ** 6) == 0:
        break
    x += 1
print(x)
end = time()
print("Time elapsed", end - start, "seconds")
