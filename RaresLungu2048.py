"""
Python 2048 Game : Basic Console Based User Interface For Game Play

Originally written by Phil Rodgers, University of Strathclyde
"""

from py2048_classes import Board, Tile
import time
import math
import random

def play_random_game(board):
    firstMove = random.choice(better_possible_moves(board))
    board.make_move(firstMove)
    score = board.better_random_rollout(board, 10)
    return [firstMove, score]

def determine_next_move(board):
    limit = 2000
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

  def better_possible_moves(board):
    possibilities = []
    up_possible = False
    down_possible = False
    left_possible = False
    right_possible = False
    grid_state = board.export_state()
    for y in range(4):
        for x in range(4):
            selected = grid_state[y][x]
            down_neighbour = grid_state[y + 1][x] if y < 3 else -1
            up_neighbour = grid_state[y - 1][x] if y > 0 else -1
            left_neighbour = grid_state[y][x - 1] if x > 0 else -1
            right_neighbour = grid_state[y][x + 1] if x < 3 else -1

            if check_move(selected, up_neighbour):
                up_possible = True
            if check_move(selected, down_neighbour):
                down_possible = True
            if check_move(selected, left_neighbour):
                left_possible = True
            if check_move(selected, right_neighbour):
                right_possible = True

    if up_possible:
        possibilities.append("UP")
    if down_possible:
        possibilities.append("DOWN")
    if left_possible:
        possibilities.append("LEFT")
    if right_possible:
        possibilities.append("RIGHT")
    return possibilities


def better_random_rollout(board, rounds):
    gridstate = board.export_state()
    possible_moves = better_possible_moves(board)
    scores = [board.score, board.merge_count]
    action = random.choice(possible_moves)
    board.make_move(action)
    while (not ((board.is_board_full() and board.possible_moves() == []) or rounds == 0)):
        possible = better_possible_moves(board)
        board.make_move(random.choice(possible))
        board.add_random_tiles(1)
        rounds -= 1
    retscore = board.merge_count
    board.grid = []
    for row in gridstate:
        copy2 = []
        for elem in row:
            if elem is None:
                copy2.append(None)
            else:
                copy2.append(Tile(elem))
        board.grid.append(copy2)
    board.score = scores[0]
    board.merge_count = scores[1]
    return retscore


def check_move(center, adjacent):
    if center == adjacent:
        if center is not None:
            return True
    if center is not None and center != -1 and adjacent is None:
        return True
    return False
