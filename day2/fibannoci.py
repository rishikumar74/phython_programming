n=int(input("Enter upto val"))
x=0
y=1
print(x," ",y,end=" ")
sum=x+y
while n>sum :
    x=y
    y=sum
    sum=x+y
    print(sum,end=" ")