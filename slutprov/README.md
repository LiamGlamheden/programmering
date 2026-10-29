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
Jag har valt att validera IP-adressen som användaren skriver in när enheten skapas. Jag kontrollerar också att IP-adressen faktiskt tillhör det angivna nätverket.

Jag har också valt att använda flera try- och except-block för att fånga upp fel, till exempel om användaren skriver in en sträng där det ska vara ett heltal. Jag kontrollerar även att användaren väljer ett giltigt alternativ i menyn.

Jag delade upp koden i olika delar för att kunna återanvända funktionerna.

Jag delade upp koden så att man ska kunne återanvända funktionerna.
## AI - logg
Jag använde ChatGPT lite grann, främst när jag arbetade med IP-modulen. I början var jag osäker på hur den fungerade och bad AI om hjälp när jag skrev fel. Jag skrev först koden själv och frågade sedan om hjälp när jag fastnade.

För resten av programmet, framför allt menyn, arbetade jag mest själv. Jag ställde några enstaka frågor till AI när jag hade problem med listan. Jag försökte främst att själv ta reda på hur man kunde lösa problemen och kollade även upp information på W3Schools. AI var till hjälp när jag fastnade med IP-modulen.

## Reflektion
Reflektion 1

Programmet fungerar genom att användaren först får ange nätverkets adress. När användaren sedan skapar en enhet får hen skriva in en IP-adress. Om IP-adressen stämmer överens med nätverket kan användaren spara enheten.

Reflektion 2

Jag tyckte att det var svårt i början att förstå hur valideringen fungerade och hur jag kunde kontrollera användarens inmatning. Jag fick därför söka information och försöka förstå hur det fungerade. Efter ett tag förstod jag det bättre och kunde implementera det i min kod.

## Testtabel (för A)