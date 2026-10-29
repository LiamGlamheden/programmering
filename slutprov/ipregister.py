import ipaddress

while True:
    print("Skriv nätverkets nät: tex 192.168.10.0/24")

    try:
        natet = input("")
        natet = ipaddress.ip_network(natet)

    except ValueError:
        print("Fel! Skriv in ett giltigt nätverk. Och ha med /")
        continue

    print("Skriv in nätverkets IP: tex 192.168.10.25")

    try:
        ip = input("")
        ip = ipaddress.ip_address(ip)

    except ValueError:
        print("Fel! Skriv in en giltig IP-adress.")
        continue

    if ip in natet:
        print("IP-adressen tillhör nätverket!")
    else:
        print("IP-adressen tillhör inte nätverket!")

    break


while True:
    print("1. Lägg till enhet. 2. Visa alla enheter. 3. Avsluta")

    try:
        meny_val = int(input("Välj ett alternativ: "))

        
    except ValueError:
        print("felaktigt värde skriv med siffror och välja mellan meny valen") 

