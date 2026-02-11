class Employee:
    comapny="Google"  # class variable
    noOfemployee=0
    def __init__(self,name):
        self.name = name
        self.raise_amount=0.02 # instance variable
        Employee.noOfemployee += 1
    def showdetails(self):
        print(f"name of emplyee is {self.name} and the raise is {self.raise_amount} in the company of {self.comapny} with numbe of employees {Employee.noOfemployee}")

e1=Employee("Alice")
e1.raise_amount=0.05
e1.comapny="Youtube"
e1.showdetails()
print(Employee.comapny) # accessing class variable using class name
print(e1.comapny)  # accessing class variable using instance
e2=Employee("Bob")
e2.showdetails()

#firstly it will check for instance variable if not found then it will check for class variable