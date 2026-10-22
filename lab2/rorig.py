# Samlar gränsvärdet på ett ställe så att det enkelt kan ändras.
GRANS = 300


def rakna_summa(svarstider_ms):
    totalt = 0

    for svarstid_ms in svarstider_ms:
        totalt = totalt + svarstid_ms

    return totalt


def rakna_over_grans(svarstider_ms):
    antalet_over_grans = 0

    for svarstid_ms in svarstider_ms:
        if svarstid_ms > GRANS:
            antalet_over_grans = antalet_over_grans + 1

    return antalet_over_grans


svarstider_ms=[120,95,310,80,450]

# Funktionerna delar upp beräkningarna så att koden blir lättare att återanvända.
totalt = rakna_summa(svarstider_ms)
antalet_over_grans = rakna_over_grans(svarstider_ms)

print("Total:", totalt)
print("Genomsnitt:", totalt / len(svarstider_ms))
print("Antal över gränsen:", antalet_over_grans)