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
            if n != 2:
                display_row += " ".join(" | ")
        print(display_row)
        if x != 2:
            print("--------------------------")


def ask_pos():
    pos = input("Send row number and case number to add your sign. eg: 1,2 for first row, second case : ")
    position = tuple(map(int, pos.split(',')))
    if boardgame[position[0]-1][position[1]-1] != 0:
        return ask_pos()
    else:
        return position

def turn(player):
    global boardgame
    print(f"--- Player {player} turn ---")
    position = ask_pos()
    boardgame_pos = boardgame[position[0]-1][position[1]-1]
    if boardgame_pos == 0 :
        boardgame[position[0]-1][position[1]-1] = player
    print_board(boardgame)

def check_win():
    global boardgame
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


