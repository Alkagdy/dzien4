#petla for

#range

x = range(100)
print(x)

for liczba in x:
    print(liczba)

for litera in "Aleksandra":
    print(litera)

for litera in "Aleksandra" [::-1]:
    print(litera)

for litera in "Aleksandra":
    print(litera.capitalize())

for litera in "Aleksandra":
    print("Nie korzystam z litery!")

imie = "Hermenegilda"
indeks = 0
for c in imie:
    print(indeks, c)
    indeks +=1

imie = "Bartoszek"
for i,c in enumerate(imie):
    print(i, c)