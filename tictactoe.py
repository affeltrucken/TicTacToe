import os


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_move(player):
    while True:
        inputPos = int(input(f"\n({player}) 1-9: ")) - 1
        if inputPos <= 2:
            if row1[inputPos] == " ":
                row1[inputPos] = player
                break
            print("\nSelect valid position.")
        elif inputPos <= 5:
            if row2[inputPos-3] == " ":
                row2[inputPos-3] = player
                break
            print("Select valid position.")
        elif inputPos <= 8:
            if row3[inputPos-6] == " ":
                row3[inputPos-6] = player
                break
            print("Select valid position.")
        else:
            print("Position has to be less then 10.")

def print_board():
    clear_console()
    print("\n -------")
    for row in (row1, row2, row3):
        print(f" |{row[0]}|{row[1]}|{row[2]}|")
        print(" -------")

def check_board_row():
    for row in (row1, row2, row3):
        if all(tile == row[0] for tile in row) and row[0] != " ":
            print_board()            
            print(f"{row[0]} won!")
            exit()

def check_board_col():
    atPos = 0
    for i in range(1, 3):
        if row1[atPos] == row2[atPos] == row3[atPos] == row1[atPos] != " ":
            print_board()
            print(f"{row1[atPos]} won!")
            exit()
        atPos += 1

def check_board_diag():
    if row1[0] == row2[1] == row3[2] and row1[0] != " ":
        print(f"{row1[0]} won!")
        exit()
    if row1[2] == row2[1] == row3[0] and row1[2] != " ":
        print_board()
        print(f"{row1[2]} won!")
        exit()

def check_board():
    check_board_row()
    check_board_col()
    check_board_diag()

def play():
    while True:
        print_board()
        input_move("X")
        print_board()
        check_board()
        input_move("O")
        check_board()


if __name__ == '__main__':
    play()