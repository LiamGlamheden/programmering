platskod = input("Ange platskod: ")
enhetstyp = input("Ange enhetstyp: ")
senasteNumret = input("Ange senasteNumret: ")
foretagDoman = input("Ange företagets domän: ")

nästaNummer = int(senasteNumret) + 1

platskod = platskod.lower()
enhetstyp = enhetstyp.lower()

nästaNummer = str(nästaNummer).zfill(2)

hostnamn = platskod + "-" + enhetstyp + "-" + nästaNummer + "." + foretagDoman

print("Nästa hostnamn:", hostnamn)