from time import time

start = time()
months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
first_day_of_a_month = []
dummy = 0
for years in range(1901, 2001):
    if years % 4 == 0:
        months.update({2: 29})
    for days in months.values():
        first_day_of_a_month.append(dummy)
        dummy += days
    months.update({2: 28})
count = 0
for begin in first_day_of_a_month:
    if begin % 7 == 6 and begin != 0:
        count += 1
print(count-1)
end = time()
print('Time elapsed', end - start, 'seconds')
