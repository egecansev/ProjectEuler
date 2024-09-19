from decimal import *
fraction={}
precision=100000
limit=1000
for i in range(2,limit):
    getcontext().prec=precision
    fract=Decimal(1)/Decimal(i)
    fract=str(fract)
    fract=fract.replace("0.","")
    fraction[i]=fract

recurring={}
for denominator in fraction:
    if(len(fraction.get(denominator))>precision-2):
        dummy=[]
        decimal=""
        count=0
        flag1=0
        flag2=0
        for i in range(precision-1):
            if(flag2==1):
                break
            for j in range(i+1,precision):
                if(flag1==1):
                    break
                if(fraction.get(denominator)[i]==fraction.get(denominator)[j]):
                    a=i
                    b=j
                    for chk in range(precision-j-5):
                        if(fraction.get(denominator)[a]==fraction.get(denominator)[b]):
                            count+=1
                            decimal+=fraction.get(denominator)[a]
                            a+=1
                            b+=1
                            if(count==precision-j-5 and count>20):
                                for k in range(j-i):
                                    dummy.append(decimal[k])
                                recurring[denominator]=len(dummy)

                                flag1=1
                                flag2=1
                                break
                        else:
                            count=0
                            decimal=""
                            break

for denominator in recurring.keys():
    if(recurring.get(denominator)==max(recurring.values())):
        print(denominator)
