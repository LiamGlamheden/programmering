# Lab 3 – Losenord_kontroll // Lösenord kontroll
# Gjort av: Liam Glamheden
# Beskrivning: Servicedesk som hjälper användare att byta lösenord. Programmet ska vara enkelt att använda och ge tydliga felmeddelanden.


import getpass

# Konstanter för lösenordskontrollen
MIN_LANGD = 15

VANLIGA = ["123456", "password", "qwerty123",
           "sommar2026", "lösenord"]

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
    print("Lösenord kontroll – huvudmeny")
    print("1. Kontrollera lösenord")
    print("2. Visa lösenord policy")
    print("3. Avsluta")




# Kontrollerar om lösenordet följer policyn
def kontrollera(losenord, anvandarnamn):
    problem = []

    if len(losenord) < MIN_LANGD:
        problem.append("för kort – minst 15 tecken")

    if losenord.lower() in VANLIGA:
        problem.append("finns i listan över vanliga lösenord")

    if anvandarnamn.lower() in losenord.lower():
        problem.append("innehåller användarnamnet")

    return problem


# Menyval 1 – Kontrollera lösenord
def kontrollera_losenord():
    anvandarnamn = input("Skriv ditt användarnamn: ").strip()

    losenord = getpass.getpass(
        "Skriv ditt lösenord (syns inte): "
    )

    problem = kontrollera(losenord, anvandarnamn)

    if len(problem) == 0:
        print("Lösenordet är godkänt!")
    else:
        print("Lösenordet är inte godkänt:")
        for fel in problem:
            print("-", fel)


def visa_losenord_policy():
    print("Inte klart än.")


# Huvudprogram
while True:
    visa_meny()
    val = input("Välj 1, 2 eller 3: ").strip()

    if val == "1":
        kontrollera_losenord()
    elif val == "2":
        visa_losenord_policy()
    elif val == "3":
        print("Avslutar. Hej då!")
        break
    else:
        print("Ogiltigt val. Skriv 1, 2 eller 3.")