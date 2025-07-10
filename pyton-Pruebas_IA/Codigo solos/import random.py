import itertools

def tiempo_total(cruces):
    tiempo = 0
    lado = [0, 0, 0, 0, 0]  # Inicialmente, todos en el lado 0
    for cruzadores in cruces:
        for cruzador in cruzadores:
            lado[cruzador] = 1 - lado[cruzador]  # Cambiar de lado
        tiempo += max(tiempo_balsa(cruzadores))
    return tiempo

def tiempo_balsa(cruzadores):
    tiempos = [1, 3, 6, 8, 12]  # Tiempos de cruzar para P, D, M, H, S
    return [tiempos[i] for i in cruzadores]

def encuentra_secuencia_optima():
    personas = [0, 1, 2, 3, 4]  # Índices de las personas (P, D, M, H, S)
    mejores_cruces = None
    mejor_tiempo = float('inf')

    # Genera todas las permutaciones posibles de cruzadores
    for cruzadores in itertools.permutations(personas):
        for i in range(1, len(cruzadores) + 1):
            subsecuencia = cruzadores[:i]
            if 0 not in subsecuencia:  # Asegura que el policía esté en la balsa
                continue
            tiempo = tiempo_total(subsecuencia)
            if tiempo < mejor_tiempo:
                mejor_tiempo = tiempo
                mejores_cruces = subsecuencia

    return mejores_cruces

secuencia_optima = encuentra_secuencia_optima()
for i, cruzador in enumerate(secuencia_optima):
    print(f"Pasa {cruzador} en {tiempo_balsa([cruzador])[0]} min")