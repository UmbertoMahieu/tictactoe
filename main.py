class TicTacToe:
    def __init__(self, size = 3):
        self.size = size
        self.board = [[0 for e in range(self.size)] for e in range(self.size)]
        self.player1 = "X"
        self.player2 = "O"
        self.max_turn = size * size


    def print_board(self):
        for x in range(self.size):
            display_row = ""
            for n in range(self.size):
                if self.board[x][n] == "O":
                    display_row += " ".join(" O ")
                elif self.board[x][n] == "X" :
                    display_row += " ".join(" X ")
                else :
                    display_row += " ".join("   ")
                if n != len(self.board) - 1:
                    display_row += " ".join(" | ")
            print(display_row)
            if x != len(self.board) - 1:
                print("--------------------------")


    def check_value(self):
        try:
            pos = input("Send row number and case number to add your sign. eg: 1,2 for first row, second case : ")
            position = tuple(map(int, pos.split(',')))
            row,col = position[0] - 1, position[1] - 1
            if row not in range(3) or col not in range(3):
                print("Case doesn't exist, try another one")
                return self.check_value()
            if self.board[row][col] != 0 :
                print("Case already taken, try another one")
                return self.check_value()
            else:
                return row,col
        except (ValueError, IndexError):
            print("Wrong input. Try again")
            return self.check_value()

    def turn_manager(self, player):
        print(f"--- Place your {player} ---")
        row,col = self.check_value()
        self.board[row][col] = player

    def find_winner(self):
        for i in range(self.size):
            if all(self.board[i][j] == self.board[i][0] != 0 for j in range(self.size)):
                return self.board[i][0]
            if all(self.board[j][i] == self.board[0][i] != 0 for j in range(self.size)):
                return self.board[0][i]
        if all(self.board[i][i] == self.board[0][0] != 0 for i in range(self.size)):
            return self.board[0][0]
        if all(self.board[i][self.size - 1 - i] == self.board[self.size - 1][0] != 0  for i in reversed(range(self.size - 1))):
            return self.board[self.size - 1][0]
        else:
            return None

    def win_check(self):
        winner = self.find_winner()
        if winner :
            if winner == self.player1:
                print(f"Player {self.player1} won ! ")
            if winner == self.player2:
                print(f"Player {self.player2} won ! ")
            return True
        else:
            return False

    def start_game(self):
        rounds = 0
        player = self.player1
        while rounds < self.max_turn:
            rounds += 1

            self.print_board()
            self.turn_manager(player)
            if self.win_check():
                break

            if player == self.player1:
                player = self.player2
            else:
                player = self.player1

game = TicTacToe()
game.start_game()


