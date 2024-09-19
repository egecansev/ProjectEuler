from time import time
from urllib import request


def is_square_anagram(duo, number):
    anagram_map = {}
    num_an = 'x' * len(number)
    ambiguous = []
    for index0 in range(len(duo[0])):
        indexes = []
        for index1 in range(len(duo[1])):
            if duo[0][index0] == duo[1][index1]:
                indexes.append(index1)
        if len(indexes) == 1:
            anagram_map[index0] = indexes.pop()
        else:
            anagram_map[index0] = indexes
            if indexes not in ambiguous:
                ambiguous.append(index0)
    for_flag = 0
    if ambiguous:
        for m in range(len(ambiguous)):
            for n in range(m + 1, len(ambiguous)):
                if number[ambiguous[m]] != number[ambiguous[n]]:
                    for_flag = 1
                    break
        if not for_flag:
            for item in anagram_map.values():
                if type(item) == list:
                    for x in range(len(item)):
                        for key in anagram_map.keys():
                            if anagram_map.get(key) == item:
                                anagram_map[key] = item[x]
                                break
    if not for_flag:
        for key in anagram_map.keys():
            num_an = num_an[:anagram_map.get(key)] + number[key] + num_an[anagram_map.get(key) + 1:]
        if (int((int(num_an)) ** 0.5)) ** 2 == int(num_an) and len(str(int(number))) == len(str(int(num_an))):
            print(max(int(number), int(num_an)))
            return True
    return False


start = time()
words = sorted(request.urlopen("https://projecteuler.net/project/resources/p098_words.txt").readline().decode("utf-8")
               .replace('"', '').split(','), key=lambda s: len(s), reverse=True)
flag = 0
while True:
    length = len(words[0])
    longest_words = [words[0]]
    sorted_words = ["".join(sorted(words.pop(0)))]
    while len(words[0]) == length:
        longest_words.append(words[0])
        sorted_words.append("".join(sorted(words.pop(0))))
    anagrams = []
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j]:
                anagrams.append((longest_words[i], longest_words[j],
                                 [sorted_words[i].count(char) for char in sorted_words[i]]))
    if anagrams:
        i = int((10 ** length) ** 0.5)
        while i > int((10 ** (length - 1)) ** 0.5):
            square = str(i * i)
            for anagram in anagrams:
                if sorted([square.count(digit) for digit in square]) == sorted(anagram[2]):
                    if is_square_anagram(anagram, square):
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
            i -= 1
    if flag == 1:
        break
end = time()
print('Time elapsed', end - start, 'seconds')
