def sum(num) :
    sum=0
    while num>0 :
        rem=num%10
        sum+=rem
        num=num//10
    print(sum)
sum(560)