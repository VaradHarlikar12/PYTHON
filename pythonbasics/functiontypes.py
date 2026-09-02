# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.¸
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child1,child2,child3):
  print("The youngest child is " + child3)
  print("The oldest child is " + child1)
  print("The middle child is " + child2)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# To specify that a function can have only positional arguments, add , / after the arguments: