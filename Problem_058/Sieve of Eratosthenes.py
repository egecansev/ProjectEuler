import timeit

start = timeit.default_timer()
num_set = []
prime = [2]
start_index = {}
k = 1
jump = 6
while True:

    if k == 1:
        for i in range(1, int(k*pow(10, jump)/2)):
            num_set.append(2*i+1)
    else:
        for i in range((k-1)*pow(10, jump), k*pow(10, jump)):
            num_set.append(i)

    for i in num_set:
        if i == -1:
            continue
        inc = i
        if k == 1:
            index = 1
            index_prime = 0
        else:
            if start_index.get(i) is None:
                index = 1
            else:
                index = int((start_index.get(i)-num_set.index(i))/inc)
            index_prime = 8+(k-2)*pow(10, jump)
        while num_set.index(i)+index*inc < len(num_set):
            if index and num_set[num_set.index(i)+index*inc] != -1:
                num_set[num_set.index(i)+index*inc] = -1
            index += 1
        index -= 1
        start_index[i] = num_set.index(i)+index*inc

    for i in range(index_prime, len(num_set)):
        if num_set[i] != -1:
            prime.append(num_set[i])

    k += 1
    if k == 2:
        stop = timeit.default_timer()
        break
print(prime)
print("Build primes:", stop-start)
