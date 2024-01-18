coor_x = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
}

coor_y = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
}

def_field = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

def convert_to_indices(string):
    coordinates = [char for char in string]
    x = coor_x[coordinates[0]]
    y = coor_y[coordinates[1]]
    return [y,x]

def convert_user_input(ui_dict):
    user_matrix = def_field.copy()
    coor_user_input = []
    for i in range(len(ui_dict)):
        coor = convert_to_indices(ui_dict[i])
        coor_user_input.append(coor)
    for coor in coor_user_input:
        user_matrix[coor[0]][coor[1]] = 1
    return coor_user_input, user_matrix


user_input = ['a1', 'b3', 'c4', 'd2', 'c5']


res = convert_user_input(user_input)

print(res[0], '\n\n')
for i in res[1]:
    print(i)