std=[("5aq",'rishi',80),("5af","nandu",90),("5ag","naveen",60),("5ax","mohith",59),("5ay","sak",8)]
maxm=std[0][2]
for i in std :
    if(i[2]>maxm) :
        maxs=i;
        maxm=i[2];
print("max marks ",maxs[1])
for i in std :
    if i[2]>=75 :
        print(i[1])


