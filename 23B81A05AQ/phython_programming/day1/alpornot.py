def check(cha) :
    if((cha>='a' and cha<='z') or (cha>='A' and cha<='Z')) :
        print(f"{cha} is a alphabet")
    else :
        print(f"{cha} not a alphabet")
check("a")
check("@")
check("A")
check('6')
check(']')