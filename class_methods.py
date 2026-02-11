class Employee:
    company="apple"
    def show(self):
        print(f"Employee works at {self.company} and the name is {self.name}")
    
    @classmethod 
    def change_company(cls, new_company):
        cls.company = new_company



emp1 = Employee()
emp1.name = "John"
emp1.show()  # Output: Employee works at apple and the name is John
emp1.change_company("google")
emp1.show()  # Output: Employee works at google and the name is John
print(Employee.company)  # Output: google