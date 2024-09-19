powers=[]
for a in range(2,101):
    for b in range(2,101):
        term=pow(a,b)
        if term not in powers:
            powers.append(term)
print(len(powers))
