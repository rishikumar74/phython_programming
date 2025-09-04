def sum(num) :
    sum=0
    i=0
    k=[]
    
    while num>0 :
        rem=num%10
        sum+=rem
        num=num//10
        k.append(rem)
    siz=len(k)
    print(k[0]+k[siz-1])
    
sum(998)