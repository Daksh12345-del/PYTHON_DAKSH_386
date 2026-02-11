class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,a):
        self.num=self.num+a
    @staticmethod #not used instance or class variable and used as a decorator
    def add(a,b):
        return a+b
# reuslt=math.add(2,3)
# print(reuslt)
b=math(5)
print(b.num)
b.addtonum(6)
print(b.num)
print(b.add(10,20 ))