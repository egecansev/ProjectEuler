from time import time
from urllib import request


def subtractive(num):
    subtractives = ["IV", "IX", "XL", "XC", "CD", "CM"]
    occurence = []
    for subt in subtractives:
        if subt in num:
            occurence.append(subt)
    return occurence


def reorder(series):
    nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    number = 0
    final = ''
    subts = subtractive(series)
    for exception in subts:
        number += nums.get(exception[1]) - nums.get(exception[0])
        series = series.replace(exception, '')

    for letter in series:
        number += nums.get(letter)

    exceptions = {"40": "IV", "41": "XL", "42": "CD", "90": "IX", "91": "XC", "92": "CM"}
    num_str = [d for d in str(number)]
    index = -1
    for digit in num_str:
        index += 1
        digit_index = len(num_str) - index - 1
        if digit_index != 3:
            if digit == '4' or digit == '9':
                key = digit + str(digit_index)
                final += exceptions.get(key)
                continue
        for roman, value in nums.items():
            if 4 < int(digit) < 9:
                if value == 5 * 10 ** digit_index:
                    final += roman
                    digit = int(digit) - 5
            if value == 10 ** digit_index:
                for i in range(int(digit)):
                    final += roman
                break
    return final


start = time()
data = request.urlopen("https://projecteuler.net/project/resources/p089_roman.txt")
global codes
numerals = []
password = ''
difference = 0
for line in data:
    numeral = line.decode("utf-8")
    numeral = numeral.rstrip()
    new_numeral = reorder(numeral)
    difference += len(numeral) - len(new_numeral)
print(difference)
end = time()
print("Time elapsed", end-start, "seconds")
