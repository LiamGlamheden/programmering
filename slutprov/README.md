# Slutprov - IP-register
Gjort av: Liam Glamheden
## Pseudokod

Start
    Start av huvudloop
        Utdata: "1. Lägg till enhet. 2. Visa alla enheter. 3. Avsluta."
        Indata: "Skriv det alternativ du vill välja. Skriv alternativet som ett heltal."
        Catch: Om användaren skriver in en sträng, skriv "Fel. Skriv in ett heltal."
        Om användaren skriver 1
            Utdata: "Skriv enhetens namn, t.ex. skrivare-01."
            Indata: "Enhetens namn"
            Indata: "Skriv in IP-adressen."
            Om användaren skriver in en IP-adress som är utanför nätverket
                Utdata: "Skriv den korrekta IP-adressen för detta nätverk." och loopa tillbaka till inmatningen av IP-adressen.
            Utdata: "Skrivare-01 har fått adressen 192.168.10.20."
            Avsluta loop
        Om användaren skriver 2
            Utdata: "Skriv ut alla enheter i listan."
        Om användaren skriver 3
            Utdata: "Avsluta."
    Slut på huvudloop
Slut


## Redogörelse

## AI - logg

## Reflektion

## Testtabel (för A)