try:
    a=int(input("Enter age must be +ve"))
    if(a<0) :
        raise ValueError("number must be +ve")
    elif(a>18) :
        print("you are eligible to vorte")
    else :
        print("You are not eligible to vote")
except ValueError:
    print("number must be +ve man")



