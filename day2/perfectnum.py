num=int(input("Enter a number"))
x=num
i=num-1
count=0
sum=0
while i>0 :
    if num%i==0 :
        sum+=i
    i-=1
if(sum==x) :
    print("yes strong num")
else :
    print("no")