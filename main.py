# ✅ Mercedes Sprinter 517 CDI, 5500 KG, 140 KW, 7367 mm
# ✅ Anvelope 205/75/R16 C
# ✅ Rezervor princpial 93 litri
# ✅ Cutie de viteze manuală ECO Gear pe 6 trepte


def specificationsParser(ml):
    with open(ml, 'a') as file:

        firma = input("Introduceți firma masinii (ex. Mercedes): ")

        model = input("Introduceți modelul masinii (ex. Sprinter 517 CDI): ")

        kg = input("Introduceți greutatea maxima a masinii (ex. 5000): ")
        try:
            int(kg)
            pass
        except ValueError:
            print("Greutatea trebuie să fie un număr întreg.")
            kg = input("Introduceți greutatea maxima masinii (ex. 5000): ")


        kw = input("Introduceți puterea motorului masinii (ex. 140): ")
        try:
            int(kw)
            pass
        except ValueError:
            print("Puterea motorului trebuie să fie un număr întreg.")
            kw = input("Introduceți puterea motorului masinii (ex. 140): ")


        latime = input("Introduceți latimea masinii (ex. 7367): ")
        try:
            int(latime)
            pass
        except ValueError:
            print("Latimea trebuie să fie un număr întreg.")
            latime = input("Introduceți latimea masinii (ex. 7367): ")



        file.write(f"✅ {firma} {model}, {kg} KG, {kw} KW, {latime} mm\n")



        anvelope = input("Introduceți dimensiunea anvelopelor (ex. 205/75/R16 C): ")

        file.write(f"✅ Anvelope {anvelope}\n")



        rezervor = input("Introduceți capacitatea rezervorului principal (ex. 93): ")
        try:
            int(rezervor)
            pass
        except ValueError:
            print("Capacitatea rezervorului trebuie să fie un număr întreg.")
            rezervor = input("Introduceți capacitatea rezervorului principal (ex. 93): ")

        file.write(f"✅ Rezervor principal {rezervor} L\n")



        cutie = input("Introduceți tipul cutiei de viteze (ex. manuala/autoamata): ")
        if cutie == "automata" or cutie=="automată":
            file.write(f"✅ Cutie de viteze automată 9G-TRONIC\n")
        elif cutie == "manuala" or cutie=="manuală":
            file.write(f"✅ Cutie de viteze manuală ECO Gear pe 6 trepte\n")


def optionParser(line):
    # For each line, ask if the product has that specific option
    # Wait for a Y/N response
    print("\n")
    print(line)

    # If the product has a similar option than the one displayed, type M to modify the option
    response = input("Are produsul această opțiune? Apăsați 'D' dacă DA, 'N' dacă NU, sau 'M' dacă doriți să modificați opțiunea (D/N/M): ")
    # If the response is Y, add "✅ " plus the option to result.txt
    # If the response is N, skip to the next line
    if response == "D" or response == "d":
        with open(ml, 'a') as file:
            file.write("✅ " + line + "\n")
            return("da")
    elif response == "N" or response == "n":
        print("Opțiunea nu a fost adăugată.")
        return("nu")
    elif response == "M" or response == "m":
        return("modifica")
    else:
        print("Răspuns invalid. Vă rugăm să răspundeți cu D, N sau M.")
        # If the response is not Y, N or M, ask for that line again continuously until a valid response is given
        while response != "D" or response != "N" or response != "M":
            response = input("Are produsul această opțiune? (D/N/M): ")
            if response == "D" or response == "d":
                with open(ml, 'a') as file:
                    file.write("✅ " + line + "\n")
                return("da")
            elif response == "N" or response == "n":
                print("Opțiunea nu a fost adăugată.")
                return("nu")
            elif response == "M" or response == "m":
                return("modifica")
            else:
                print("Răspuns invalid. Vă rugăm să răspundeți cu D,N sau M.")
                continue


def optionsParser(ml):
    # Read line by line from options.txt
    with open('options.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            result = optionParser(line)
            if result == "modifica":
                aux = input("Introduceți noua opțiune: ")
                with open(ml, 'a') as file:
                    file.write("✅ " + aux + "\n")



def customisableOptionsParser(ml):
    # Parse until the first $ is found
    # Prompt the user with the section found after the first $ and before the second $
    # Than continue with the next part of the line
    # And add the completed line to the result.txt file
    with open('custom_options.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            ok = input("Doriți să adăugați această opțiune? (D/N): ")
            if ok == "D" or ok == "d":
                sections = line.split("$")
                i = 0
                result = ""
                for section in sections:
                    if i%2==0:
                        result+=section
                        print(section)
                    else:
                        response = input("Introduceti " + section + ": ")
                        result+=response
                    i+=1
                with open(ml, 'a') as file:
                    file.write("✅ " + result + "\n")


ml = input("Introduceți codul de identficare al masinii (ex. 01 pentru ML-01): ")
ml="ML-"+ml+".txt"
specificationsParser(ml)
optionsParser(ml)
customisableOptionsParser(ml)


