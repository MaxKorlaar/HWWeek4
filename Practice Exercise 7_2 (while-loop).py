def vierletter():
    while True:
        woordje = input("Voer een string van vier letters in: ")
        lengte = len(woordje)
        if lengte == 4:
            print("Inleren van correcte string: '" + woordje + "' is geslaagd")
            break
        else:
            print("'" + woordje + "' heeft " + str(lengte) + " letters")
            woordje

vierletter()
