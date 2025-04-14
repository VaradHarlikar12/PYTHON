#Lambda is an anuonamous function used for making done reductante
# A lambda function can take any number of arguments, but can only have one expression.
# cube=lambda x:x*x*x
# square=lambda x:x*x
#
# while True:
#     no=int(input("Enter a number: "))
#     if(no>100):
#         print("number too large")
#     else:
#         print("Cube of number is:",cube(no))
#         print("Square of numebr is:",square(no))
#

def add_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 100:
            print("Number too large, exiting.")
            break
        else:
            result = (lambda x: x + 1)(n)  # Call the lambda immediately
            print("Result:", result)


add_number()