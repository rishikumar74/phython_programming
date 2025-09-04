num=int(input("Enter A number"))
def cube(r) :
    cub=r**3
    return cub
    
    
number=num
sum=0
while number>0 :
    rem=number%10
    val=cube(rem)
    number=number//10
    sum+=val
if(sum==num) :
    print("yes amstrong")
else :
    print("no")