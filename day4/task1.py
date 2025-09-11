
class vehicle:
    def __init__(self,numberplate,ownername) :
        self.__np=numberplate
        self.__on=ownername
    def display(self) :
        print(f"vehicle owner name is {self.__on} license plate no . is {self.__np}")
    def getnp(self) :
        return self.__np
    def geton(self) :
        return self.__on
    

class bike(vehicle) :
    def __init__(self,numberplate,ownername,helment) :
        super().__init__(numberplate,ownername)
        self.helment=helment
    def display(self) :
        print(f"bike owner name:{self.geton()} licsence no . is {self.getnp()} helment:{self.helment}")
    def calculate_parking_fee(self,hours):
        val=hours*20
        print("parking cost  ",val)


class car(vehicle) :
    def __init__(self,numberplate,ownername,seats) :
        super().__init__(numberplate,ownername)
        self.seats=seats
    def display(self) :
        print(f"car owner name:{self.geton()} licsence no . is {self.getnp()} seats:{self.seats}")
    def calculate_parking_fee(self,hours):
        val=hours*50
        print("parking cost  ",val)



class truck(vehicle) :
    def __init__(self,numberplate,ownername,maxload) :
        super().__init__(numberplate,ownername)
        self.maxload=maxload
    def display(self) :
        print(f"truck owner name:{self.geton()} licsence no . is {self.getnp()} maxload:{self.maxload}")
    def calculate_parking_fee(self,hours):
        val=hours*100
        print("parking cost  ",val)



bo1=bike("tg07m4255","rishi","yes")
bo1.display()
bo1.calculate_parking_fee(5)

co1=car("tso6y7777","santhosh","7")
co1.display()
co1.calculate_parking_fee(5)

to1=truck("mho7ey8888","naveen","7tons")
to1.display()
to1.calculate_parking_fee(5)
