board = [[1,0,1,0,0,0],
         [1,1,0,1,0,1],
         [0,1,0,0,0,0],
         [0,0,0,0,0,1],
         [1,0,1,1,0,0],
         [0,0,1,0,0,1],
         [1,1,0,0,0,1]]

def print_board(board):
    for row in board:
        for i in range(0, len(row)):
            print(row[i], end=" ")
        print("")

def make_a_move(cell1, cell2):
    value_anterior = board[int(cell1[0])][int(cell1[1])]
    board[int(cell1[0])][int(cell1[1])] = board[int(cell2[0])][int(cell2[1])]
    board[int(cell2[0])][int(cell2[1])] = value_anterior

def check_the_board(cell):
    row = board[cell[0]]
    left = cell[1] - 1
    right = cell[1] + 1
    matches = []
    matches.append(cell[1])
    while left >= 0 and right < len(row):
        if row[left] == 1 and row[cell[1]] == 1 and row[right] == 1:
            matches.append(left)
            matches.append(right)
        elif row[left] != 1 and row[cell[1]] == 1 and row[right] == 1:
            matches.append(right)

instructions = "You can move a cell only to adjacent cells, if the movement result in 3 adjacents cells containing the numbe 1 those will turn to zero's"

print_board(board)
print(instructions)
value1 = input("column to move: ")
value2 = input("to column: ")
print(f'Columns to move are {value1} to the column {value2}')
cell1 = [value1[:1],value1[2:]]
cell2 = [value2[:1],value2[2:]]
print(f'cell1 {cell1} cell2 {cell2}')
make_a_move(cell1, cell2)
print_board(board)
check_the_board(cell2)

