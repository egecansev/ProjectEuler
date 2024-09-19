from time import time
start = time()
number = ""
i = 1
while len(number) < pow(10, 6)+1:
    number += str(i)
    i += 1
const = 1
for i in range(7):
    const *= int(number[pow(10, i)-1])
print(const)
end = time()
print("Time elapsed", end-start, "seconds")
