portar = [8000, 8001]

for i in range(len(servrar)):
    if port_svarar(servrar[i], portar[i]):
        print(f"{servrar[i]} svarar på port {portar[i]}.")
    else:
        print(f"{servrar[i]} svarar inte på port {portar[i]}.")