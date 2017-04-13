#break

imie = "Hermenegilda"

for litera in imie:
    if litera =='n':
        break
    print(litera)
print("Koniec")

imie2 = "Agnieszka"
imie3 = "Alicja"

for litera1, litera2 in zip(imie2, imie3):
    print(litera1, litera2)

indeks = '0123456789012'
zdanie = 'Ala ma kota kot ma Ale'

for i, l in zip(indeks, zdanie):
    print(i, l)

