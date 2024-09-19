from time import time

start = time()
num2words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
             9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
             20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
             80: "eighty", 90: "ninety", 1000: "onethousand"}
n2l = ""
for number in range(1, 1001):
    if len(str(number)) == 3:
        if number % 100 == 0:
            hundreds = number / 100
            hundreds = num2words.get(hundreds) + "hundred"
            number = 0
        else:
            hundreds = int(number / 100)
            number -= hundreds * 100
            hundreds = num2words.get(hundreds) + "hundredand"
    else:
        hundreds = ""
    if number == 0:
        rest = ""
    elif number < 21 or number % 10 == 0:
        rest = num2words.get(number)

    else:
        ones = number % 10
        tens = number - ones
        rest = num2words.get(tens) + num2words.get(ones)
    n2l += (hundreds + rest)
print(len(n2l))
end = time()
print('Time elapsed', end - start, 'seconds')
