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
    while 1:
        print("Player 1 is X's and Player 2 is O's")
        play_1_move = int(input("Player 1, input the location (1-9) of your X"))
        place_mark(moves, play_1_move-1, 'X')
        play_2_move = int(input("Player 2, input the location (1-9) of your O"))
        place_mark(moves, play_2_move-1, 'O')
        print_board(moves)

def place_mark(moves, location, marker):
    moves[location] = marker


def main():
    print("Welcome To Tic Tac Toe By Joaquin Roibal!")
    moves = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    print_board(moves)
    player_input(moves)

if __name__ == "__main__":
    main()