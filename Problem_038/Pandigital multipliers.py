def ispandigital(n):
    if "0" in str(n):
        return False
    for w in str(n):
        if w in str(n)[str(n).index(w)+1:]:
            return False
    return True


max_pandigital=0
for i in range(1,pow(10,4)):
    pandigital=""
    if ispandigital(i):
        pandigital+=str(i)
        j=2
        while True:
            prod=i*j
            if ispandigital(prod):
                pandigital+=str(prod)
                if ispandigital(int(pandigital)):
                    j+=1
                    if len(pandigital)==9 and max_pandigital<int(pandigital):
                        max_pandigital=int(pandigital)
                        break
                else:
                    break
            else:
                break
print(max_pandigital)
