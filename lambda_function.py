# def double(x):
#     return x * 2
#lambda function is used to create small anonymous functions.
def appl(func, value):
    return 6+func(value)
double=lambda x: x * 2
cube=lambda x: x**3
avg=lambda x,y: (x+y)/2
print(double(5))
print(cube(3))
print(int(avg(10,20)))
print(appl(double,5))