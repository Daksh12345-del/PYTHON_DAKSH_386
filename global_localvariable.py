x=4#global variable
print (x)

def hello():
    global x
    x=7 #modifying global variable
    global y
    y=5#local variable
    print(f"The local y is still:{y}")
    print(y)
    print("Hello Daksh")
hello()
print(x)
print(f"The global y is still:{y}")# This will give error as y is local variable and not defined globally