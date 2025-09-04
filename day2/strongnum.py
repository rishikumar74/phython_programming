def factorial(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul
num=int(input("Enter a number"))
number=num
sum=0
while number>0 :
    rem=number%10
    val=factorial(rem)
    sum+=val
    number=number//10
if(sum==num) :
    print("yes")
else :
    print("no")