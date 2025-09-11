class payment:
    def pay(self) :
        print("pay money")

class cashMethod(payment) :
    def pay(self) :
        print("paid in cash")

class cardMethod(payment) :
    def pay(self) :
        print("paid in card method")

class upiMethod(payment) :
    def pay(self) :
        print("paid using upi")

#cust1=upiMethod()
#cust1.pay()

payments=[cashMethod(),cardMethod(),upiMethod()]
for i in payments :
    x=i
    x.pay()
