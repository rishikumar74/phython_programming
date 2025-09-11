try:
    numa=int(input("Enter a  number"))
    numb=int(input("Enter a  number"))
    c=numa/numb
except ValueError:
    print("invalid ip")
except ZeroDivisionError:
    print("zero div error")

else :
    print("No error occured")
finally :
    print("finally block executed")
