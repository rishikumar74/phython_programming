st=input("Enter as string")
dict={}
last={}
for i in st :
    cnt=0
    for j in st:
        if i==j :
            cnt+=1
        dict[i]=cnt
    last[i]=cnt;

for i in dict :
    print(i,end="")
    print(last[i],end="")

