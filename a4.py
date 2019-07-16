# a4.py

import random
import math

# ...

def print_board(board_list):
    print(' ')
    index_counter = 0
    print(' --- --- ---')
    for i in range(3):
        for j in range(3):
            if board_list[index_counter] == 'z':
                print('|  ', end=' ')
            else:
                print('| %s' % board_list[index_counter], end=' ')
            index_counter += 1 
        print('|')
        print(' --- --- ---')

def check_win(board_list):
    # row check
    for i in range(0, 9, 3):
        if board_list[i] != 'z' and board_list[i] == board_list[i+1] and board_list[i] == board_list[i+2]:
            return True
    
    # column check
    for i in range(3):
        if board_list[i] != 'z' and board_list[i] == board_list[i+3] and board_list[i] == board_list[i+6]:
            return True

    # # diagonal check 
    if board_list[0] != 'z' and board_list[0] == board_list[4] and board_list[0] == board_list[8]:
            return True
    if board_list[2] != 'z' and board_list[2] == board_list[4] and board_list[2] == board_list[6]:
            return True

    return False

def simulate(board_list, moves, moves_list, x):
    bot = 'o'
    user = 'x'
    win = False
    moves_remaining = moves
    playout_list = []
    index_list = moves_list

    for i in board_list:
        playout_list.append(i)
    
    # initial move
    playout_list[x] = bot
    win = check_win(playout_list)
    if win == True:
        return 1

    moves_remaining -= 1
    for i in range(len(index_list)):
        if index_list[i] == x:
            del index_list[i]
            break

    while win == False and moves_remaining > 0:
        rand_index = random.choice(index_list)
        playout_list[rand_index] = user
        win = check_win(playout_list)
        if win == True:
            return 0
       
        moves_remaining -= 1
        for i in range(len(index_list)):
            if index_list[i] == rand_index:
                del index_list[i]
                break
        
        if moves_remaining > 0:
            rand_index =  random.choice(index_list)
            playout_list[rand_index] = bot
            win = check_win(playout_list)
            if win == True:
                return 1

            moves_remaining -= 1
            for i in range(len(index_list)):
                if index_list[i] == rand_index:
                    del index_list[i]
                    break
    return 1

def play_a_new_game():
    board_list = []
    moves_count = 9
    user = 'x'
    bot = 'o'
    user_index = 0
    game_end = False

    for i in range(0, 9):
        board_list.append('z')
    
    choose_turn = random.randint(0, 1)
    if choose_turn == 1:
        print_board(board_list)

    while game_end == False and moves_count > 0:  
        if choose_turn == 1:   
            while True:
                user_index = input("Choose your position (index from 1 - 9): ")
                if user_index.isdigit() == False:
                    print('Invalid Response')
                    continue
                index = int(user_index)
                index = index - 1
                if index > 8 or index < 0 or board_list[index] == 'o' or board_list[index] == 'x':
                    print('Invalid Location')
                    continue
                else:
                    break  

            board_list[index] = user
            print_board(board_list)
            moves_count -= 1
            choose_turn -= 1

            game_end = check_win(board_list)
            if game_end == True:
                print(' ')
                print('x wins!')
            
        else:
            moves_dict = {}
            moves_list = []
            moves_remaining = 0
            number_of_playouts = 20

            for i in range(len(board_list)):
                if board_list[i] == 'z':
                    moves_dict[i] = 0
                    moves_list.append(i)
                    moves_remaining += 1

            for x in moves_dict:
                for y in range(number_of_playouts):
                    for i in range(len(board_list)):
                        if board_list[i] == 'z':
                            moves_list.append(i)
                            moves_remaining += 1 

                    moves_dict[x] += simulate(board_list, moves_remaining, moves_list, x)

                    moves_list.clear()
                    moves_remaining = 0
            
            for y in moves_dict:
                print('y = %d, md[%d] = %d' % (y, y, moves_dict[y]))

            # takes the max number of wins and uses the key of that value for index
            best_move = max(zip(moves_dict.values(), moves_dict.keys()))

            #best_move[1] has index and storing bot piece into it
            board_list[best_move[1]] = bot
            print_board(board_list)

            game_end = check_win(board_list)
            if game_end == True:
                print(' ')
                print('o wins!')
            moves_count -= 1
            choose_turn += 1
    
    if game_end == False:
        print(' ')
        print('Draw')

if __name__ == '__main__':
  play_a_new_game() 



