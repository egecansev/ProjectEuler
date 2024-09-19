from time import time

start = time()
product_num = 1
product_den = 1
for i in range(10, 100):
    for j in range(i+1, 100):
        if str(i)[1] == str(j)[0] and str(j)[1] != "0":
            if i/j == int(str(i)[0])/int(str(j)[1]):
                product_num *= i
                product_den *= j
print(product_den/product_num)
end = time()
print('Time elapsed', end - start, 'seconds')
