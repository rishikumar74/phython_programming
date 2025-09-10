st=input("Enter string")
cno=cnc=0
for i in st :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' :
        cno+=1
    else :
        cnc+=1
print("no of vowels is",cno)
print("no of consonents is",cnc)