i=1
while True:
    if sorted(list(str(i))) == sorted(list(str(6*i))):
        if sorted(list(str(i))) == sorted(list(str(5*i))):
            if sorted(list(str(i))) == sorted(list(str(4*i))):
                if sorted(list(str(i))) == sorted(list(str(3*i))):
                    if sorted(list(str(i))) == sorted(list(str(2*i))):
                        print(i)
                        break
    i+=1
