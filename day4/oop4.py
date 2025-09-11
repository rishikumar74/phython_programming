#abstraction
#hiding internal details and only shows nessesery output
from abc import ABC,abstractmethod 
class shape(ABC):
    @abstractmethod
    def area(self) :
        pass
    @abstractmethod
    def perimeter(self) :
        pass

class circle(shape) :
    def __init__(self,radius):
        self.radius=radius
    def area(self) :
        ar=3.14*self.radius**2
        print("area of cir is  ",ar)
    def perimeter(self)  :
        return "h"

c1=circle(5)
c1.area()
c1.perimeter()
