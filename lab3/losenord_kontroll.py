# Lab 3 – Losenord_kontroll // Lösenord kontroll
# Gjort av: Liam Glamheden
# Beskrivning: Servicedesk som hjälper användare att byta lösenord. Programmet ska vara enkelt att använda och ge tydliga felmeddelanden.

# Frågar tills användaren skriver ett heltal mellan minsta och storsta
def las_heltal(fraga, minsta, storsta):
    while True:
        try:
            tal = int(input(fraga))
        except ValueError:
            print("Fel: skriv ett heltal, till exempel", minsta)
        else:
            if minsta <= tal <= storsta:
                return tal
            print("Fel: talet måste vara", minsta, "till", storsta)


def visa_meny():
    print()
    print("[Programmets namn] – huvudmeny")
    print("1. [Första valet]")
    print("2. [Andra valet]")
    print("3. Avsluta")


def val_ett():
    # Byt namn på funktionen och skriv din kod här
    print("Inte klart än.")


def val_tva():
    print("Inte klart än.")


# Huvudprogram
while True:
    visa_meny()
    val = input("Välj 1, 2 eller 3: ").strip()

    if val == "1":
        val_ett()
    elif val == "2":
        val_tva()
    elif val == "3":
        print("Avslutar. Hej då!")
        break
    else:
        print("Ogiltigt val. Skriv 1, 2 eller 3.")