from xmlrpc.client import boolean

dict={}
bo=1
while bo:
    print("\n")
    print("1.ADD BOOK")
    print("2.REMOVE book")
    print("3.SEARCH BOOK")
    print("4.update the title")
    print("5.dispaly all books")
    print("6.count the books")
    print("7.check title exists")
    n=int(input())
    if n==1 :
        st1=input("book id\n")
        st2=input("book name")
        dict.update({st1:st2})
    elif n==2 :
        rm=input("WHAT DO U WANT TO REMOVE FROM BELOW LIST\n")
        dict.pop(rm)

    elif n==3 :
        sr=input("SEARCH book\n")
        if sr in dict.keys() :
            print(f"id {sr} title is {dict[sr]}")
        else:
            print(f"{sr} is not present")


    elif n==4 :
        print("update the title for which book id:\n")
        ti=input()
        nt=input("Enter new title")
        dict[ti]=nt

    elif n==5 :
        print("display all books")

        for i in dict.values() :

            print(i)

    elif n==6:
        x = 0
        for i in dict.values():
            x += 1


        print(f"count : {x}")


    elif n==7 :

        print("check title exists")
        n=input("Enter tile name")
        for i in dict.values() :
            if(i==n) :
                print("title exists")
                exit()
        print("not exist")


    else :
        print("INPUT IS WRONG")
    print("\n")
    print("\n")

    bo=int(input("1 FOR CONTINUE\n 2 FOR EXIT\n"))
    if bo!=1:
        break





