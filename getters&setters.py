#getters:used to access value of an object attribute
#setters:used to set or update value of an object attribute
class MyClass:
    def __init__(self, value):
        self._value = value  # Private attribute
    def show(self):
            print("Value is:",self._value)
    # Getter method
    @property
    def ten_value(self):
        return 10* self._value
        # # Setter method
    @ten_value.setter 
    def ten_value(self, new_value):
        if new_value >= 0:  # Example validation
            self._value = new_value
        else:
            raise ValueError("Value must be non-negative")

object = MyClass(10)
object.ten_value = 20  # Using setter to update value
print(object.ten_value)  # Accessing private attribute directly (not recommended)
object.show()
#encapsulation: can be defined focuses on output restriction of access to certain components and not on method