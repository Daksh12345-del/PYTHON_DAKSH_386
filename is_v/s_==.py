#is and == both are compariosn operators in Python but they serve different purposes.
# a=(1,2,3)
# b=(1,2,3)
# a=[1,2,3]
# b=[1,2,3]
a=None
b=None
print(a==b)#it compares the values of both the operands and checks for value equality
print(a is b)#it compares the exact memory locations of both the operands and checks for reference equality
print(a is None)#it checks if the variable a is pointing to None object in memory