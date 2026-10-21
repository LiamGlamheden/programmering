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
## Del 3: Debuggern
## Del 4: Refaktorering