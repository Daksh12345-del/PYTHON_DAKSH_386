# # single inheritence

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Woof! Woof!")
    
# d=Dog("Buddy", "Golden Retriever")
# d.make_sound()

# a=Animal("Generic Animal", "Unknown")
# a.make_sound()


#Multiple Inheritence
# class Employee:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"Employee Name: {self.name}")

# class Dancer:
#     def __init__(self,dance):
#         self.dance=dance
#     def show(self):
#         print(f"Employee Name: {self.dance}")

# class DancingEmployee(Employee, Dancer):
#     def __init__(self,name,dance):
#         self.dance=dance
#         self.name=name
#     # def __str__(self):
#     #     return f"{self.name}, {self.dance}"

# o=DancingEmployee("alice","ballet")
# # print(str(o))
# print(o.name)
# o.show()
# print(DancingEmployee.__mro__) # it tells where all it will find for the show method first it will check in Employee then in Dancer and then in DancingEmployee

#multi level inheritence

# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species
#     def showdetails(self):
#         print(f"Animal Name: {self.name}, Species: {self.species}")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed = breed
#     def showdetails(self):
#         print(f"Dog Name: {self.name}, Breed: {self.breed}")

# class GoldenRetriever(Dog):
#     def __init__(self,name):
#         Dog.__init__(self,name,breed="Golden Retriever")
#     def showdetails(self):
#         Dog.showdetails(self) # it will call the showdetails method of Dog class
#         print(f"Golden Retriever Name: {self.name}")


# d1=GoldenRetriever("Buddy")
# d1.showdetails()
# print(GoldenRetriever.__mro__) # it will show the method resolution order for the showdetails method first it will check in GoldenRetriever then in Dog and then in Animal

# Hybrid Inheritence/Hierachical Inheritence

## EXAMPLE OF HYBRID INHERITENCE
class Base_class:
    pass

class Derived_class1(Base_class):
    pass

class Derived_class2(Base_class):
    pass

class Derived_class3(Derived_class1,Derived_class2):
    pass

# EXAMPLE OF HIERARCHICAL INHERITENCE
class Base_class:
    pass

class Derived_class1(Base_class):
    pass

class Derived_class2(Base_class):
    pass

class Derived_class3(Derived_class1):
    pass