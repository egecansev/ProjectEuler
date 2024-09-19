import copy


def ispalindrome (palindrome):
    if palindrome==reverse(palindrome):
        return True
    else:
        return False


def reverse (n):
    return int("".join(list(reversed(str(n)))))


Lychrel=[]
for i in range(pow(10,4)):
    flag=0
    k=i
    for iteration in range(50):
        k+=reverse(str(k))
        if ispalindrome(k):
            flag=1
            break
    if flag==0:
        Lychrel.append(i)

print(len(Lychrel))
