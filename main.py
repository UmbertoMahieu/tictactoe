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


def turn(player):
    global boardgame
    print(f"Player {player}")
    pos = input("Send row number and case number to add your sign as (1,2) for first row, second case : ")
    position = tuple(map(int, pos.split(',')))
    boardgame_pos = boardgame[position[0]-1][position[1]-1]
    if boardgame_pos == 0 :
        boardgame[position[0]-1][position[1]-1] = player
    print(boardgame)
    print_board(boardgame)

boardgame = [[0,0,0],[0,0,0],[0,0,0]]
player1 = 1
player2 = 2

print(boardgame)
print_board(boardgame)

while True:
    turn(player1)
    turn(player2)
    for row in boardgame:
        if sum(row) == 3:
            print("player 1 win !")
        elif sum(row) == 6:
            print("player 2 win !")

