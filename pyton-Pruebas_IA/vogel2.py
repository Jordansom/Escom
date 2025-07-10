def vogel_approximation_method(supply, demand, costs):
    num_rows = len(supply)
    num_cols = len(demand)

    # Calcular las penalizaciones de Vogel
    row_penalty = [0] * num_rows
    col_penalty = [0] * num_cols

    for i in range(num_rows):
        row = costs[i]
        row.sort()
        row_penalty[i] = abs(row[1] - row[0])

    for j in range(num_cols):
        col = [costs[i][j] for i in range(num_rows)]
        col.sort()
        col_penalty[j] = abs(col[1] - col[0])

    # Inicializar variables
    total_cost = 0
    allocations = [[0] * num_cols for _ in range(num_rows)]

    # Iterar hasta que todos los suministros y demandas se cumplan
    while sum(supply) > 0 and sum(demand) > 0:
        max_penalty_row = row_penalty.index(max(row_penalty))
        max_penalty_col = col_penalty.index(max(col_penalty))

        if supply[max_penalty_row] < demand[max_penalty_col]:
            allocation = supply[max_penalty_row]
        else:
            allocation = demand[max_penalty_col]

        # Asignar la asignación y actualizar suministros y demandas
        allocations[max_penalty_row][max_penalty_col] = allocation
        supply[max_penalty_row] -= allocation
        demand[max_penalty_col] -= allocation

        # Actualizar penalizaciones
        row_penalty[max_penalty_row] = float('inf')
        col_penalty[max_penalty_col] = float('inf')

        for i in range(num_rows):
            if supply[i] > 0:
                row_penalty[i] = abs(min(costs[i]) - max(costs[i]))

        for j in range(num_cols):
            if demand[j] > 0:
                col_vals = [costs[i][j] for i in range(num_rows) if supply[i] > 0]
                if col_vals:
                    col_penalty[j] = abs(min(col_vals) - max(col_vals))

        # Actualizar el costo total
        total_cost += allocation * costs[max_penalty_row][max_penalty_col]

    return total_cost, allocations

# Ejemplo de uso
supply = [20, 30, 50]
demand = [30, 40, 30]
costs = [
    [6, 8, 10],
    [9, 7, 4],
    [3, 2, 8]
]

total_cost, allocations = vogel_approximation_method(supply, demand, costs)

print(f"Costo total mínimo: {total_cost}")
print("Asignaciones:")
for row in allocations:
    print(row)

