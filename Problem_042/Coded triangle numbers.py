names=open("p042_words.txt","r")
names=names.readline()

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alphabet={}
for i in range(1,len(letters)+1):
    alphabet[letters[i-1]]=i
names=names.replace('"',"")
names=names.split(',')

count=0
for name in names:
    value=0
    for i in name:
        value+=alphabet[i]
    n=1
    while value>0:
        value-=n
        n+=1
    if value==0:
        count+=1
print(count)
