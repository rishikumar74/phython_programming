def reverse(num) :
    stri=str(num)
    revstr=stri[-1::]
    revnum=int(revstr)
    if(num==revnum) :
        print(f"{num} is apallindrome")
    else :
        
        print(f"{num} is not a apallindrome")
        
reverse(121)

        

    