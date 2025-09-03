x=int(input("Enter val"))
y=int(input("Enter val"))
x,y=y,x
print(f"{x},{y}")

a=int(input("Enter val"))
b=int(input("Enter val"))
temp=a;
a=b;
b=temp;
print(f"{a},{b}")

t=int(input("Enter val"))
n=int(input("Enter val"))

t=t^n
n=t^n
t=t^n
print(f"{t},{n}")


