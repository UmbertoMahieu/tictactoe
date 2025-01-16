def print_board(boardgame):
    for x in range(len(boardgame)):
        display_row = ""
        for n in range(len(boardgame[x])):
            if boardgame[x][n] == 1:
                display_row += " ".join(" O ")
            elif boardgame[x][n] == 2 :
                display_row += " ".join(" X ")
            else :
                display_row += " ".join("   ")
            if n != len(boardgame) -1:
                display_row += " ".join(" | ")
        print(display_row)
        if x != len(boardgame) -1:
            print("--------------------------")


def ask_pos():
    try:
        pos = input("Send row number and case number to add your sign. eg: 1,2 for first row, second case : ")
        position = tuple(map(int, pos.split(',')))
        row,col = position[0] - 1, position[1] - 1
        if row not in range(3) or col not in range(3):
            print("Case doesn't exist, try another one")
            return ask_pos()
        if boardgame[row][col] != 0 :
            print("Case already taken, try another one")
            return ask_pos()

        else:
            return row,col
    except (ValueError, IndexError):
        print("Wrong input!")
        return ask_pos()



def turn(player):
    print(f"--- Player {player} turn ---")
    row,col = ask_pos()
    boardgame[row][col] = player
    print_board(boardgame)

def check_win():
    if boardgame[0][0] != 0 and boardgame[0][0] == boardgame[0][1] and boardgame[0][1] == boardgame[0][2]:
        return check_winner(boardgame[0][0])
    elif boardgame[1][0] != 0 and boardgame[1][0] == boardgame[1][1] and boardgame[1][1] == boardgame[1][2]:
        return check_winner(boardgame[0][0])
    elif boardgame[2][0] != 0 and boardgame[2][0] == boardgame[2][1] and boardgame[2][1] == boardgame[2][2]:
        return check_winner(boardgame[0][0])
    elif boardgame[0][0] != 0 and boardgame[0][0] == boardgame[1][0] and boardgame[1][0] == boardgame[2][0]:
        return check_winner(boardgame[0][0])
    elif boardgame[0][1] != 0 and boardgame[0][1] == boardgame[1][1] and boardgame[1][1] == boardgame[2][1]:
        return check_winner(boardgame[0][1])
    elif boardgame[0][2] != 0 and boardgame[0][2] == boardgame[1][2] and boardgame[1][2] == boardgame[2][2]:
        return check_winner(boardgame[0][2])
    elif boardgame[0][0] != 0 and boardgame[0][0] == boardgame[1][1] and boardgame[1][1] == boardgame[2][2]:
        return check_winner(boardgame[0][0])
    elif boardgame[0][2] != 0 and boardgame[0][2] == boardgame[1][1] and boardgame[1][1] == boardgame[2][0]:
        return check_winner(boardgame[0][2])
    else:
        return False

def check_winner(result):
    if result == 1:
        print("player 1 win !")
    if result == 2:
        print("player 2 win !")
    return True


boardgame = [[0,0,0],[0,0,0],[0,0,0]]
player1 = 1
player2 = 2

print_board(boardgame)

while True:
    turn(player1)
    if check_win():
        break
    turn(player2)
    if check_win():
        break


