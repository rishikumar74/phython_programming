class car:
    brand="toyato"
   
    def color(self,cl) :
        self.colorr=cl
        print("car color is",self.colorr)
car1=car()
print(car1.brand)
car1.color("green")
