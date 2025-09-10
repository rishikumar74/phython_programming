list_a=[1,5,6,-5,-9,8,-7,12]
n=int(input("Enter elemnt"))
list_b=[]
for i in list_a:
    if(i!=n):
        list_b.append(i)
    else:
        continue;
print(list_b)
    