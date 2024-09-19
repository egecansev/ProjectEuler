import copy
import pickle

#Card to values
def c2v(card):
    return card_order.get(card[0])
#Values to card
def v2c(value):
    for c, v in card_order.items():
        if v==value:
            return c


def flush (hand):
    suits=[]
    for card in hand:
        suits.append(card[1])
    suits=set(suits)
    if len(suits)==1:
        return [6,c2v(hand[4])]
    else:
        return [0,-1]


def straight (hand):
    for i in range(4):
        if c2v(hand[i])+1!=c2v(hand[i+1]):
            return [0,-1]
    return [5, c2v(hand[4])]


def straight_or_royal_flush (hand):
    return 0
#if straight(hand):
#         if flush(hand)[2]==1:
#             if hand[4][0]=='A':
#                 return [10,14]
#             else:
#                 return [9, c2v(hand[4])]
#         return 0
#     return 0


def repetitive_hands(hand):
    card_counter={}
    max_value=0
    for card in hand:
        if card[0] not in card_counter.keys():
            card_counter[card[0]]=1
        else:
            card_counter[card[0]]+=1

    #Four of a kind
    if 4 in card_counter.values():
        for card, repetition in card_counter.items():
            if repetition==4:
                kind=card
            elif repetition==1:
                other=card
        return [8, c2v(kind), c2v(other)]

    elif 3 in card_counter.values():
        #Full House
        if 2 in card_counter.values():
            for card, repetition in card_counter.items():
                if repetition==3:
                    full=card
                elif repetition==2:
                    house=card
            return [7,c2v(full),c2v(house)]
        #Trips
        else:
            for card, repetition in card_counter.items():
                if repetition==3:
                    trips=card
                else:
                    if max_value<c2v(card):
                        high_card=card
                        max_value=c2v(card)
            return[4,c2v(trips),c2v(high_card)]

    elif 3 not in card_counter.values() and 2 in card_counter.values():
        #Two pairs
        if len(card_counter)==3:
            pairs=[]
            for card, repetition in card_counter.items():
                if repetition==2:
                    pairs.append(card)
                    if max_value<c2v(card):
                        pair=card
                        max_value=c2v(card)
            for papapa in pairs:
                if papapa!= pair:
                    piccolo_pair=papapa
            return [3,c2v(pair),c2v(piccolo_pair)]
        #Pair
        else:
            for card, repetition in card_counter.items():
                if repetition==2:
                    pair=card
                else:
                    if max_value<c2v(card):
                        high_card=card
                        max_value=c2v(card)
            return [2,c2v(pair),c2v(high_card)]

    #High card
    else:
        return [1,c2v(hand[4][0]),c2v(hand[3][0])]


def card_combination(hand):
    ccomb={}
    for card in hand:
        if card[0] not in ccomb.keys():
            ccomb[card[0]]=1
        else:
            ccomb[card[0]]+=1
    return ccomb


def evaluator (hands):
    score=[0,0]
    reserve_score1=[0,0]
    reserve_score2=[0,0]
    flag=0
    for i in range(2):
        hand=hands[i]
        if flush(hand)[0]!=0:
            score[i]=flush(hand)[0]
            reserve_score1[i]=flush(hand)[1]

        elif straight(hand)[0]!=0:
            score[i]=straight(hand)[0]
            reserve_score1[i]=straight(hand)[1]
            flag=1
        else:
            score[i]=repetitive_hands(hand)[0]
            reserve_score1[i]=repetitive_hands(hand)[1]
            reserve_score2[i]=repetitive_hands(hand)[2]

    if (score[0]>score[1]):
        return True
    elif score[0]==score[1]:
        if reserve_score1[0]>reserve_score1[1]:
            return True
        elif reserve_score1[0]==reserve_score1[1]:
            if reserve_score2[0]>reserve_score2[1]:
                return True
            elif reserve_score2[0]==reserve_score2[1]:
                ##print(hands)
                if len(card_combination(hands[0]).keys())==3:
                    if hands[0][0][0]>hands[1][0][0]:
                        return True
                    else: return False
                elif len(card_combination(hands[0]))==4:
                    if hands[0][1][0]>hands[1][1][0]:
                        return True
                    elif hands[0][1][0]==hands[1][1][0]:
                        if hands[0][0][0]>hands[1][0][0]:
                            return True
                        else: return False
                    else: return False
                elif (len(card_combination(hands[0])))==5:
                    if hands[0][2][0]>hands[1][2][0]:
                        return True
                    elif hands[0][2][0]==hands[1][2][0]:
                        if hands[0][1][0]>hands[1][1][0]:
                            return True
                        elif hands[0][1][0]==hands[1][1][0]:
                            if hands[0][0][0]>hands[1][0][0]:
                                return True
                            else: return False
                        else: return False
                    else: return False
                else: return False
            else: return False
        else: return False
    else: return False


data=open("poker.txt","r")
card_order={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
cards=[]
hand=[]
hands=[]
round=[]
line=data.readline()
player1_wins=0
player2_wins=0

while line:
    cards=line.split(" ")
    cards[9]=cards[9].rstrip("\n")
    for i in range(2):
        for j in range(5):
            hand.append(cards[i*5+j])
        hand=sorted(hand,key=c2v)
        hands.append(copy.deepcopy(hand))
        hand.clear()
    if evaluator(hands):
        player1_wins+=1
        winner=1
    else:
        winner=2
        player2_wins+=1
    round.append(copy.deepcopy(hands))
    hands.clear()
    line=data.readline()
print("Player1 wins",player1_wins,"hands and Player2 wins",player2_wins,"hands")
