class employee:
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary
    def display(self) :
        print(f"name of emp is {self.name} and salary is {self.salary}")


class manager(employee) :
    def __init__(self,name,salary,dept) :
        super().__init__(name,salary) 
        self.dept=dept
    def display(self) :
        print(f"this is manager name:{self.name} dept:{self.dept} sal:{self.salary}")
m1=manager("rishi","20000","cse")
m1.display()
emplo1=employee("naveen","2900")
emplo1.display()