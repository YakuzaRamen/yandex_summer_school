def exhibition(height: int, width: int, *args) -> None:
    matrix = []
    node = {'s_x_position': 0, 's_y_position': 0}
    need_visit = 0

    # Создаем матрицу
    for i in range(height):
        matrix_part = list(str(*args)[width * i: width * i + width])
        matrix.append(matrix_part)
        need_visit += matrix_part.count('.')
        # Проверка наличие входа в элементе матрицы
        if 'S' in matrix_part:
            node['s_x_position'] = matrix_part.index('S')
            node['s_y_position'] = i

    # ПУл нод
    next_position = [node]
    # Проверка 4 соседних клеток
    while need_visit > 0:

        if len(next_position) != 0:
            node = next_position.pop()
        else:
            break

            # Проверка верхней позиции и добавление в пул при мэтче
        if matrix[node['s_y_position'] - 1][node['s_x_position']] == '.':
            next_position.append({'s_y_position': node['s_y_position'] - 1, 's_x_position': node['s_x_position']})
            matrix[node['s_y_position'] - 1][node['s_x_position']] = 'U'
            need_visit -= 1
            # Проверка нижней позиции и добавление в пул при мэтче
        if matrix[node['s_y_position'] + 1][node['s_x_position']] == '.':
            next_position.append({'s_y_position': node['s_y_position'] + 1, 's_x_position': node['s_x_position']})
            matrix[node['s_y_position'] + 1][node['s_x_position']] = 'D'
            need_visit -= 1
            # Проверка правой позиции и добавление в пул при мэтче
        if matrix[node['s_y_position']][node['s_x_position'] + 1] == '.':
            next_position.append({'s_y_position': node['s_y_position'], 's_x_position': node['s_x_position'] + 1})
            matrix[node['s_y_position']][node['s_x_position'] + 1] = 'R'
            need_visit -= 1
            # Проверка левой позиции и добавление в пул при мэтче
        if matrix[node['s_y_position']][node['s_x_position'] - 1] == '.':
            next_position.append({'s_y_position': node['s_y_position'] , 's_x_position': node['s_x_position'] - 1})
            matrix[node['s_y_position']][node['s_x_position'] - 1] = 'L'
            need_visit -= 1
    for i in matrix:
        print(i)



exhibition(5, 8, '#########......##.#S#.####...###########')

"""
def check(node: dict, matrix: list, need_visit: int) -> list:


    while need_visit == 0:
        node = next_position.pop()
        if matrix[node['s_x_position'] - 1][node['s_y_position']] == '.':
            matrix[node['s_x_position'] - 1][node['s_y_position'] + 1] = 'U'
            next_position.append(matrix[node['s_x_position'] - 1][node['s_y_position'] + 1])
        if matrix[node['s_x_position'] + 1][node['s_y_position'] + 1] == '.':
            matrix[node['s_x_position'] + 1][node['s_y_position'] + 1] = 'D'
            next_position.append(matrix[node['s_x_position'] + 1][node['s_y_position'] + 1])
        if matrix[node['s_x_position']][node['s_y_position'] + 1] == '.':
            matrix[node['s_x_position']][node['s_y_position'] + 1] = 'R'
            next_position.append(matrix[node['s_x_position']][node['s_y_position'] + 1])
        if matrix[node['s_x_position'] - 1][node['s_y_position'] + 1] == '.':
            matrix[node['s_x_position'] - 1][node['s_y_position'] + 1] = 'L'
            next_position.append(matrix[node['s_x_position'] - 1][node['s_y_position'] + 1])
"""
"""
['#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', 'R', 'D', 'D', 'D', 'L', '#'],
['#', '.', '#', 'S', '#', 'L', '#', '#'],
['#', '#', 'R', 'U', 'L', '#', '#', '#'],
['#', '#', '#', '#', '#', '#', '#', '#']

"""
