import ipaddress

while True:
    print("Skriv nätverkets nät: tex 192.168.10.0/24")

    try:
        natet = input("")
        natet = ipaddress.ip_network(natet)

    except ValueError:
        print("Fel! Skriv in ett giltigt nätverk. Och ha med /")
        continue


    break


while True:
    print("1. Lägg till enhet. 2. Visa alla enheter. 3. Avsluta")

    try:
        meny_val = int(input("Välj ett alternativ: "))

        if meny_val > 3 :
            print("För högt")
            raise ValueError
        elif meny_val < 1:
            print("för lågt")
            raise ValueError
        elif meny_val == 1:
            print("Du har valt 1.")

            try:

                enhet_namn = input("Skriv namnet på enheten: ")

                if not enhet_namn.strip(): 
                    raise ValueError

                enhet_ip = input("Skriv ip till enheten: ")

                if ip in natet:
                    print("IP-adressen tillhör nätverket!")
                else:
                    print("IP-adressen tillhör inte nätverket!")



            except ValueError:
                print("Felaktigt värde. Namnet får inte vara tomt Ip adressen ska vara en giltigt ip i nätet")

           

        elif meny_val == 2: 
            print("Du har valt 2.")
        elif meny_val == 3:
            print("programmet är avslutat")
            break

        
    except ValueError:
        print("felaktigt värde skriv med siffror och välja mellan meny valen 1 - 3") 

