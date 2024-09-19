with open("p067_triangle.txt") as file:
    content = file.readlines()
content = [x.strip() for x in content]
lines = []
content = [element.split(" ") for element in content]
content = [list(map(int, element)) for element in content]
new_line = []
for line in reversed(content):
    if new_line:
        line = [x + y for x, y in zip(new_line, line)]
    new_line.clear()
    for i in range(len(line)-1):
        new_line.append(max(line[i], line[i+1]))
print(line[0])