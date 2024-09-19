from time import time

start = time()
file = open("p022_names.txt", "r")
file = file.readline()
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
alphabet = {}
for i in range(1, len(letters)+1):
    alphabet[letters[i-1]] = i
file = file.replace('"', "")
file = file.split(',')
file = sorted(file)

total_score = 0
cnt = 1
for name in file:
    score = 0
    for letter in name:
        score += alphabet.get(letter)
    score *= cnt
    total_score += score
    cnt += 1
print(total_score)
end = time()
print('Time elapsed', end - start, 'seconds')
