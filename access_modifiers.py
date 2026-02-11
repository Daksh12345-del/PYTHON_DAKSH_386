# class employee:
#     pass

# a-employee()
# a.emp1=5
#public access modifier
class Employee:
    def __init__(self):
        self.name="Daksh"
a=Employee()
print(a.name)
#private access modifier
class Employee:
    def __init__(self):
        self.__name="Daksh"
a=Employee()
# print(a.__name)
print(a._Employee__name) #name mangling method to access private member
print(a.__dir__()) #to see all the members of the class including private members

#protected access modifier
class Employee:
    def __init__(self):
        self.name="Daksh"
a=Employee()
print(a.name)