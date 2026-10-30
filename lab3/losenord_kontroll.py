# Lab 3 – Losenord_kontroll // Lösenord kontroll
# Gjort av: Liam Glamheden
# Beskrivning: Servicedesk som hjälper användare att byta lösenord. Programmet ska vara enkelt att använda och ge tydliga felmeddelanden.


import getpass

# Konstanter för lösenordskontrollen
MIN_LANGD = 15

VANLIGA = ["123456", "password", "qwerty123",
           "sommar2026", "lösenord"]


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

    while True:
        try:
            anvandarnamn = input("Skriv ditt användarnamn: ").strip()

            if not anvandarnamn:
                raise ValueError

        except ValueError:
            print("Fel! Du måste skriva ett användarnamn.")
            continue

        break

    while True:
        try:
            losenord = getpass.getpass(
                "Skriv ditt lösenord (syns inte): "
            )

            if not losenord.strip():
                raise ValueError

        except ValueError:
            print("Fel! Du måste skriva ett lösenord.")
            continue

        break

    problem = kontrollera(losenord, anvandarnamn)

    if len(problem) == 0:
        print("Lösenordet är godkänt!")
    else:
        print("Lösenordet är inte godkänt:")
        for fel in problem:
            print("-", fel)


# Menyval 2 – Visa lösenordspolicy
def visa_losenord_policy():
    print("Lösenordspolicy")
    print("1. Lösenordet måste vara minst", MIN_LANGD, "tecken.")
    print("2. Lösenordet får inte vara vanligt eller läckt.")
    print("3. Lösenordet får inte innehålla användarnamnet.")
    print("4. Lösenordet behöver inte innehålla olika teckentyper.")

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
