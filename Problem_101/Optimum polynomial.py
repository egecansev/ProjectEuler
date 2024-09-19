from time import time
from numpy import linalg, zeros, round


def op(k, n):
    output = zeros(n).transpose()
    parameters = zeros((n, n))
    for i in range(n):
        output[i] = correct_series[i]
        for j in range(n):
            parameters[i][j] = (i + 1)**(n-1-j)
    coefficients = round(linalg.inv(parameters).dot(output), 2)
    series = []
    for i in range(1, k):
        total = 0
        exponent = len(coefficients)-1
        for coefficient in coefficients:
            total += coefficient * (i**exponent)
            exponent -= 1
        series.append(total)
    return series


start = time()
series_length = 12
correct_series = []
for a in range(1, series_length):
    term = 0
    for b in range(series_length-1):
        term += (-a)**b
    correct_series.append(term)
length = 1
fit = []
while True:
    bop = op(series_length, length)
    length += 1
    for index in range(len(bop)):
        if bop[index] != correct_series[index]:
            fit.append(bop[index])
            break
    if bop == correct_series:
        break
print(int(sum(fit)))
end = time()
print('Time elapsed', end - start, 'seconds')
