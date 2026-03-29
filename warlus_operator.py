a=True
print(a:=False) #Warlus operator, it assigns the value and returns it at the same time.
numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())

#Walrus Operator:
#new to Python 3.8, it allows you to assign values to variables as part of an expression. It is denoted by the := symbol. This operator can be used in various contexts, such as in loops, comprehensions, and conditional statements, to make code more concise and readable.
happy=True
print(happy) #True
print(happy:=True) #True, it assigns the value True to happy and returns it at the same time.
# food=[]
foods=list()
while True:
    food=input("What do u wan to have?")
    if food=="quit":
        break
    foods.append(food)

#Walrus operator
foods=list()
while (food:=input("What do u wan to have?"))!="quit":
    foods.append(food) 