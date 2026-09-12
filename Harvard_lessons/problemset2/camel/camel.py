    # implement a program that prompts the user for the name of a var in camel case and O/P the corresponding
    # name in snake case.Assume that the user’s input will indeed be in camel case.
def Snakecase(Variable):
    output = " "
    for i in range(len(Variable)):
        if(Variable[i].isupper()) and Variable[i] != Variable[0]:
            output = output + " _ " + Variable[i].lower()
        else:
            output = output+Variable[i]
    print(output)

def main():
    Camelcaseinput = input("Please enter Camel Case Variable ")
    Snakecase(Camelcaseinput)

if __name__ == "__main__":
    main()
