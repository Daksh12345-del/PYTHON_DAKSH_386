class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.id}")

class Programmer(Employee):
    def showlanguages(self,Languages=None):
        print("Languages Known: Python, Java, C++")


e1=Employee("Daksh",101)
e1.showdetails()
e2=Employee("Aarushi",102)
e2.showdetails()
e3=Programmer("Rajesh Singhal",103)
e3.showlanguages()
e4=Employee("Parth Singhal",104)
e4.showdetails()