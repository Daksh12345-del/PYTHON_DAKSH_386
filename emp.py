class Employee:
    def __init__(self,name):
         self.name="Daksh"
    def __len__(self):
        i=0
        for item in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return (f"Employee name is {self.name}")
    
    def __repr__(self):
        return (f"Employee name is {self.name} repr")
    
    def call(self):
        return (f"Employee name is {self.name} call")