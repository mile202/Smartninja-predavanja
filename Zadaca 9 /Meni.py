from collections import OrderedDict

cijena1 = str(33.00) + "Kn"
cijena2 = str(24.50) + "Kn"
cijena3 = str(10.00) + "Kn"
cijena4 = str(36.00) + "Kn"
cijena5 = str(36.00) + "Kn"
cijena6 = str(55.00) + "Kn"
cijena7 = str(110.00) + "Kn"
cijena8 = str(25.00) + "Kn"
cijena9 = str(10.00) + "Kn"
cijena10 = str(120.00) + "Kn"

moj_Meni = OrderedDict()

moj_Meni["Cevapi"] = cijena1
moj_Meni["Hamburger"] = cijena2
moj_Meni["Juha"] = cijena3
moj_Meni["Naravni Odrezak"] = cijena4
moj_Meni["Becki Odrezak"] = cijena5
moj_Meni["Mjesano Meso"] = cijena6
moj_Meni["Mesna Plata"] = cijena7
moj_Meni["Lignje sa zara"] = cijena8
moj_Meni["Mjesana Salata"] = cijena9
moj_Meni["Specijalitet Kuce"] = cijena10



i=1
for k, v in moj_Meni.items():
    print(i, k, v)
    i+=1

broj_Narudzbe = int(input("Izaberite jelo: "))
jelo=list(moj_Meni.items())[broj_Narudzbe-1]

print("Izabrali ste:", jelo[0], "Cijena: " + str(jelo[1]) + " KN")

while True:

    nova_naruzdba = raw_input("Zelite li naruciti jos? (Y/N) ")
    if nova_naruzdba == "Y" or nova_naruzdba == "y":
        broj_Narudzbe = int(input("Izaberite jelo: "))
        jelo = list(moj_Meni.items())[broj_Narudzbe - 1]
        print("Izabrali ste:", jelo[0], "Cijena: " + str(jelo[1]) + " KN")
    elif nova_naruzdba == "N" or nova_naruzdba == "n":
         print ("\nHvala na narudzbi, DOBAR TEK!")
         break

    else:
        print ("Pogresan unos, pokrenite program ponovno za novu narudzbu!")








