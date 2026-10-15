OBS har fullskärm annars ser tabellen inte rätt ut.
# Lab 1 – Planering
## Problem 1
• Vad är indata?
Data som matas in av användaren, till exempel platskod (STO), enhetstyp (srv) och det senast använda numret (7).
• Vad är utdata?
Data som programmet visar, till exempel det nya hostnamnet (sto-srv-08).
• Vilka regler gäller? Tänk på små bokstäver, bindestreck och två siffror.
Hostnamnet ska bestå av en platskod, enhetstyp och ett tvåsiffrigt nummer. Allt ska skrivas med små bokstäver och delarna ska separeras med bindestreck.
• Vad kan gå fel?
Användaren kan mata in fel data, till exempel bokstäver i stället för ett nummer eller fel platskod och enhetstyp.

Planera:
1. LÄS IN platskod.
2. LÄS IN enhetstyp.
3. LÄS IN det senast använda numret.
4. BERÄKNA nästa nummer genom att öka det senaste numret med 1.
5. GÖR platskoden och enhetstypen till små bokstäver.
6. BERÄKNA hostnamnet genom att sätta ihop platskoden, enhetstypen och nästa nummer med bindestreck.
7. SKRIV UT nästa hostnamn.


Felmedelande TypeError: can only concatenate str (not "int") to str

svar:
Felet uppstår eftersom input() sparar inmatningen som text. Därför kan programmet inte addera texten med heltalet 1.

test:
| Platskod | Typ | Senaste nr | Förväntat  | Faktiskt | OK? |
|----------|-----|------------|------------|----------|-----|
| STO      | srv | 7          | sto-srv-08 | sto-srv-08   ja
| gbg      | SW  | 11         | gbg-sw-12  |  gbg-sw-12   ja
| sto      | srv | 0          | sto-srv-01 | sto-srv-01   ja
| mal      | pc  | 99         | ?mal-pc-100 | mal-pc-100  nej
| sto      | srv | sju        | ?  error    |   error    nej  

Vad händer med testet mal, pc, 99? Följer namnet fortfarande standarden? Vad borde företaget göra?

Numret går över till 100. Det följer inte standarden eftersom numret ska bestå av två siffror. Företaget borde bestämma vad som ska hända när numret går över 99.

Vilket fel ger det sista testet? Hur kan man förhindra sådana krascher?

Man kan använda en if-sats för att kontrollera att användaren matar in rätt data.



## Problem 2

 Kommer du ihåg från genomgången hur många bitar som går på en byte?
8 bitar.

• Vad är indata?

Filens storlek i GB och nätverkets bandbredd i Mbit/s, till exempel 1 GB och 100 Mbit/s.

• Vad är utdata?

Överföringstiden i sekunder och minuter.

• Vilka regler gäller?

Filstorleken kan vara ett decimaltal, till exempel 4,5 GB. Därför behöver man använda float. En byte består av 8 bitar, vilket är anledningen till att formeln multiplicerar med 8.

• Vad kan gå fel?

Användaren kan mata in fel data, till exempel text i stället för ett nummer eller 0 som bandbredd.

Exemple
\text{tid (s)} = \frac{\text{storlek (GB)} \times 1000 \times 8}{\text{bandbredd (Mbit/s)}}

1 GB på 100 Mbit/s

Sekunder: (1 × 1000 × 8) / 100 = 80 sekunder.
Minuter: 80 / 60 = 1,33 minuter.

Svar: Det tar 80 sekunder, vilket är ungefär 1,33 minuter.

Test
| Storlek (GB) | Bandbredd (Mbit/s) | Förväntat (s) | Förväntat (min) | Faktiskt | OK? |
|---|---|---|---|---|---|
| 1 | 100 | 80.0 | 1.33 | 80.0 s, 1.33 min | Ja |
| 4.5 | 250 | 144.0 | 2.40 | 144.0 s, 2.40 min | Ja |
| 50 | 1000 | 400.0 | 6.67 | 400.0 s, 6.67 min | Ja |
| 0.5 | 1000 | 4.0 | 0.07 | 4.0 s, 0.07 min | Ja |
| 1 | 0 | ? | ? | ZeroDivisionError | Nej |

Vilket fel ger det sista testet, och varför?

ZeroDivisionError: division by zero
Eftersom man försöker dela ett tal med noll.

I verkligheten tar överföringen oftast längre tid än programmet räknar ut. Ge två skäl till varför. Tänk på vad du vet om nätverk.
1. Eftersom bredbandshastigheten inte alltid är exakt jämn och kan ändras.
2. Eftersom andra enheter kan använda nätverket samtidigt, vilket kan göra överföringen långsammare.
## Problem 3

• Vad är indata?

Prefixlängden och antalet enheter som redan finns i nätverket, till exempel prefix 24 och 180 enheter.

• Vad är utdata?

