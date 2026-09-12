#2 letters,6 chara maximum and mini of 2 chara,no numbers between the plates only at end, no periods spaces puncatations

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(Vanityplate):
    special_characters = [".", ",", "!", "?", " "]
    numberic_value = ["0","1","2","3","4","5","6","7","8","9",]
    number_started = False
    if len(Vanityplate) > 6 or len(Vanityplate) < 2:
        return False
    else:
        for i in range(len(Vanityplate)):
            if  Vanityplate[i] in special_characters:
                return False

            if Vanityplate[i] in numberic_value:
                number_started = True

            elif number_started:
                return False

        if Vanityplate[0] in numberic_value:
            return False

    return True

main()
