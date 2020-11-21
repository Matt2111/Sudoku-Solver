from os import system
from time import sleep
from json import loads

def Clear():
    system("cls")

def DrawBoard(board):
    for x in range(9):
        row = str()
        if not x % 3 and x:
            print("□□□□□□□□□□□□□□□□□□□□□□□")
        for y in range(9):
            if not y % 3 and y:
                row += f"□□ {board[x][y]} "
            else:
                row += f"{board[x][y]} "
        print(row)

def CheckDuplicates(board, point):
    x, y = point
    value = board[x][y]
    spaces = list()
    gridX = x // 3
    gridY = y // 3
    for xSpare in range(3):
        for ySpare in range(3):
            if xSpare != x - (gridX*3) and ySpare != y - (gridY*3):
                spaces.append(board[(3*gridX) + xSpare][(3 * gridY) + ySpare])
    for i in range(9):
        if i != x:
            spaces.append(board[i][y])
        if i != y:
            spaces.append(board[x][i])
    if value in spaces:
        return True
    return False

def Main():
    lastTried = [[list() for y in range(9)] for x in range(9)]
    board = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "]]
    # board = [[" " for y in range(9)] for x in range(9)]
    saved = False
    if input("Have you got a board saved(y/n): ").lower() == "y":
        saved = True
        fileName = input("Type the file name: ")
        with open(fileName, "r") as file:
            board = loads(file.read())
    y = 0
    while y < 9 and not saved:
        x = 0
        while x < 9:
            board[x][y] = "!"
            Clear(); DrawBoard(board)
            choice = input("Type a number 1-9, back to go back a step, exit to solve the puzzle, anything else will set it to clear: ")
            if choice in [str(_) for _ in list(range(1, 10))]:
                board[x][y] = int(choice)
                x += 1
            elif choice == "back":
                if x:
                    board[x][y] = " "
                    x -= 1
                elif y:
                    board[x][y] = " "
                    y -= 1
            elif choice == "exit":
                board[x][y] = " "
                y = 10
                break
            else:
                board[x][y] = " "
                x += 1
        y += 1
        if y == 9:
            y = 0

    solvableSpaces = list()
    for x in range(9):
        for y in range(9):
            if board[x][y] == " ":
                solvableSpaces.append([x, y])
    current = 0
    last = 0
    continuous = 0
    while True:
        if last == current:
            continuous += 1
        elif last != current:
            continuous = 0
        if continuous > 10:
            if current:
                current -= 1
            board[x][y] = " "
            lastTried[x][y] = list()
            continuous = 0
        last = current
        x, y = solvableSpaces[current]
        if board[x][y] == " ":
            board[x][y] = 1
        else:
            if int(board[x][y]) < 9:
                board[x][y] = int(board[x][y]) + 1
            else:
                board[x][y] = 1
        if not CheckDuplicates(board, solvableSpaces[current]) and board[x][y] not in lastTried[x][y]:
            current += 1
            lastTried[x][y].append(board[x][y])
            if current >= len(solvableSpaces):
                break
            continue
    Clear()
    DrawBoard(board)
    input()
if __name__ == '__main__':
    Main()
