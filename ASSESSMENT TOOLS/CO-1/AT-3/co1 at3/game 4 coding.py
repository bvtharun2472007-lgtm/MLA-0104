ROWS = 6
COLS = 7

board = [[" "]*COLS for _ in range(ROWS)]

def display():
    for row in board:
        print("|".join(row))
    print("-"*13)

def drop(col,player):
    for r in range(ROWS-1,-1,-1):
        if board[r][col]==" ":
            board[r][col]=player
            return True
    return False

display()

drop(3,"X")
drop(2,"O")
drop(3,"X")
drop(4,"O")
drop(3,"X")

display()
