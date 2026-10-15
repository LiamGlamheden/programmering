prefix = int(input("Ange prefixlängd: ")) 
enheter = int(input("Ange antal befintliga enheter: ")) 

hostbitar = 32 - prefix 
totalt = 2 ** hostbitar 
anvandbara = totalt - 2 
lediga = anvandbara - enheter 

print("Totalt antal adresser:", totalt) 
print("Användbara adresser:", anvandbara) 
print("Lediga adresser:", lediga)