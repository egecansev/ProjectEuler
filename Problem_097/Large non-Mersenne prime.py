from time import time

start = time()
number = 1
count = 0
while len(str(number)) < 10:
    number *= 2
    count += 1
exponent = int(7830457 / count)
remainder = 7830457 % count
shortened = 1
for i in range(exponent):
    shortened = int(str(shortened * number)[-10:])
shortened = int(str(shortened * 28433 * (2 ** 7) + 1)[-10:])
print(shortened)
end = time()
print("Time elapsed", end-start, "seconds")
