while(True):
        
    svarstid = float(input("ange svarstid= "))

    bedomning = round(svarstid)

    if(bedomning < 0):
        print("Ogiltigt värde")
    elif(bedomning < 50):
        print("Utmärkt")
    elif(bedomning < 150):
        print("Bra")
    elif(bedomning < 500):
        print("Långsam")
    elif(bedomning > 499):
        print("Ingen användbar kontakt")
    else: print("Ett fell uppstod försök försök igen")