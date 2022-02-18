import numpy as np
import random

#Class which implements the game of tic_tac_toe
class Game:
    def __init__(self, board = [0,0,0,0,0,0,0,0,0] ):
        self.board = np.array(board).reshape((3,3))
        self.current_player = 1
        self.winner = None
        self.moves_left = [0,1,2,3,4,5,6,7,8]
        self.cordinates_for_moves = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
        self.heur_tab = [[3, 2, 3], [2, 4, 2], [3, 2, 3]]

    # Give the winner of the match
    def winner_give(self):
        self.winner = self.check_winner(self.current_player)
        return self.winner

    # Fucntion checks if current player has won
    def check_winner(self, current_player, normal = -1):
        winner = current_player *normal
        win_value = current_player * normal * 3

        column = np.sum(self.board, axis = 0)
        for x in range(3):
            if column[x] == win_value:
                return winner 

        row = np.sum(self.board, axis =1)
        for y in range(3):
            if row[y] == win_value:
                return winner

        diag_1 = np.sum(self.board.diagonal())
        if diag_1 == win_value:
            return winner

        diag_2 = np.fliplr(self.board).diagonal()
        if np.sum(diag_2) == win_value:
            return winner

        if len(self.moves_left) == 0:
            return 0

    # Shows current state of the board
    def show_board(self):
        print(self.board)

    # Makes a move on the board
    def make_move(self, coordinates):
        x,y = self.cordinates_for_moves[coordinates]
        self.board[x][y] = self.current_player
        self.current_player *= -1
        self.moves_left.remove(coordinates)

    # Cancels a move on the board
    def un_make_move(self, coordinates):
        x,y = self.cordinates_for_moves[coordinates]
        self.board[x][y] = 0
        self.current_player *= -1
        self.moves_left.append(coordinates)

    # Makes a random move
    def random_play(self):
        move = random.choice(self.moves_left)
        self.make_move(move)

    # Algorithm minmax_full
    def minimax_full(self):
        best_move = self.minimax_prestep(  self.current_player)
        self.make_move(best_move[1])

    # Inner recursive function for the Full MinMax algorithm
    def minimax_prestep(self,  player, path = None):
        winner = self.check_winner( self.current_player) 
        if winner is not None:
            return [winner * player,path]
        layer = []
        for path in self.moves_left.copy():
                self.make_move(path)
                layer.append([self.minimax_prestep( player, path)[0], path])
                self.un_make_move(path)
        if self.current_player == player:
            return max(layer, key = lambda k: k[0])
        else:
            return min(layer, key = lambda k: k[0])

    # Heuristic function, that uses the heuristic table
    def heuristic(self):
        result = 0
        for i in range(3):
            for j in range(3):
                result += self.board[i][j] * self.heur_tab[i][j]
        return result

    # MinMax function with a heuristic
    def minimax(self, depth):
        best_move = self.minimax_dig(self.current_player, depth)
        self.make_move(best_move[1])

    # The inner recursive function for the MinMax algortithm with a heuristic
    def minimax_dig(self,  player, depth, path = None):
        winner = self.check_winner( self.current_player) 
        if winner is not None:
            return [winner * player*10, path]
        if depth == 0:
            heuro = self.heuristic() 
            return [heuro*player , path]
        layer = []
        for path in self.moves_left.copy():
                self.make_move(path)
                layer.append([self.minimax_dig( player, depth -1, path)[0], path])
                self.un_make_move(path)
        if self.current_player == player:
            return max(layer, key = lambda k: k[0])
        else:
            return min(layer, key = lambda k: k[0])

