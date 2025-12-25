#decorators modify a function behaviour
def greet(func):
    def wrapper():
        print("Greetings!")
        func()
    return wrapper
@greet
def hello():
    print("Hello, World!")
hello()