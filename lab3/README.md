# Lab 3 – E. Lösenordskontroll
Gjort av: Liam Glamheden
## Del 1: Projektbeskrivning


1. Programmets namn och vad det gör
Lösenordskontroll – Programmet kontrollerar om ett lösenord följer lösenordspolicyn.

2. Användaren
Servicedesk som hjälper användare att byta lösenord. Programmet ska vara enkelt att använda och ge tydliga felmeddelanden.

3. Menyvalen

1. Kontrollera lösenord – Kontrollerar om lösenordet följer policyn.
2. Visa lösenordspolicy – Visar vilka krav som gäller för lösenord.
3. Avsluta – Avslutar programmet.

4. Indata
Användaren skriver in ett lösenord. Lösenordet ska vara minst 15 tecken långt och får inte finnas med bland vanliga lösenord.

## Del 2: Pseudokod och flödesschema

START
start loop
SÅ LÄNGE programmet körs:
    Skriv ut menyval 1: Kontrollera lösenord
    Skriv ut menyval 2: Visa lösenordspolicy
    Skriv ut menyval 3: Avsluta

    Läs in menyval

    OM menyval är 1:
        Läs in användarnamn
        Läs in lösenord

        OM lösenordet är kortare än 15 tecken:
            Visa felmeddelande
        ANNARS OM lösenordet är vanligt:
            Visa felmeddelande
        ANNARS OM lösenordet innehåller användarnamnet:
            Visa felmeddelande
        ANNARS:
            Visa att lösenordet är godkänt

    ANNARS OM menyval är 2:
        Visa lösenordspolicyn

    ANNARS OM menyval är 3:
        Avsluta programmet

    ANNARS:
        Visa felmeddelande
avslutad loop
SLUT

![Flödesschema](flodesschema.png).


## Del 4: Användartest

Användare: Eddie

Uppgift Klarade testaren det? (ja / delvis / nej)

Vad hände, och vad sa testaren?

1. kontrollera ett rätt lösenord

   resultat: Kunde inte se antalet tecken han hade skrivit in och skrev för kort. Efter felmeddelandet löste han problemen. Han fick inte tillräckliga instruktioner eftersom användaren tryckte på 1 först och inte på 2 för att se policyn.

2. kontrollera ett felaktigt lösenord

   resultat: Lyckades, men behövde läsa lösenordspolicyn.

Försök att krascha programmet

```
resultat: Användaren lyckades inte krascha programmet, även om han testade på många olika sätt, som att skriva ett jättelångt användarnamn och att skriva bokstäver i stället för siffror.
```

Testarens återkoppling

Efter testet svarar testaren på tre frågor. Skriv ner svaren i README.md.

1. Vad fungerade bra?

Instruktionerna visade relevant information. Felmeddelandena var också till god hjälp då de gav feedback på vad jag behövde lägga till eller ändra.

2. Var var du osäker, eller vilket felmeddelande var svårt att förstå?

Det var lite svårt att förstå vilka regler man skulle följa innan man såg lösenordspolicyn. Så om man tryckte på 1 först var det lite oklart.

3. Om du fick ändra en sak, vad skulle det vara?

Jag hade gjort lösenordspolicyn mer tillgänglig.

När du ger återkoppling: var konkret och vänlig. Skriv "jag visste inte om jag skulle skriva MB eller GB" i stället för "det var otydligt".



## Del 5: Förbättringar och reflektion

Vad testaren märkte
Att de var svårt att skriva ett lösenord som följde policy innan dem såg det

Vad jag ändrade
Jag valde att istället visa lösenord policy som val 1 istället för val 2. det hade gjort de lite mer självklar för användare att kolla där först.

Commit-meddelande
uppdaterad if sats annam meny ordning
# Reflektion

Svara kort, några meningar per fråga:

**1. Vad var svårast i projektet, och hur löste du det?**

Att hoppa in i startkoden och kombinera den med byggkoden. Det tog lite tid för mig att förstå den helt och att veta var jag skulle implementera byggdelen.

**2. Vad lärde du dig av användartestet som du inte hade märkt själv?**

Jag lärde mig att en användare kanske oftast strävar efter att gå till det första möjliga alternativet och att det kan vara viktigare att ge informationen till användaren först.

**3. Vem kan drabbas? Finns det användare som ditt program fungerar sämre för, till exempel den som använder skärmläsare? Vad skulle du göra med mer tid?**

Jag tror att äldre hade kunnat drabbas, eftersom de förmodligen hade behövt se policyn först innan de börjar skriva in lösenordet.
