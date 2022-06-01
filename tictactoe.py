import os


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_move(player):
    while True:
        invalid_input = "\nSelect valid position."
        try:
            inputPos = int(input(f"\n({player}) 1-9: ")) - 1
        except ValueError:
            print(invalid_input)
            continue
        if inputPos <= 2:
            if row1[inputPos] == " ":
                row1[inputPos] = player
                break
            print(invalid_input)
        elif inputPos <= 5:
            if row2[inputPos-3] == " ":
                row2[inputPos-3] = player
                break
            print(invalid_input)
        elif inputPos <= 8:
            if row3[inputPos-6] == " ":
                row3[inputPos-6] = player
                break
            print(invalid_input)
        else:
            print("Position has to be less then 10.")

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
            print(f"{row[0]} won!\n")
            done()

def check_board_col():
    atPos = 0
    for i in range(1, 3):
        if row1[atPos] == row2[atPos] == row3[atPos] == row1[atPos] != " ":
            print_board()
            print(f"{row1[atPos]} won!\n")
            done()
        atPos += 1

def check_board_diag():
    if row1[0] == row2[1] == row3[2] and row1[0] != " ":
        print(f"{row1[0]} won!\n")
        done()
    if row1[2] == row2[1] == row3[0] and row1[2] != " ":
        print_board()
        print(f"{row1[2]} won!\n")
        done()
        
def check_draw():
    for tile in (row1 + row2 + row3):
        if tile == " ":
            return
    print("Draw!\n")
    done()

def check_board():
    check_board_row()
    check_board_col()
    check_board_diag()
    check_draw()

def play():
    while True:
        print_board()
        input_move("X")
        print_board()
        check_board()
        input_move("O")
        check_board()

def done():
    answer = input("Play again or exit? (p/e): ")[0].lower()
    if answer == "e":exit()
    if answer == "p":play()

if __name__ == '__main__':
    play()
