import random
import math
import os



class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        self.name= input(f'ingrese el nombre del jugador: \n')
        if random.randint(0, 1) == 1:
            self.humanPLayer = 'X'
            self.botPlayer = "O"
        else:
            self.humanPLayer = "O"
            self.botPlayer = "X"

    def show_board(self):
        print("")
        for i in range(3):
            print("  ", self.board[0 + (i * 3)], " | ", self.board[1 + (i * 3)], " | ", self.board[2 + (i * 3)])
            print("")

    def is_board_filled(self, state):
        return not "-" in state

    def is_player_win(self, state, player):
        if state[0] == state[1] == state[2] == player: return True
        if state[3] == state[4] == state[5] == player: return True
        if state[6] == state[7] == state[8] == player: return True
        if state[0] == state[3] == state[6] == player: return True
        if state[1] == state[4] == state[7] == player: return True
        if state[2] == state[5] == state[8] == player: return True
        if state[0] == state[4] == state[8] == player: return True
        if state[2] == state[4] == state[6] == player: return True

        return False

    def checkWinner(self):
        if self.is_player_win(self.board, self.humanPLayer):
            os.system("cls")
            print(f"   el jugador {self.name} ganó el juego!!")
            print(f"   el jugador {self.botPlayer} perdio el juego!! :( ")
            return True

        if self.is_player_win(self.board, self.botPlayer):
            os.system("cls")
            print(f"   Player {self.botPlayer} wins the game!")
            print(f"   el jugador {self.name} perdio el juego!! :( ")
            return True
        else:
            print(f'empate entre {self.name} y {self.botPlayer} ')


        if self.is_board_filled(self.board):
            os.system("cls")
            print("   Match Draw!")
            return True
        return False

    def start(self):
        bot = ComputerPlayer(self.botPlayer)
        human = humanPLayer(self.humanPLayer)
        while True:
            os.system("cls")
            print(f"   Player {self.humanPLayer} turn")
            self.show_board()

            # jugador
            square = human.human_move(self.board)
            self.board[square] = self.humanPLayer
            if self.checkWinner():
                break

            # maquina
            square = bot.machine_move(self.board)
            self.board[square] = self.botPlayer
            if self.checkWinner():
                break

        # showing the final view of board
        print()
        self.show_board()


class humanPLayer:
    def __init__(self, letter):
        self.letter = letter

    def human_move(self, state):
        # taking user input
        while True:
            square = int(input("ingrese los valores para las casillas del 1 al 9: "))
            print()
            if state[square - 1] == "-":
                break
        return square - 1


class ComputerPlayer(TicTacToe):
    def __init__(self, letter):
        self.botPlayer = letter
        self.humanPlayer = "X" if letter == "O" else "O"

    def players(self, state):
        n = len(state)
        x = 0
        o = 0
        for i in range(9):
            if (state[i] == "X"):
                x = x + 1
            if (state[i] == "O"):
                o = o + 1

        if (self.humanPlayer == "X"):
            return "X" if x == o else "O"
        if (self.humanPlayer == "O"):
            return "O" if x == o else "X"

    def actions(self, state):
        return [i for i, x in enumerate(state) if x == "-"]

    def result(self, state, action):
        newState = state.copy()
        player = self.players(state)
        newState[action] = player
        return newState

    def terminal(self, state):
        if (self.is_player_win(state, "X")):
            return True
        if (self.is_player_win(state, "O")):
            return True
        return False

    def minimax(self, state, player):
        max_player = self.humanPlayer  # jugador
        other_player = 'O' if player == 'X' else 'X'


        if self.terminal(state):
            return {'position': None,
                    'score': 1 * (len(self.actions(state)) + 1) if other_player == max_player else -1 * (
                            len(self.actions(state)) + 1)}
        elif self.is_board_filled(state):
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in self.actions(state):
            newState = self.result(state, possible_move)
            sim_score = self.minimax(newState, other_player)

            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

    def machine_move(self, state):
        square = self.minimax(state, self.botPlayer)['position']
        return square


# inicializar el juego

i = 0
while i == 0:
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
    print(' tecla para continuar ingrese 0, si desea terminar el juego ingrese cualquier: ')
    i = int(input())
