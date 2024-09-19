from itertools import permutations


def ascii2bin(n):
    n=bin(int(n))
    n=n.split("b")[1]
    for i in range(8-len(n)):
        n="0"+n
    return n

def xor (c,k):
    x=""
    for i in range(8):
        if c[i]==k[i]:
            x+="0"
        else:
            x+="1"
    k=pow(2,7)
    sum=0
    for y in x:
        sum+=k*int(y)
        k/=2
    x=chr(int(sum))
    return x


cipher=open("cipher.txt","r")
cipher=cipher.read()
cipher=cipher.rstrip("\n")
cipher=cipher.split(",")

ascii=[]
for x in cipher:
    x=ascii2bin(x)
    ascii.append(x)

key_set=[]
for x in range(97,123):
    x=ascii2bin(x)
    key_set.append(x)


ascii1=[]
ascii2=[]
ascii3=[]
for x in range(len(ascii)):
    if x%3==0:
        ascii1.append(ascii[x])
    elif x%3==1:
        ascii2.append(ascii[x])
    elif x%3==2:
        ascii3.append(ascii[x])


decrypted1=[]
decrypted2=[]
decrypted3=[]
dummy=[]
candidates=[]
perm=list(permutations(key_set,3))
for keygen in perm:
    decrypted=""
    for word in ascii1:
        new_word=xor(word,keygen[0])
        decrypted1.append(new_word)
    for word in ascii2:
        new_word=xor(word,keygen[1])
        decrypted2.append(new_word)
    for word in ascii3:
        new_word=xor(word,keygen[2])
        decrypted3.append(new_word)
    while True:
        dummy.append(decrypted1.pop())
        if len(decrypted1)==0:
            break
        dummy.append(decrypted3.pop())
        dummy.append(decrypted2.pop())
    while len(dummy)!=0:
        decrypted+=dummy.pop()
    if "the" in decrypted:
        if "and" in decrypted:
            candidates.append(decrypted)
for candidate in candidates:
    if "this" in candidate and "that" in candidate and "have" in candidate and "be" in candidate:
        break

sum=0
for w in candidate:
    sum+=ord(w)
print(sum)
