from time import time


def is_aligned(a, b):
    if a[1] and b[1]:
        if a[0] / a[1] == b[0] / b[1]:
            return True
    elif not a[1] and not b[1]:
        return True
    else:
        return False


def is_side_right_triangle(a, b):
    if (not a[0] and b[0]) or (a[0] and not b[0]):
        if a[1] == b[1]:
            return True
    elif (not a[1] and b[1]) or (a[1] and not b[1]):
        if a[0] == b[0]:
            return True
    return False


def norm(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def is_right_triangle(a, b):
    norms = sorted((norm(a, b), norm(a, o), norm(b, o)))
    if norms[0] + norms[1] == norms[2]:
        return True
    return False


start = time()
limit = 50
count = 0
o = (0, 0)
for x1 in range(limit + 1):
    for y1 in range(limit + 1):
        if not x1 and not y1:
            continue
        for x2 in range(limit + 1):
            for y2 in range(limit + 1):
                if not x2 and not y2:
                    continue
                p1 = (x1, y1)
                p2 = (x2, y2)
                if p1 == p2 or is_aligned(p1, p2):
                    continue
                if is_side_right_triangle(p1, p2):
                    count += 1
                    continue
                if is_right_triangle(p1, p2):
                    count += 1
print(int(count / 2))
end = time()
print("Time elapsed", end-start, "seconds")
