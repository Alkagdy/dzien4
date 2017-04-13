#policzyc ilosc liczb parzystych i nieparzystych

zakres = range(23, 3495846)

ilosc_parzyste = 0
ilosc_nieparzystych = 0

for i in zakres:
    if i % 2 ==0:
        ilosc_parzyste +=1
    else:
        ilosc_nieparzystych +=1

#drukuj ilosc
print("Ilosc parzystych: {}, nieparzystych {}".format(ilosc_parzyste, ilosc_nieparzystych))