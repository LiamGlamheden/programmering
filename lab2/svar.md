# Lab 2 – Svar
## Del 1

Nivå 1 - klassa svarstiden

*Vad är indata?*
Svarstiden i millisekunder. 

*vad är utdata*
En bedömning av svarstiden.

pseudokoden:
1. läs in svarsiden
2. Omvandla svarstid till heltal
3. Om svarstiden är mindre än 0, skriv ut ”Ogiltigt värde”.
4. Annars om svarstiden är mindre än 50, skriv ut ”Utmärkt”.
5. Annars om svarstiden är mindre än 150, skriv ut ”Bra”.
6. Annars om svarstiden är mindre än 500, skriv ut ”Långsam”.
7. Annars, skriv ut ”Ingen användbar kontakt”.

Test:
| Svarstid | Förväntat               | Faktiskt                | OK? |
| -------- | ----------------------- | ----------------------- | --- |
| 12       | Utmärkt                 | Utmärkt                 | Ja  |
| 49       | Utmärkt                 | Utmärkt                 | Ja  |
| 50       | Bra                     | Bra                     | Ja  |
| 149      | Bra                     | Bra                     | Ja  |
| 150      | Långsam                 | Långsam                 | Ja  |
| 500      | Ingen användbar kontakt | Ingen användbar kontakt | Ja  |
| -3       | Ogiltigt värde          | Ogiltigt värde          | Ja  |


nivå 2 

Binärsökning: Gissa mitten av intervallet och halvera det efter varje gissning.


Nivå 3

Detta kan vara bra att veta för att förstå om programmet är otydligt eller om någon försöker attackera systemet.

## Del 2: Feltabell
medel värde = 71

| Nr | Rad | Feltyp         | Hur hittade du felet? | Vad var fel?                 | Rättning               | Förebyggande           |
| -- | --- | -------------- | --------------------- | ---------------------------- | ---------------------- | ---------------------- |
| 1  | 22  | Syntaxfel      | Felmeddelande         | Citattecken saknades.        | Lade till `"`          | Kontrollera strängar.  |
| 2  | 7   | Syntaxfel      | Felmeddelande         | Kolon saknades.              | Lade till `:`          | Kontrollera syntax.    |
| 3  | 25  | Exekveringsfel | Felmeddelande         | Tal + text.                  | Lade till ','- `+`      | Kontrollera datatyper. |
| 4  | 26  | Exekveringsfel | Felmeddelande         | Index 4 fanns inte.          | Ändrade till 3.        | Kontrollera index.     |
| 5  | 13  | Logiskt fel    | Fel resultat          | Första värdet hoppades över. | Startade på 0.         | Kontrollera loopar.    |
| 6  | 10  | Logiskt fel    | Fel resultat          | 80 räknades inte.            | Ändrade `>` till `>=`. | Testa gränsvärden.     |


## Del 3: Debuggern

Gissning:
Jag tror utrskiften kommer att se ut så här:
Misslyckade totalt: 3
Timmar med larm: 1

Misslyckade totalt: 0 "kanske 1"
Timmar med larm: 0

Misslyckade totalt: 5 
Timmar med larm: 3

Misslyckade totalt: 1
Timmar med larm: 0

Sen slutar programmet tror jag.

| När programmet pausar | antal | misslyckade | timmar_med_larm |
| --------------------- | ----- | ----------- | --------------- |
| Rad 5, varv 1         | 3     | 0           | 0               |
| Rad 5, varv 2         | 0     | 3           | 1               |
| Rad 5, varv 3         | 5     | 3           | 1               |
| Rad 5, varv 4         | 1     | 8           | 2               |
| Rad 8, efter loopen   | 1     | 9           | 2               |

1. Stämde din gissning? Om inte, vad tänkte du fel?
 Delvis. Några delar av mina gissningar stämde, men jag hade också fel på många. På den första trodde jag att det skulle bli ett misslyckande eftersom det var 3 stycken. Jag trodde också att programmet hade hoppat fram två gånger när vi startade vid rad 5.

Jag hade också fel på den andra. Jag trodde att allt skulle bli noll. Det kan ha varit för att jag trodde att värdena från det tidigare varvet inte skulle följa med.

På den tredje hade jag också fel. Jag trodde att programmet skulle fortsätta lägga till även efter 3 försök.

Om jag ska sammanfatta vad jag tror har hänt, eftersom jag fortfarande är lite osäker, så är det förmodligen att datan inte följde med på det sättet jag förväntade mig.

2. Varför ändras timmar_med_larm inte i varje varv?

Det ändras bara när antal är 3 eller mer. Om antal är mindre än 3 körs inte if-satsen och då ändras inte värdet.

3. Vilket värde har antal när loopen är klar? Förklara varför.

antal har värdet 1 när loopen är klar. Det beror på att 1 är det sista värdet i listan inloggningar, och variabeln antal får det värdet i det sista varvet.

4. Hur kan debuggern hjälpa dig att hitta ett logiskt fel, som felen i Del 2?

Debuggern gör att man kan följa programmet rad för rad och se hur variablernas värden ändras. Då kan man se var programmet börjar ge ett felaktigt resultat och lättare hitta det logiska felet.

## Del 4: Refaktorering

tot 1055
snitt 211.0
hog 2

Ändringar:
Jag gjorde texten till utskriften tydligare. Så att de är lättare att läsa
Gett bättre namn givning
Lagt till en konstant för GRANS
Lagt till två funktioner för att räkna summan och räknar långsamma svar.
Lagt till kommentarer som föklarar varför jag lag till funktioner

**2. Hur kontrollerade du att din nya version räknar ut exakt samma sak som den gamla?**

Jag körde programmet och kontrollerade att resultatet blev samma som i den gamla versionen. Summan blev 1055, genomsnittet 211.0 och antalet svar över gränsen blev 2.

**3. Varför är det viktigt med läsbar kod i ett driftteam, där flera personer använder och ändrar samma skript?**

Läsbar kod gör det enklare för andra i teamet att förstå, felsöka och ändra skriptet. Det minskar risken för misstag och gör samarbetet lättare.
