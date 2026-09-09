def convert(String):
    String=String.replace(":)","🙂").replace(":(","🙁")
    if(String=="🙂"):
        print(f"Nice to here that you are happy{String}!")
    elif(String=="🙁"):
        print(f"Why are you sad?")
    else:
        print("Invalid input please enter ':)' or ':(' as your input")

def main():
    userinput=input("Enter ':)' or ':(' depending on your mood")
    convert(userinput)

main()