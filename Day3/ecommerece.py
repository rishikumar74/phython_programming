from xmlrpc.client import boolean

l=[]
bo=1
while bo:
    print("\n")
    print("1.ADD TO CART")
    print("2.REMOVE FROM CART")
    print("3.SEARCH IN CART")
    print("4.DISPLAY")
    print("5.TOTAL COUNT")
    print("6.sort the cart")
    print("7.clear the cart")
    n=int(input())
    if n==1 :
        st=input("WHAT ITEM DO U WANT\n")
        l.append(st)
    elif n==2 :
        rm=input("WHAT DO U WANT TO REMOVE FROM BELOW LIST\n")
        print(l)
        l.remove(rm)
    elif n==3 :
        sr=input("WHAT DO U WANT TO SEARCH\n")
        if sr in l :
            print(f"{sr} is present in list")
        else:
            print(f"{sr} is not present in list")
    elif n==4 :
        print("DISPLAY OF ALL ITEMS :\n")
        for i in l :
            print(i)
    elif n==5 :
        print("count of items",len(l))
    elif n==6:

        print(f"sorted cart is : {sorted(l)}")
    elif n==7 :
        del l
        print("cart is cleared")
    else :
        print("INPUT IS WRONG")
    print("\n")
    print("\n")

    bo=int(input("1 FOR CONTINUE\n 2 FOR EXIT\n"))
    if bo!=1:
        break
print(f"display of all items is {l}")




