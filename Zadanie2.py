zdanie = input("Napisz coś:")

litery = 0
cyfry = 0
samogloski = 'aeiouy'
ilosc_samoglosek = 0
ilosc_spolglosek = 0

for i in zdanie:
    if i.isdigit():
        cyfry +=1
    elif i.isalpha():
        litery +=1
        if i in samogloski:
            ilosc_samoglosek +=1
        else:
            ilosc_spolglosek +=1


print("Litery:", litery)
print("Cyfry:", cyfry)
print("Ilosc samoglosek:", ilosc_samoglosek)
print("Ilosc spolglosek:", ilosc_spolglosek)
