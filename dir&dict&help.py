# #dir() function shows the attributes and methods of any object (functions, modules, strings, lists, dictionaries etc.)
# x=[1,2,3]
# print(dir(x))  #dir shows all the methods and attributes of list object
# print(x.__add__)

#__dict__ attribute shows the namespace of the object
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.country="USA" #instance variable

# p1=Person("John",30)
# print(p1.__dict__)  #prints the namespace of p1 object and provides us output in dictionary as:
# # {'name': 'John', 'age': 30, 'country': 'USA'}

# #help() function is used to display the documentation of modules, functions, classes, methods etc.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.country="USA" #instance variable

p1=Person("John",30)
print(p1.__dict__)
print(help(p1))  #prints the documentation of Person class and its methods including __init__ method
