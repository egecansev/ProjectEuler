from time import time
from random import randrange, sample


def roll():
    a = randrange(1, 5)
    b = randrange(1, 5)
    return a, b


def move(stand, a, b):
    stand += a + b
    return stand % 40


def is_double(a, b):
    if a == b:
        return True
    else:
        return False


def go2jail():
    stand = 10
    return stand


def community_chest(deck, stand):
    card = deck.pop(0)
    if card == 0:
        stand = 0
    elif card == 10:
        stand = 10
    deck.append(card)
    return deck, stand


def chance(deck, stand):
    card = deck.pop(0)
    if type(card) == int:
        if card == 0:
            stand = 0
        elif card == 5:
            stand = 5
        elif card == 10:
            stand = 10
        elif card == 11:
            stand = 11
        elif card == 24:
            stand = 24
        elif card == 39:
            stand = 39
        elif card == -3:
            stand -= 3
    else:
        if stand == 7:
            if card == 'R':
                stand = 15
            else:
                stand = 12
        elif stand == 22:
            if card == 'R':
                stand = 25
            else:
                stand = 28
        else:
            if card == 'R':
                stand = 5
            else:
                stand = 12
    deck.append(card)
    return deck, stand


def padding(n):
    n = str(n)
    if len(n) < 2:
        n = '0' + n
    return n


def get_str(most):
    res = ''
    for element in most:
        res += padding(element)
    print(res)


start = time()

# Initialization
boxes = {}
for k in range(40):
    boxes[k] = 0

cc_deck = sample([0, 10] + [40] * 14, 16)
ch_deck = sample([0, 10, 11, 24, 39, 5, 'R', 'R', 'U', -3] + [40] * 6, 16)

recent = 0
double_count = 0
i = 0
j = 0


while True:
    x, y = roll()
    recent = move(recent, x, y)
    i += 1

    # Double
    if is_double(x, y):
        i -= 1
        double_count += 1
        if double_count == 3:
            recent = 10
    else:
        double_count = 0

    # Conditions
    if recent == 30:
        recent = go2jail()
    elif recent in (2, 17, 33):
        cc_deck, recent = community_chest(cc_deck, recent)
    elif recent in (7, 22, 36):
        ch_deck, recent = chance(ch_deck, recent)

    boxes[recent] += 1
    j += 1
    if j == 10**6:
        break

sorted_boxes = sorted(boxes.items(), key=lambda kv: kv[1], reverse=True)
get_str([box[0] for box in sorted_boxes[:3]])

end = time()
print('Time elapsed', end - start, 'seconds')
