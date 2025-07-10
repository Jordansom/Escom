# Laberinto con algortimo A*
#Ávila Juárez Alexis Aramis
#Jurado Santos Alberto Isaac
#Gutierrez Espinosa Jordan Gabriel
#Pérez Ortiz Saúl
#Ramírez Juárez Arturo Yamil
import heapq

class Nodo:
    def __init__(puest, x, y, costo, padre):
        puest.x = x
        puest.y = y
        puest.costo = costo
        puest.padre = padre

    def __lt__(puest, otro):
        return puest.costo < otro.costo

def a_estrella(maze, comienzo, end):
    fila, columna = len(maze), len(maze[0])
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cola_prioridad = []
    heapq.heappush(cola_prioridad, Nodo(comienzo[0], comienzo[1], 0, None))
    visitados = set()

    while cola_prioridad:
        nodo_actual = heapq.heappop(cola_prioridad)

        if (nodo_actual.x, nodo_actual.y) == end:
            camino = []
            while nodo_actual:
                camino.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return list(reversed(camino))

        if (nodo_actual.x, nodo_actual.y) in visitados:
            continue

        visitados.add((nodo_actual.x, nodo_actual.y))

        for dx, dy in movimientos:
            nx, ny = nodo_actual.x + dx, nodo_actual.y + dy
            if 0 <= nx < fila and 0 <= ny < columna and maze[nx][ny] != 1:
                nuevo_costo = nodo_actual.costo + 1
                heapq.heappush(cola_prioridad, Nodo(nx, ny, nuevo_costo, nodo_actual))

    return None

# 0: camino, 1: pared
laberinto = [
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

comienzo = (0, 0)
end = (19, 19)

solucion = a_estrella(laberinto, comienzo, end)

if solucion:
    for fila in range(len(laberinto)):
        for columna in range(len(laberinto[0])):
            if (fila, columna) in solucion:
                print("S", end=" ")
            elif laberinto[fila][columna] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No se encontró solución.")

