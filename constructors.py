class person: 
    def __init__(self,Daksh,Student):  #keyword used for making a constructor and temporary variable cannot have numerical value
        print("Hey i am a person")
        self.name=Daksh
        self.occupation=Student
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person("Aarushi","Engineer") #a is an object of class person
b=person("daksh","Student")
a.info()
b.info()