storlek = float(input("Ange filens storlek i gigabyte: "))
bandbredd = float(input("Ange nätverkets bandbredd i megabit per sekund: "))
anvandBandbredd = float(input("Ange den använda bandbredden i %:" ))

tidSek = (storlek * 1000 * 8) / bandbredd
riktigTid = tidSek / (anvandBandbredd / 100)
tidMin = riktigTid / 60


tidSek = round(tidSek, 1)
tidMin = round(tidMin, 2)
riktigTid = round(riktigTid, 1)


print("Överföringstid i sekunder:", riktigTid) 
print("Överföringstid i minuter:", tidMin)