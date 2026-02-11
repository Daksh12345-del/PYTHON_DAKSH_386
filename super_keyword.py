# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method-1.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Daksh Singhal")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method-2.")
#         super().parent_method()  # Calling the parent class method using super()

# child_object=ChildClass()
# child_object.child_method()  # Calling the child class method
# child_object.parent_method()  # Calling the overridden parent class method

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name = name
        # self.id = id
        self.lang = lang
        super.__init__(name,id)

rohan=Programmer("Rohan",101,"Python")
harry=Programmer("Harry",102,"Java")
print(rohan.lang)