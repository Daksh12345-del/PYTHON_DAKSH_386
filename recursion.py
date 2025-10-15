#recursion:function ke andar function ko call karna recursion kehlata hai
def factorial(n):
    """Returns the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n=int(input("Enter a number:"))
print(factorial(n))

#fibonacci series
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter a positive integer: "))
