def factorial(num):
    mul=1
    for i in range(1,num+1):
        mul*=i
    return mul
print(factorial(5))