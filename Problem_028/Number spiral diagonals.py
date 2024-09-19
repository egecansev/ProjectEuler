dim=1001
diag_sum=1
increment=0
diag=1
for d in range(int(dim/2)):
    increment+=2
    for i in range(4):
        diag+=increment
        diag_sum+=diag
print(diag_sum)
