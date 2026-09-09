def main():
    time=input("What time is it?")
    convert(time)

def convert(time):
    hours, minutes = time.split(":")
    hours=int(hours)
    minutes=int(minutes)
    time = hours + minutes / 60
    if time>=7 and time<=12:
        print("Breakfast time!")

    if time>=12 and time<=18:
        print("Lunch time!")

    if time>=18 and time<=20:
        print("Dinner time!")

if __name__ == "__main__":
    main()
