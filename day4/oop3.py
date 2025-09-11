class student:
    def __init__(self,name,roll,marks) :
        self.name=name
        self.marks=marks
        self.roll=roll
    def display(self) :
        print(f"student {self.name} got {self.marks}")

class teacher(student) :
    def __init__(self,name,sub) :
        super().__init__()
        self.name=name
        self.sub=sub
    def subject(self) :
        print(f"hi i will explain {self.sub}")
        

std1=student("rishi","5aq",99)
std2=student("nandu","5af",100)
std1.display()
std2.display()
t1=teacher("naveen","ph")
t1.display()
