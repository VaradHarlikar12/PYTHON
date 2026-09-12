usertweet=input("Enter a tweet please")
Vowels=["a","e","i","o","u"]

def Twttr(usertweet):
    output=""
    for i in range(len(usertweet)):
        if usertweet[i] not in Vowels:
            output = output + usertweet[i]
    print(output)


Twttr(usertweet)
