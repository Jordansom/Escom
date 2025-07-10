import random

def inicializar_tablero():
    return [[' ' for _ in range(4)] for _ in range(4)]

def mostrar_tablero(tablero):
    print("   A  B  C  D")
    print(" -------------")
    for i in range(4):
        print(i + 1, "|", end="")
        for j in range(4):
            print(tablero[i][j], "|", end="")
        print("\n -------------")

def verificar_ganador(tablero, jugador):
    # Verificar filas y columnas
    for i in range(4):
        if all(tablero[i][j] == jugador for j in range(4)):
            return True
        if all(tablero[j][i] == jugador for j in range(4)):
            return True

    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(4)) or all(tablero[i][3 - i] == jugador for i in range(4)):
        return True

    return False

def tablero_lleno(tablero):
    return all(cell != ' ' for row in tablero for cell in row)

def obtener_movimiento_computadora(tablero, jugador, profundidad):
    mejor_movimiento = None
    mejor_valor = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for i in range(4):
        for j in range(4):
            if tablero[i][j] == ' ':
                tablero[i][j] = jugador
                valor = minimax(tablero, profundidad, False, jugador, alpha, beta)
                tablero[i][j] = ' '

                if valor > mejor_valor:
                    mejor_movimiento = (i, j)
                    mejor_valor = valor

                alpha = max(alpha, valor)

    return mejor_movimiento

def minimax(tablero, profundidad, es_maximizador, jugador, alpha, beta):
    if profundidad == 0 or tablero_lleno(tablero) or verificar_ganador(tablero, jugador):
        if verificar_ganador(tablero, jugador):
            return 1
        elif verificar_ganador(tablero, 'X' if jugador == 'O' else 'O'):
            return -1
        else:
            return 0

    if es_maximizador:
        mejor_valor = float('-inf')
        for i in range(4):
            for j in range(4):
                if tablero[i][j] == ' ':
                    tablero[i][j] = jugador
                    valor = minimax(tablero, profundidad - 1, False, jugador, alpha, beta)
                    tablero[i][j] = ' '
                    mejor_valor = max(mejor_valor, valor)
                    alpha = max(alpha, mejor_valor)
                    if beta <= alpha:
                        break
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for i in range(4):
            for j in range(4):
                if tablero[i][j] == ' ':
                    tablero[i][j] = 'X' if jugador == 'O' else 'O'
                    valor = minimax(tablero, profundidad - 1, True, jugador, alpha, beta)
                    tablero[i][j] = ' '
                    mejor_valor = min(mejor_valor, valor)
                    beta = min(beta, mejor_valor)
                    if beta <= alpha:
                        break
        return mejor_valor

def jugar():
    tablero = inicializar_tablero()
    jugador = 'X'
    nivel = input("Selecciona el nivel (facil/medio/dificil): ")

    profundidad = 0  # Profundidad por defecto para el nivel fácil
    if nivel == 'medio':
        profundidad = 2
    elif nivel == 'dificil':
        profundidad = 4

    while True:
        mostrar_tablero(tablero)

        if jugador == 'X':
            fila, columna = input("Ingresa tu movimiento (fila columna, ej. 2 A): ").split()
            fila = int(fila) - 1
            columna = ord(columna.upper()) - ord('A')
            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = jugador
            else:
                print("Movimiento inválido. Inténtalo de nuevo.")
                continue
        else:
            print(f"Turno de la computadora ({nivel})")
            movimiento_computadora = obtener_movimiento_computadora(tablero, jugador, profundidad)
            tablero[movimiento_computadora[0]][movimiento_computadora[1]] = jugador

        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡{jugador} ha ganado!")
            break
        elif tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador = 'X' if jugador == 'O' else 'O'

if __name__ == "__main__":
    jugar()