#haslo musi miec minimum 6 znakow, litery i cyfry


haslo = input("Podaj haslo:")
while len(haslo) <6:
        print("Haslo jest za krotkie",end=" ")
        print("Podaj prawidlowe haslo")
        haslo = input("Podaj prawidlowe haslo:")

while not haslo.isalnum():
    print("Haslo musi miec litery i cyfry")
    haslo = input("Podaj ponownie haslo:")


print("Poodano prawidlowe haslo")
