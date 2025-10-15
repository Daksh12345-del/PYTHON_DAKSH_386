def square(n):
    #doc string basically ek triple quote string ko likhta hai end mein aur agar kuch nn likha ho toh none deta hai
    """This function calculates and prints the square of a number.
    """
    print(n**2)
square(3)
print(square.__doc__) # it will print the docstring


#doc string just function define karne ke baad aati hai
def square(n):
    print(n)
    """This function calculates and prints the square of a number.
    """
    print(n**2)
square(3)
print(square.__doc__) # it will print the docstring