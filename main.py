matrice = [[1, 2, 1, -2, 2],
           [2, 0, -1, 1, 2],
           [0, 2, 1, -1, 2],
           [1, 2, -1, 0, 2]]

matrice_line_size = len(matrice[0])

columns_to_zero = len(matrice[0]) - 2

print('Temos a Matriz:\n')

for x in matrice:
    print(x)

print('\n#######>Tratativas da Matriz<#######')

for cur_column in range(columns_to_zero):
    pivot_line = cur_column

    print(f'\n>>>Zerando a coluna {cur_column}<<<')

    line_interaction = len(matrice) - (pivot_line + 1)

    interaction_line = pivot_line

    for cur_interaction in range(line_interaction):
        interaction_line += 1
        upper_line = matrice[pivot_line]
        target_line = matrice[interaction_line]

        multiplier_a = upper_line[pivot_line]
        multiplier_b = target_line[pivot_line]

        if not multiplier_b == 0:

            matrice[pivot_line] = [x * multiplier_b for x in upper_line]

            matrice[interaction_line] = [x * multiplier_a for x in target_line]

            for index in range(matrice_line_size):
                matrice[interaction_line][index] = matrice[interaction_line][index] - matrice[pivot_line][index]

        print(f'\n=Interação {cur_interaction + 1}=\n')

        print(f'Para zerar a posição => coluna: {cur_column} linha: {interaction_line} temos que:')

        print(f'-Multiplicar a linha {pivot_line} por {multiplier_b}')

        print(f'-Multiplicar a linha {interaction_line} por {multiplier_a}')

        print(f'-Subtrair a linha {pivot_line} da {interaction_line}')

        print('Após Essa iteração temos a matriz:')

        for x in matrice:
            print(x)


print('\n#######>Aplicando Algebra<#######\n')

print('Para achar o W temos a função:')

print(f'{matrice[-1][matrice_line_size - 2]} * W = {matrice[-1][matrice_line_size - 1]}')

w = matrice[-1][matrice_line_size - 1] / matrice[-1][matrice_line_size - 2]

print(f'Temos que W = {w}\n')

print('Para achar o Z temos a função:')

print(f'{matrice[2][matrice_line_size - 3]} * Z + ({(matrice[2][matrice_line_size - 2] * w)}) = {matrice[2][matrice_line_size - 1]}')

z = (matrice[2][matrice_line_size - 1] - (matrice[2][matrice_line_size - 2] * w)) / matrice[2][matrice_line_size - 3]

print(f'Temos que Z = {z}\n')

print('Para achar o Y temos a função:')

print(f'{matrice[1][matrice_line_size - 4]} * Y + ({(matrice[1][matrice_line_size -3] * z)}) + ({(matrice[1][matrice_line_size - 2] * w)}) = {matrice[1][matrice_line_size - 1]}')

y = (matrice[1][matrice_line_size - 1] - (matrice[1][matrice_line_size - 2] * w) - (matrice[1][matrice_line_size -3] * z)) / matrice[1][matrice_line_size - 4]

print(f'Temos que Y = {y}\n')

print('Para achar o X temos a função:')

print(f'{matrice[0][matrice_line_size - 5]} * X + ({(matrice[0][matrice_line_size -4] * y)}) + ({(matrice[0][matrice_line_size -3] * z)}) + ({(matrice[0][matrice_line_size - 2] * w)}) = {matrice[0][matrice_line_size - 1]}')

x = (matrice[0][matrice_line_size - 1] - (matrice[0][matrice_line_size - 2] * w) - (matrice[0][matrice_line_size -3] * z) - (matrice[0][matrice_line_size -4] * y)) / matrice[0][matrice_line_size - 5]

print(f'Temos que X = {x}\n')


