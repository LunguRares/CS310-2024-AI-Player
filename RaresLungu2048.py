"""
Python 2048 Game : Basic Console Based User Interface For Game Play

Originally written by Phil Rodgers, University of Strathclyde
"""

from py2048_classes import Board, Tile
import time
import math
import random

def play_random_game(board):
    firstMove = board.possible_moves()[random.randint(0,len(board.possible_moves())-1)]
    board.make_move(firstMove)
    score = board.random_rollout(math.inf)
    return [firstMove, score]

def determine_next_move(board):
    limit = 500
    sums = [0, 0, 0, 0] # UP   DOWN    LEFT    RIGHT
    counts =   [0, 0, 0, 0]
    for i in range(0, limit):
        newBoard = Board(board.export_state(), board.score, board.merge_count)
        result = play_random_game(newBoard)
        if result[0] == "UP":
            sums[0] += result[1]
            counts[0] += 1
        elif result[0] == "DOWN":
            sums[1] += result[1]
            counts[1] += 1
        elif result[0] == "LEFT":
            sums[2] += result[1]
            counts[2] += 1
        elif result[0] == "RIGHT":
            sums[3] += result[1]
            counts[3] += 1
    averages = [0, 0, 0, 0]
    if(counts[0] != 0):
        averages[0] = sums[0]/counts[0]
    if(counts[1] != 0):
        averages[1] = sums[1]/counts[1]
    if(counts[2] != 0):
        averages[2] = sums[2]/counts[2]
    if(counts[3] != 0):
        averages[3] = sums[3]/counts[3]
    maxAverage = averages[0]
    move = "UP"
    if averages[1] > maxAverage:
        maxAverage = averages[1]
        move = "DOWN"
    if averages[2] > maxAverage:
        maxAverage = averages[2]
        move = "LEFT"
    if averages[3] > maxAverage:
        maxAverage = averages[3]
        move = "RIGHT"
            
    return move
    
            

def main():
#    allmoves = ['UP','LEFT','DOWN','RIGHT']
    board = Board()
    board.add_random_tiles(2)
    print("main code")

    move_counter = 0
    move = None
    move_result = False
    
    
    overalltime=time.time()
    while True:
        print("Number of successful moves:{}, Last move attempted:{}:, Move status:{}".format(move_counter, move, move_result))
        print(board)
       # print(board.print_metrics())
        if board.possible_moves()==[]:
            if (board.get_max_tile()[0]<2048):
                print("You lost!")
            else:
                print("Congratulations - you won!")
            break
        begin = time.time()
###################################### Your code should be inserted below 
###################################### (feel free to define additional functions to determine the next move)
        
#        move = board.possible_moves()[random.randint(0,len(board.possible_moves())-1)]
        move = determine_next_move(board)
        board.make_move(move)
        
        
######################################  Do not modify 4 lines below      
######################################
        print("Move time: ", time.time()-begin)
        board.add_random_tiles(1)
        move_counter = move_counter + 1
    print("Average time per move:", (time.time()-overalltime)/move_counter)
    

if __name__ == "__main__":
    main()

  
