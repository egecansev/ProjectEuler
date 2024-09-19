import copy


def isdouble_basepalindrome(n):
    number = copy.deepcopy(n)
    number = str(number)
    if ispalindrom(number):
        number = bin(n)[2:]
        if ispalindrom(number):
            return True
        else:
            return False
    else:
        return False


def ispalindrom(n):
    for i in range(len(n)):
        if n[i] != n[len(n)-1-i]:
            return False
    return True


sum_dp = 0
limit = pow(10, 6)
for k in range(1, limit+1):
    if isdouble_basepalindrome(k):
        sum_dp += k
print(sum_dp)
