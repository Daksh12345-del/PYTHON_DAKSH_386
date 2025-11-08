# # map takes a functin as a argument function and is a higher order function
# #it applies the function to each item in the iterable and returns a map object

# # def cube(x):
# #     return x**3
# cube=lambda x:x**3
# print(cube(3))

# l=[1,2,3,4,5]
# # newl=[]
# # for i in l:
# #     newl.append(cube(i))

# newl=map(cube,l)
# newl=list(map(cube,l))
# print(newl)

# # // filter takes a functin as a argument function and is a higher order function
# #it applies the function to each item in the iterable and returns a map object
# def filter_func(x):
#     return x>4
# newl=filter(filter_func,l)
# newl=list(filter(filter_func,l))
# print(newl)

# # reduce takes a functin as a argument function and is a higher order function
# #it applies the function to each item in the iterable and returns a single value
from functools import reduce
def reduce_func(x,y):
    return x+y
l=[1,2,3,4,5]
newl=reduce(reduce_func,l)
print(newl)