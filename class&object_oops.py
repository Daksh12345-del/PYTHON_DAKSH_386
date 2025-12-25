class person: #blueprint which is used to create objects
    name="Daksh"
    age=19
    occupation="Student"
    def info(self):
        print(f"{self.name} is a {self.occupation} of age {self.age}")


a=person() #a is an object of class person
b=person() #b is another object of class person
# b.name="Daksh"
# b.occupation="Developer"
# print(b.name,b.occupation)
# # print(b.info())
# a.name="aarushi"
# a.occupation="Engineer"
# print(a.name,a.occupation)
# a.info() 
# b.info()