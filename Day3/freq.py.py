list_a=[1,5,6,-5,-9,8,-7,-7,12]
freq=0
for i in list_a:
    freq=0
    for j in list_a :
        if(i==j):
            freq+=1
    print(f"frequency of {i} is {freq}")

    