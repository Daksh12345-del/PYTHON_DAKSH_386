class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x*self.y

class circle(shape):
    def __init__(self,r):
        self.r=r
        super().__init__(r,r)
    def area(self):
        return 3.14*super().area()
    
e=shape(5,10)
print(e.area())

c=circle(5)
print(c.area())