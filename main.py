# Object Introspection Functions

# 1.type()

# Description: Returns the type of an object.
# Example:
# Different types of variables
integer = 10
string = "Hello"
list = [1, 2, 3]

# Print their types
print(f"The type of {integer} is {type(integer)}")
print(f"The type of '{string}' is {type(string)}")
print(f"The type of {list} is {type(list)}")


# and thi's the second Functions

# 2.isinstance()
# Description: Returns True if an object is an instance of a specified class or any of its subclasses. This is the recommended way to check an object's type.
# Example:


value = 5.5

float = isinstance(value, float)
int = isinstance(value, int)
str = isinstance(value, str)

print(f"Is the value a float? {float}")
print(f"Is the value an int? {int}")
print(f"Is the value a str? {str}")  