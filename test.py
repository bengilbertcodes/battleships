coor_x = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}

coor_y = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
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


def valid_coordinates():
    """
    List of valid coordinates to check against user input. 
    Ensuring only correct values can be entered
    """
    list_of_coordinates = []
    
    for i in range(8):
        for j in range(8):
            square = chr(ord('a') + j) + str(i + 1)
            list_of_coordinates.append(square)
    return list_of_coordinates
    
list_of_coordinates = valid_coordinates()


# Creates a list of coordinates.
# Code based on https://stackoverflow.com/questions/18817207/use-python-to-create-2d-coordinate
# def coordinates():
#     tuple_coordinates_list = []

#     for x in range(BOARD_SIZE):
#         for y in range(1, 9):
#             tuple_coordinates_list.append((x, y))

#     return tuple_coordinates_list

# tuple_coordinates_list = coordinates()
