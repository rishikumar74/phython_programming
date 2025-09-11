class person:
    def __init__(self,name,age,gender) :
        self.name=name
        self.age=age
        self.gender=gender
    def work(self) :
        print(f"{self.name} will do bussiness")
    def talk(self) :
        print(f"{self.name} will talk in telugu")
person1=person("raju",25,"male")
print(person1.name)
print(person1.age)
print(person1.gender)
person1.work()
person1.talk()