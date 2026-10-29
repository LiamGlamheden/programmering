import ipaddress

## Ett program där man kan spara enheter och rätt nät.
enheter = []

while True:
    print("Skriv nätverkets nät: tex 192.168.10.0/24")

    try:
        natet = input("")
        natet = ipaddress.ip_network(natet)

    except ValueError:
        print("Fel! Skriv in ett giltigt nätverk. Och ha med /")
        continue

    break


## Skapar enheter och ser till att de tillhör rätt nät.
def lagg_till_enhet():
    print("Du har valt 1.")

    try:
        enhet_namn = input("Skriv namnet på enheten: ")

        if not enhet_namn.strip():
            raise ValueError

        enhet_ip = input("Skriv IP till enheten: ")
        enhet_ip = ipaddress.ip_address(enhet_ip)

        if enhet_ip in natet:
            print("IP-adressen tillhör nätverket! Enheten är tillagd.")
            enheter.append([enhet_namn, enhet_ip])
        else:
            print("IP-adressen tillhör inte nätverket!")

    except ValueError:
        print("Felaktigt värde. Namnet får inte vara tomt och IP-adressen måste vara giltig.")


## Visar alla enheter i listan.
def visa_alla_enheter():
    print("Du har valt 2.")

    enhet_nummer = 1

    for nuvarande_enhet in enheter:
        print(enhet_nummer, nuvarande_enhet)
        enhet_nummer = enhet_nummer + 1

    if not enheter:
        print("Det finns inga sparade enheter.")


## Avslutar programmet.
def avsluta_program():
    print("Programmet är avslutat.")


while True:
    print("1. Lägg till enhet. 2. Visa alla enheter. 3. Avsluta")

    try:
        meny_val = int(input("Välj ett alternativ: "))

        if meny_val > 3:
            print("För högt")
            continue

        elif meny_val < 1:
            print("För lågt")
            continue

        elif meny_val == 1:
            lagg_till_enhet()

        elif meny_val == 2:
            visa_alla_enheter()

        elif meny_val == 3:
            avsluta_program()
            break

    except ValueError:
        print("Felaktigt värde! Skriv en siffra och välj mellan menyvalen 1–3.")
