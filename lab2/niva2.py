HEMLIG_PORT = 443

antal_gissningar = 0
while(True):

    gissning = int(input("Gissa den hemliga porten, den ligger mellan 1-1023: "))

    if antal_gissningar < 10:

        if(gissning == HEMLIG_PORT):
            print("Grattis! Du gissade rätt.")
            print("Du gissade", antal_gissningar, "gånger innan du hittade rätt port.")
            break
        elif(gissning > HEMLIG_PORT):
            print("För högt")
            antal_gissningar += 1
        elif(gissning < HEMLIG_PORT):
            print("För lågt")
            antal_gissningar += 1

    else:
        print("Du har gissat för många gånger. Försök igen.")
        print("Den hemliga porten var", HEMLIG_PORT)
        break