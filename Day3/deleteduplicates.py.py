list_a=[1,5,5,6,-5,-9,8,-7,-7,12]

for i in list_a :
    freq=0
    for j in list_a :
        if(i==j) :
            freq+=1
    if(freq!=1) :
        print(f"{i} is duplicate")
    for d in range(1,freq) :
        list_a.remove(i)
print(f"list with out duplicates is {list_a}")