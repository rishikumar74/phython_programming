class bankAccount:
    def __init__(self) :
        self.__balance=0
    def deposit(self,money) :
        self.money=money
        self.__balance+=money
        print(f"Rs {self.money} is sussessfully added into bank")
    def withdraw(self,cash) :
        self.cash=cash
        if(self.__balance>cash) :
            self.__balance-=self.cash
            print(f"Rs {self.cash} is sussessfully debited")
        else :
            print("insufficient balance")
    def getbalance(self) :
        return self.__balance;
cust1=bankAccount()
cust1.deposit(5000)
cust1.withdraw(1000)
print("balance ",cust1.getbalance())

