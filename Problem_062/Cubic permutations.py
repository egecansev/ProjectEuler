i=1
cubes={}
while i<pow(10,5):
    cubes[str(pow(i,3))]=len(str(pow(i,3)))
    i+=1

length=0
set=[]
final_set=[]
k=1
while length<=max(cubes.values()):
    flag=0
    for cube, length in cubes.items():
        if length==k:
            set.append(cube)
        elif length>k:
            break
    k+=1
    for i in range(len(set)):
        for j in range(i+1,len(set)):
            if sorted(set[i])==sorted(set[j]):
                if set[i] not in final_set:
                    final_set.append(set[i])
                if set[j] not in final_set:
                    final_set.append(set[j])
                # min_cube=set[i]
                # if int(set[j])<int(min_cube):
                #     min_cube=set[j]
        if len(final_set)==5:
            print(min(final_set))
            flag=1
            break
        final_set.clear()
    if flag:
        break
    set.clear()
