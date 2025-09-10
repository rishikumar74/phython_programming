st=input("Enter string")
cnl=cnu=cnd=cns=0
for i in st :
    if i>='a' and i<='z' :
        cnl+=1
    elif i>='A' and i<='Z' :
        cnu+=1
    elif i>'0' and i<='9' :
        cnd+=1
    else :
        cns+=1
print(f"count of lowercase alp is {cnl}\n count of uppercase is {cnu} \n count of dig is {cnd} \ncount of spec is {cns}")

