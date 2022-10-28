import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_board():
    global row1; global row2; global row3
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]

def input_move(player):
    while True:
        invalid_input = "\n Select valid position."
        indexOffset = [0, 3, 6]
        try:
            inputPos = int(input(f"\n Player: {player}\n\n 1-9: ")) - 1
        except ValueError:
            print(invalid_input); continue
        for row, num in zip([row1, row2, row3], indexOffset):
            if inputPos <= num + 2:
                if row[inputPos-(num)] == " ":
                    row[inputPos-(num)] = player
                    return
                print(invalid_input)
                break
        print("\nPosition has to be less then 10.")
        
def print_board():
    clear_console()
    line = " ----------"
    print("\n"+line)
    for row in (row1, row2, row3):
        print(f" |{row[0]} |{row[1]} |{row[2]} |")
        print(line)

def check_board_row():
    for row in (row1, row2, row3):
        if all(tile == row[0] for tile in row) and row[0] != " ":
            print_board()
            print(f"\n {row[0]} won!\n")
            done()

def check_board_col():
    atPos = 0
    for i in range(1, 3):
        if row1[atPos] == row2[atPos] == row3[atPos] == row1[atPos] != " ":
            print_board()
            print(f"\n {row1[atPos]} won!\n")
            done()
        atPos += 1

def check_board_diag():
    if row1[0] == row2[1] == row3[2] and row1[0] != " ":
        print_board()
        print(f"\n {row1[0]} won!\n")
        done()
    if row1[2] == row2[1] == row3[0] and row1[2] != " ":
        print_board()
        print(f"\n {row1[2]} won!\n")
        done()
        
def check_draw():
    for tile in (row1 + row2 + row3):
        if tile == " ": return
    print(" Draw!\n")
    done()

def check_board():
    check_board_row(); check_board_col(); check_board_diag(); check_draw()

def play():
    clear_board()
    while True:
        print_board()
        input_move("X")
        print_board()
        check_board()
        input_move("O")
        check_board()

def done():
    answer = input(" Play again or exit? (p/e): ")[0].lower()
    if answer == "e": exit()
    if answer == "p": play()

if __name__ == '__main__': play()
