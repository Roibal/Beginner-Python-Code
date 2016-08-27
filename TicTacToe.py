def print_board(moves):
    """
    The Purpose of this python program is to allow 2 players to play tic-tac-toe
    Function will print a board based on 'moves' list
    :return:
    """
    board = "%s  |  %s  |  %s \n" %(moves[0], moves[1], moves[2])
    board += "___|_____|____\n"
    board += "%s  |  %s  |  %s \n" %(moves[3], moves[4], moves[5])
    board += "___|_____|____\n"
    board += "%s  |  %s  |  %s \n" %(moves[6], moves[7], moves[8])
    board += "   |     |     "
    print(board)

def player_input(moves):
    while check_board(moves):
        print("Player 1 is X's and Player 2 is O's")
        play_1_move = int(input("Player 1, input the location (1-9) of your X"))
        place_mark(moves, play_1_move-1, 'X')
        check_board(moves)
        play_2_move = int(input("Player 2, input the location (1-9) of your O"))
        place_mark(moves, play_2_move-1, 'O')
        print_board(moves)
        check_board(moves)

def place_mark(moves, location, marker):
    moves[location] = marker
    
def check_board(moves):
    winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for combo in winning_combos:
        if moves[combo[0]]==moves[combo[1]]==moves[combo[2]]:
            if moves[combo[0]] == "_":
                return True
            print('str(moves[0]) + wins!')
            return False
        else:
            return True

def main():
    print("Welcome To Tic Tac Toe By Joaquin Roibal!")
    moves = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    print_board(moves)
    player_input(moves)

if __name__ == "__main__":
    main()
