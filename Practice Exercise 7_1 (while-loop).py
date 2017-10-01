getal = 0
eind = 0
while True:
    inp = int(input("Geef een getal:"))
    if inp == 0:
        print('Er zijn '+str(eind)+' getallen ingevoerd, de som is: '+str(getal))
        break
    else:
        getal += inp
        eind += 1