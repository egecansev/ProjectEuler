from time import time


def is_bouncy(n):
    order = 0
    indecisive = 0
    for i in range(len(n) - 1):
        if int(n[i]) < int(n[i + 1]):
            order = 1
            break
        elif int(n[i]) > int(n[i + 1]):
            order = -1
            break
        else:
            indecisive += 1
    if order:
        for i in range(indecisive, len(n) - 1):
            if 0 > order * (int(n[i + 1]) - int(n[i])):
                return True
    return False


start = time()
number = 1
count = 0
while True:
    if is_bouncy(str(number)):
        count += 1
    if count == 0.99 * number:
        break
    number += 1
print(number)
end = time()
print('Time elapsed', end - start, 'seconds')
