import math
def root (a,b,c):
    n=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    if float(int(n)) == n:
        return int(n)
    return n


tri=[0.5,0.5]
penta=[1.5,-0.5]
hexa=[2,-1]
series=[penta,tri]
n=1
combo=[]
while len(combo)<3:
    flag=0
    i=n*(2*n-1)
    for serie in series:
        k=root(serie[0],serie[1],-i)
        if isinstance(k,int)==False:
            break
        flag+=1
    if flag==2:
        combo.append(i)
    n+=1
print(i)
