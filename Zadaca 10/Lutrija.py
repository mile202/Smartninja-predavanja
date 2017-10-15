import random


def lotto_brojevi(kolicina):
    lista_brojeva = []

    while True:
        if len(lista_brojeva) == kolicina:
            break

        brojevi_lotta = random.randint(1, 40)

        if brojevi_lotta not in lista_brojeva:
            lista_brojeva.append(brojevi_lotta)

    return lista_brojeva

def main():
    print "Dobrodosli u generator LOTTO brojeva."

    unos = raw_input("Molim unesite koliko nasumicnih brojeva zelite: ")

    try:
        kolicina_broj = int(unos)
        print lotto_brojevi(kolicina_broj)
    except ValueError:
        print "Molim vas unesite BROJ: "



if __name__ == "__main__":
    main()

    try:
        input("Hvala na koristenju! ENTER ZA DOVIDENJA.")

    except:
        pass
