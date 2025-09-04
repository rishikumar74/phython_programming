def check(char) :
    if(char>='a' and char<='z') or (char>='A' and char<='Z') :
        print(f"{char} is alphabet")
    elif(char>='1' and char<='9') :
        print(f"{char} is a digit")
    else :
        print(f"{char} is a special char")

check('1')
check('a')
check('@')
check("")