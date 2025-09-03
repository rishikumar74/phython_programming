p=float(input("Enter principle amount"))
t=int(input("enter time in months"))
r=float(input("Enter rate of intrest"))
res=(p*t*r)/100
print(res)
print("amt in hand",res+p)