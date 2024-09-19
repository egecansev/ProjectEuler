from time import time


def value(n):
    values = {"S": 1, "D": 2, "T": 3}
    return int(n[1:]) * values[n[0]]


def find_start_index(list_of_all, n):
    if n in list_of_all:
        index = list_of_all.index(n)
    else:
        list_of_all.append(n)
        list_of_all.sort(reverse=True)
        index = list_of_all.index(n)
        list_of_all.remove(n)
    return index


def possible_checkouts(start_value):
    cnt = 0
    index = find_start_index(all_double_values, (start_value // 2) * 2)
    for double in all_double_values[index:]:
        n = start_value
        n -= double
        if n == 0:
            cnt += 1
            continue
        elif n <= 120:
            for x in all_values:
                if x >= n:
                    if x == n:
                        cnt += len(value2spot[x])
                    break
                y = n - x
                if x <= y and y in all_values:
                    cnt += len(value2spot[y]) * len(value2spot[x])
                    if y == x:
                        cnt -= (len(value2spot[y]) * (len(value2spot[x]) - 1)) // 2
        else:
            break
    return cnt


start = time()
spots = []
all_double_values = []
for letter in ["S", "D", "T"]:
    for i in range(1, 21):
        spots.append(letter + str(i))
        if letter == "D":
            all_double_values.append(value(letter + str(i)))
spots += ["S25", "D25"]
all_double_values.append(50)
all_double_values.reverse()
spot_values = []
for spot in spots:
    spot_values.append(value(spot))
all_values = list(set(spot_values))
value2spot = {}
for i in range(len(spots)):
    if spot_values[i] not in value2spot.keys():
        value2spot[spot_values[i]] = [spots[i]]
    else:
        value2spot[spot_values[i]].append(spots[i])
count = 0
for i in range(100):
    count += possible_checkouts(i)
print(count)

end = time()
print('Time elapsed', end - start, 'seconds')
