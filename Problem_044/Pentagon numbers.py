import math


def ispentagon(a, b, c):
    n = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
    if float(int(n)) == n:
        return int(n)
    return n


pentagon=[1]
n=2

while True:
   flag=0
   pentagonal=int(n*(3*n-1)/2)
   for i in pentagon:
        if isinstance(ispentagon(1.5,-0.5, i-pentagonal), int):
            if isinstance(ispentagon(1.5,-0.5, -(i + pentagonal)),int):
                flag=1
                print(pentagonal-i)
   if flag:
       break
   pentagon.append(pentagonal)
   n+=1


