from time import time


def is_pandigital(n):
    if "0" in str(n):
        return False
    for w in str(n):
        if w in str(n)[str(n).index(w)+1:]:
            return False
    return True


start = time()
pandigital_product = []
for i in range(1, 100):
    pandigital = ""
    if is_pandigital(i):
        for j in range(pow(10, 4-len(str(i))), pow(10, 5-len(str(i)))):
            pandigital = ""
            if is_pandigital(j):
                pandigital += str(i)
                pandigital += str(j)
                if is_pandigital(int(pandigital)):
                    product = i*j
                    if is_pandigital(product):
                        pandigital += str(product)
                        if len(pandigital) == 9:
                            if is_pandigital(int(pandigital)):
                                pandigital_product.append(product)
total = 0
pandigital_product = set(pandigital_product)
while len(pandigital_product):
    total += pandigital_product.pop()
print(total)
end = time()
print('Time elapsed', end - start, 'seconds')
