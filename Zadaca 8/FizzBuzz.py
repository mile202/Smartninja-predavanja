print ("Fizz | Buzz igra," + "dobrodosli".upper())

fizzbuzz = []

start = int(input("Molim vas unesite jedan broj od 1 do 100 :"))
end = int(input("Molim vas unesite drugi broj od 1 do 100:"))

for i in range(start,end+1):
    entry = ''
    if i%3 == 0:
        entry += "fizz"
    if i%5 == 0:
        entry += "buzz"
    if i%3 != 0 and i%5 != 0:
        entry = i



    fizzbuzz.append(entry)

for i in fizzbuzz:
    print(i)
