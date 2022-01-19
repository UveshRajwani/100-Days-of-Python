game_over = False
rows = [
    {"1": '', "2": '', "3": ''},
    {"1": '', "2": '', "3": ''},
    {"1": '', "2": '', "3": ''}
]


def print_game():
    print(f" {rows[0].get('1')} | {rows[0].get('2')} | {rows[0].get('3')}\n"
          "---------\n"
          f" {rows[1].get('1')} | {rows[1].get('2')} | {rows[1].get('3')}\n"
          "---------\n"
          f" {rows[2].get('1')} | {rows[2].get('2')} | {rows[2].get('3')}\n")


def checker():
    global game_over
    board = []
    for n in range(0, 3):
        if rows[n].get("1") == rows[n].get("2") and rows[n].get("2") == rows[n].get("3"):
            if rows[n].get('1') == 'X' or rows[n].get('1') == 'O':
                print(f'{rows[n].get("1")} Won 1')
                game_over = True
                break
    for c in range(1, 4):
        c = str(c)
        if rows[0].get(c) == rows[1].get(c) and rows[1].get(c) == rows[2].get(c):
            if rows[0].get(c) == 'X' or rows[0].get(c) == 'O':
                print(f'{rows[0].get(c)} Won 2 ')
                game_over = True
                break
    if rows[0].get("1") == rows[1].get("2") == rows[2].get("3"):
        if rows[0].get('1') == 'X' or rows[0].get('1') == 'O':
            print(f'{rows[0].get("1")} Won 3')
            game_over = True
    if rows[0].get("3") == rows[1].get("2") == rows[2].get("1"):
        if rows[0].get('3') == 'X' or rows[0].get('3') == 'O':
            print(f'{rows[0].get("3")} Won ')
            game_over = True
    for n in range(0,3):
        for key, value in rows[n].items():
            board.append(value)
    if '' in board or None in board:
        pass
    else:
        print(f'kal this is a draw')
        game_over = True
print_game()
while not game_over:
    row = int(input("pls enter the row number "))
    row -= 1
    col = int(input("pls enter the col number "))
    ans = input("pls enter the input (only : X or O) ").upper()
    if ans == "X" or ans == "O":
        if row > 2:
            print("Max number of row can be 3")
        if col > 3 or col <= 0:
            print("Max number of col can be 3")
        rows[row][str(col)] = ans
    else:
        print("Pls enter X or O")
    print_game()
    checker()
