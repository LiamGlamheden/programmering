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

## Del 4: Refaktorering