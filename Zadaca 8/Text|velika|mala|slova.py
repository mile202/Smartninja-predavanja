smallLetters = raw_input("Unesite bilo koju rijec pritisnite enter pa vidite sto se desava: ")

print("\n Vasa prva rijec: " + smallLetters.upper())

capitalLetters = raw_input("\n Unesite jos jednu rijec svim velikim slovima: ")

for letter in capitalLetters:
    if letter != capitalLetters.lower() :
        print ("\n Vasa druga rijec prvi nacin: " + capitalLetters.upper() + "\n Vasa druga rijec drugi nacin: " + capitalLetters.capitalize())
        break
    else:
        print ("Pogreska, pokrenite program ponovno!")
        break



