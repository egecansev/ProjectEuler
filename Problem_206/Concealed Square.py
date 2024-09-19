from time import time


def is_bulls_eye(number):
    for x in range(2, 10):
        if str(number)[2 * (x - 1)] != str(x):
            return False
    return True


start = time()
minimum = ''
for i in range(1, 10):
    minimum += '0'
    minimum += str(i)
minimum = str(int(int(minimum) ** 0.5))
i = int(minimum[:-1] + '3')
while i < (2 ** 0.5) * 10 ** 8:
    if is_bulls_eye(i * i):
        print(i * 10)
        break
    if str(i)[-1] == '3':
        i += 4
    else:
        i += 6

end = time()
print('Time elapsed', end - start, 'seconds')
