from time import time
from urllib import request


def is_inside():
    for i in range(3):
        for j in range(i+1, 3):
            if triangle[i][0] == triangle[j][0]:
                m = 10**10
            else:
                m = (triangle[i][1] - triangle[j][1])/(triangle[i][0] - triangle[j][0])
            n = triangle[i][1] - m * triangle[i][0]
            if (midpoint[1] < m * midpoint[0] + n) != (0 < n):
                return False
    return True


start = time()
count = 0
data = request.urlopen("https://projecteuler.net/project/resources/p102_triangles.txt")
for line in data:
    line = line.decode("utf-8").strip("\n").split(',')
    triangle = []
    midpoint = [0, 0]
    for a in range(3):
        side = []
        for b in range(2):
            side.append(int(line[0]))
            midpoint[b] += int(line.pop(0))/3
        triangle.append(side)
    if is_inside():
        count += 1
print(count)
end = time()
print('Time elapsed', end - start, 'seconds')
