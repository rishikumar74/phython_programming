vow="aeiouAEIOU"
st=input("Enter a string ")
oc=cc=dc=sc=0
for i in st :
    if i in vow :
        oc+=1
    elif i.isalpha() :
        cc+=1
    elif i.isdigit() :
        dc+=1
    else :
        sc+=1
print(f"vowels {oc} \n cons {cc} \n dig {dc} \n special chat {sc}")