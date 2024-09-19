from urllib import request


data = request.urlopen("https://projecteuler.net/project/resources/p081_matrix.txt")
matrix = []
for line in data:
    line = str(line)[2:-3].split(',')
    matrix.append(list(map(int, line)))

size = len(matrix)

for i in range(size - 2, -1, -1):
    matrix[i][-1] += matrix[i + 1][-1]
    matrix[-1][i] += matrix[-1][i + 1]

for i in range(size - 2, -1, -1):
    for j in range(size - 2, -1, -1):
        matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

print(matrix[0][0])