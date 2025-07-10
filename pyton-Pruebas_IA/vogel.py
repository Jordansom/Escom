from problemas.generico import *

resultado = []


def reset_resultado():
    columna = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            columna.append(0)
        resultado.append(columna.copy())
        columna.clear()


def sum_without_none(iteraccion ):
    resultado = 0
    for numero in iteraccion :
        if numero is not None:
            resultado += numero
    return resultado


def insert_artificial_origin():
    originen.append('dummy')
    linea = []
    for i in range(0, len(destino)):
        linea.append(0)
    matrix.append(linea)
    oferta.append(sum(demanda) - sum(oferta))


def insert_artificial_destination():
    destination.append('dummy')
    for linea in matrix:
        linea.append(999)
    demanda.append(sum(oferta) - sum(demanda))


def calculo_penalisacion():
    origin_penalty = []
    destino_penalisacion = []
    columna = []

    for i, linea in enumerate(matrix):
        origin_penalty.append(differencia_lower_cost(iterable_without_none(linea.copy(), demanda)))

    for j in range(0, len(matrix[0])):
        for k in range(0, len(matrix)):
            columna.append(matrix[k][j])
        destino_penalisacion.append(differencia_lower_cost(iterable_without_none(columna, oferta)))
        columna.clear()

    return [origin_penalty, destino_penalisacion]


def differencia_lower_cost(iteraccion ):

    best = min(iteraccion )
    iteraccion .remove(best)

    if len(iteraccion ) == 0:
        return best

    alternative = min(iteraccion )

    return abs(alternative - best)


def get_columna(index):
    columna = []
    for j in range(0, len(matrix)):
        columna.append(matrix[j][index])
    return columna


def iterable_without_none(iteraccion , comparable=None):
    iterable_remove_none = []
    for i, x in enumerate(iteraccion ):
        if comparable is not None:
            if comparable[i] is not None:
                iterable_remove_none.append(x)
        else:
            if iteraccion [i] is not None:
                iterable_remove_none.append(x)
    return iterable_remove_none


def find_lower_cell(origin_penalty, destino_penalisacion):
    resultado = []

    max_difference_origin = max(origin_penalty)
    max_difference_destination = max(destino_penalisacion)

    if max_difference_origin < max_difference_destination:
        index_max_differencia = destino_penalisacion.index(max_difference_destination)
        resultado.append(index_max_differencia)
        columna = get_columna(index_max_differencia)
        lower_cost_value = min(iterable_without_none(columna, oferta))
        resultado.append(lower_cost_value)
        resultado.append(columna.index(lower_cost_value))
    else:
        index_max_differencia = origin_penalty.index(max_difference_origin)
        resultado.append(index_max_differencia)
        linea = matrix[index_max_differencia]
        lower_cost_value = min(iterable_without_none(linea, demanda))
        resultado.append(lower_cost_value)
        resultado.append(linea.index(lower_cost_value))
        resultado.reverse()

    return resultado


def calculate_result():
    z = 0
    for i in range(0, len(resultado)):
        for j in range(0, len(resultado[0])):
            z += resultado[i][j]
    return z


def main():
    if sum(demanda) > sum(oferta):
        insert_artificial_origin()
    elif sum(oferta) > sum(demanda):
        insert_artificial_destination()

    reset_resultado()

    while (sum_without_none(oferta) + sum_without_none(demanda)) != 0:

        origin_penalty, destino_penalisacion = calculo_penalisacion()
        index_columna_demanda, lower_cost_value, index_linea_oferta = find_lower_cell(origin_penalty, destino_penalisacion)

        value_oferta = oferta[index_linea_oferta]
        value_demanda = demanda[index_columna_demanda]

        if value_demanda < value_oferta:
            resultado[index_linea_oferta][index_columna_demanda] = lower_cost_value * value_demanda
            for i in range(0, len(matrix)):
                matrix[i][index_columna_demanda] = 0
            demanda[index_columna_demanda] = None
            oferta[index_linea_oferta] -= value_demanda
        else:
            resultado[index_linea_oferta][index_columna_demanda] = lower_cost_value * value_oferta
            for i in range(0, len(matrix[0])):
                matrix[index_linea_oferta][i] = 0
            oferta[index_linea_oferta] = None
            demanda[index_columna_demanda] -= value_oferta


main()
print("la matriz resultado es\n:")
print(resultado)
print("\nY la cantidad de tranporte es:")
print(calculate_result())