Antalet adresser totalt, antalet användbara adresser och antalet lediga adresser.

• Vilka regler gäller?

En IPv4-adress består av 32 bitar. Prefixlängden visar hur många bitar som används för nätverksdelen. Två adresser är reserverade för nätverksadressen och broadcastadressen.

• Vad kan gå fel?*

Användaren kan skriva in fel data, till exempel text i stället för ett nummer eller en ogiltig prefixlängd. Antalet enheter kan också vara större än antalet användbara adresser.

planering
bryt ner problemet:
1. Läs in prefixlängden.
2. Läs in antalet enheter som redan finns i nätverket.
3. Räkna ut hostbitarna: 32 − prefixlängden.
4. Räkna ut totalt antal adresser: 2 upphöjt till antalet hostbitar.
5. Räkna ut användbara adresser: totalt antal adresser − 2.
6. Räkna ut lediga adresser: användbara adresser − antalet befintliga enheter.
7. Skriv ut resultaten.

pseudokod 
start
Läs in prefixlängd
Läs in antal befintliga enheter
Beräkna hostbitar = 32 − prefixlängd
Beräkna totalt antal adresser = 2 upphöjt till hostbitar
Beräkna användbara adresser = totalt antal adresser − 2
Beräkna lediga adresser = användbara adresser − antal befintliga enheter
Visa totalt antal adresser
Visa antal användbara adresser
Visa antal lediga adresser
slut

Testa planen för hand
in data: Prefixlängd: 24
in data: Befintliga enheter: 180
beräkning: Hostbitar: 32 − 24 = 8
beräkning: Totalt antal adresser: 2⁸ = 256
beräkning: Användbara adresser: 256 − 2 = 254
beräkning: Lediga adresser: 254 − 180 = 74
visa: Svar: 256 totalt, 254 användbara och 74 lediga adresser.

test 
| Test | Prefix | Enheter | Förväntat totalt | Förväntat användbara | Förväntat lediga | Faktiskt            | OK? |
| ---- | ------ | ------- | ---------------- | -------------------- | ---------------- | ------------------- | --- |
| 1    | 24     | 180     | 256              | 254                  | 74               | 256, 254, 74        | Ja  |
| 2    | 26     | 50      | 64               | 62                   | 12               | 64, 62, 12          | Ja  |
| 3    | 30     | 2       | 4                | 2                    | 0                | 4, 2, 0             | Ja  |
| 4    | 16     | 1000    | 65536            | 65534                | 64534            | 65536, 65534, 64534 | Ja  |
| 5    | 27     | 40      | 32               | 30                   | -10              | 32, 30, -10         | Nej |
| 6    | 33     | 0       | Ogiltigt         | Ogiltigt             | Ogiltigt         | Felaktigt resultat  | Nej |
Test 3:
Ett /30-nät passar mellan två routrar eftersom det ger två användbara IP-adresser, en till varje router.

Test 5:
Resultatet visar att det finns 40 enheter men bara 30 användbara IP-adresser. Driftavdelningen behöver utöka nätverket eller dela upp det i flera subnät.

Test 6:
Programmet kontrollerar inte om prefixlängden är giltig. Därför kan det räkna ut ett felaktigt resultat. Programmet borde godta prefixlängder mellan /0 och /32 för IPv4.

## Del 4: Från källkod till körning
Uppgift A
Var på datorn ligger filen?
C:\programmering\lab1\problem3.py

Vad händer med filen när du stänger av datorn? Varför?
För mig så öppnas filen när jag startar vs code. Detta är så att man kan börja jobba med vs code utan att behöva öppna det manuelt.

Uppgift B
Skriv av sökvägen till tolken.

& C:\Users\Liaml\AppData\Local\Python\pythoncore-3.14-64\python.exe

Kör python --version (Mac: python3 --version) i terminalen. Vilken version kör ditt program?

Python 3.14.8

Förklara med egna ord: vad gör tolken med din källkod?

Tolken läser källkoden och kör instruktionerna så att datorn kan utföra det som programmet ska göra.

Uppgift C

Hur mycket minne (RAM) använder processen? Skriv av värdet.

3.6 mb

Vem har startat processen och gett den minne?

Operativsystemet startar processen och ger den minne så att programmet kan köras.

Svara nu på programmets frågor så att det avslutas. Vad händer med processen i Aktivitetshanteraren? Vad händer med variablerna i ditt program?

Processen avslutas. Variablerna visas forfarande i terminalen men dem är inte sparade i datorn.

Uppgift D

När jag klickar på start läser tolken min källkod och kontrollerar den. Python kan omvandla koden till bytekod som tolken sedan kör. Operativsystemet startar en process och ger den arbetsminne. Processorn utför instruktionerna när programmet körs. Programmet bearbetar informationen och skickar resultatet till skärmen. Till sist ser jag resultatet i terminalen i VS Code.
