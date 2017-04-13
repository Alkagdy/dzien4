import string

zdanie = input("Napisz coś:")

litery = 0
cyfry = 0

male_litery = 0
duze_litery = 0

for i in zdanie:
    if i.isdigit():
        cyfry +=1
    elif i.isalpha():
        litery +=1
        if i in string.ascii_lowercase:
            male_litery +=1
        else:
            duze_litery +=1


print("Litery:", litery)
print("Cyfry:", cyfry)
print("Male litery:", male_litery)
print("Duze litery:", duze_litery)
