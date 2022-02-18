from tic_tac_toe import Game
import numpy as np
import random
import time

# Performs the random algorithm for the player and returns the time
def t_rand(cur_game):
    start = time.process_time()
    cur_game.random_play()
    end = time.process_time()
    return end - start

# Performs the MinMax algorithm for the player and returns the time. Can be set tested depth.
def t_minmax(cur_game, depth = 2):
    start = time.process_time()
    cur_game.minimax(depth)
    end = time.process_time()
    return end - start

# Performs the Full Minmax algorithm for the player and returns the time
def t_minmax_f(cur_game):
    start = time.process_time()
    cur_game.minimax_full()
    end = time.process_time()
    return end - start

# Plays a game with ingiven algorithms for player A and player B and shows the go of the game as it goes
def play_game_fancy(player_a, player_b):
    game = Game()
    step = 1
    for i in range(1,6):
        print("===============")
        print("ROUND:",step)
        player_a(game)
        game.show_board()
        if game.winner_give() != None:
            print("Game Ended")
            return print(game.winner)
        step += 1
        print("===============")
        print("ROUND:",step)
        player_b(game)
        game.show_board()
        if game.winner_give() != None:
            print("Game Ended")
            return print(game.winner)
        step += 1

# Plays games but give only the results
def play_game_win_only(player_a, player_b):
    game = Game()
    for i in range(6):
        player_a(game)
        if game.winner_give() != None:
            return game.winner
        player_b(game)
        if game.winner_give() != None:
            return game.winner

# Gives the outcome for many games of two given algorithms
def win_lose_calc(times_played, player_a, player_b, name_a, name_b):
    stats = { -1:0, 0:0, 1:0}
    for i in range(times_played):
        # The print(i) is for measuring the progress of the test. Implemented after the first attempts of doing 100 iterations took longer than 20 min.
        #print(i)     
        game = Game()
        for i in range(6):
            player_a(game)
            if game.winner_give() != None:
                stats[game.winner] += 1
                break
            player_b(game)
            if game.winner_give() != None:
                stats[game.winner] += 1
                break

    print("Player A:", name_a)
    print("Wins: ", stats[1] )
    print("Player B:", name_b)
    print("Wins: ", stats[-1] )
    print("DRAW: ", stats[0])

# Gives the average time of all turns an algorithm is going first or second
def move_avg_time(player_a, player_b,times):
    time_a = [0,0]
    time_b = [0,0]
    for i in range(times):
        # The print(i) is for measuring the progress of the test. Implemented after the first attempts of doing 100 iterations took longer than 20 min.
        #print(i)
        game = Game()
        for i in range(6):
            time_a[0] += player_a(game)
            time_a[1] += 1
            if game.winner_give() != None:
                break
            time_b[0] += player_b(game)
            time_b[1] += 1
            if game.winner_give() != None:
                break
    return [time_a[0]/time_a[1], time_b[0]/time_b[1]]


#This section has the various test for the algorithms

play_game_fancy(t_rand, t_minmax_f)
play_game_fancy(t_minmax, t_minmax_f)
play_game_fancy(t_rand, t_minmax)

#win_lose_calc(50, t_rand, t_minmax_f, "Random", "MinMax_FULL")
#win_lose_calc(50, t_minmax_f, t_rand, "MinMax_FULL", "Random")


#win_lose_calc(50, t_minmax_f, t_minmax, "MinMax_FULL", "MinMax")
#win_lose_calc(50, t_minmax, t_minmax_f, "MinMax", "MinMax_FULL")


#win_lose_calc(50, t_rand, t_minmax, "Random", "MinMax")
#win_lose_calc(50, t_minmax, t_rand, "MinMax", "Random")

#print(move_avg_time(t_rand, t_rand,100))
#print(move_avg_time(t_minmax, t_minmax,100))
#print(move_avg_time(t_minmax_f, t_minmax_f,100))

