misslyckade_forsok = [0, 2, 1, 7, 0, 12, 3, 0]

def summa_forsok(lista):
    summa = 0

    for antal_forsok in lista:
        summa = summa + antal_forsok

    return summa

def medel_forsok(lista):
    medel_varde = summa_forsok(lista) / len(lista)

    return medel_varde


def storsta(lista):
    storsta_varde = lista[0]

    for tal in lista:
        if tal > storsta_varde:
            storsta_varde = tal

    return storsta_varde


def antal_minst(lista, grans):
    antal = 0

    for tal in lista:
        if tal >= grans:
            antal += 1

    return antal






print(summa_forsok(misslyckade_forsok))
print(medel_forsok(misslyckade_forsok))
print(storsta(misslyckade_forsok))
print(antal_minst(misslyckade_forsok, 5))


