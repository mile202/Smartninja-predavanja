# Uvoz radnom
import random

# Varijable
brojevi = (1, 100)
dozvoljeni_pokusaji = 10

tocan_broj = random.randint(*brojevi)
# Print podataka
print ("\t\t|------------------------------------------|")
print ("\t\t|\tDobro dosli u igricu pogodi tajni broj'! | ")
print ("\t\t|------------------------------------------|")
print("\t\t|\tMislim na jedan broj izmedu %d i %d.   |" % brojevi)
print ("\t\t|------------------------------------------|")
print("\t\t|Pokusaj pogoditi broj u sto manje pokusaja.|")
print ("\t\t|------------------------------------------|\n")

# FOR loop za pokusaje
for tries in range(dozvoljeni_pokusaji):
    guess = int(input("Unesite broj: "))

    if guess > tocan_broj:
        print("Nize...")
    elif guess < tocan_broj:
        print("Vise...")
    else:
        print("\nPogodili ste!!BRAVO!!  Tajni broj je bio %d" % (tocan_broj))
        print("Trebalo vam je samo %d pokusaja!\n\n" % (tries + 1))
        break
else:
    print("\nGAME OVER!!\nPonestalo vam je pokusaja! Dozvoljeno je samo %d pokusaja :)\nPokrenite program ponovno za novi pokusaj! :)\n" % (tries +1))

# Pokusaj pisanja da bi program radio u obje verzije (2 i 3)
try:
    input("Hvala na igranju! Pritisnite ENTER za izlaz iz igrice.")

except:
    pass

