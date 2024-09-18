board = ["-" for i in range(9)]

def print_board(board):
    row_one=(f"| {board[0]} | {board[1]} | {board[2]} |")
    row_two=(f"| {board[3]} | {board[4]} | {board[5]} |")
    row_three=(f"| {board[6]} | {board[7]} | {board[8]} |")
    print(row_one)
    print(row_two)
    print(row_three)
#print_board(board)


def player_one_input(player_number):
    while True:
      player_1_name=input(f"Hi,Player{player_number},what is your name?").strip().upper()
      if player_1_name.isalpha():
         return player_1_name
      else:
         print("enter a valid name!!!!!!!!!!!!!!!!!!!!!!!!")
def player_two_input(player_number):
    while True:
        player_2_name=input(f"Hi,Player{player_number},what is your name?").strip().upper()
        if player_2_name.isalpha():
            return player_2_name
        else:
            print("enter a valid name please!!!!!!!!!!")

def player_mark_move(player_one_input,player_two_input):

    while True:
        player_mark1=input(f"hi player1, {player_one_input} pick X or O")
        if player_mark1 in ["X","O"]:
            break
        else:
            print("enter X or O otherwise dont play!!!!!!!!!!!!!")


    while True :
        player_mark2=input(f"hi player2, {player_two_input} pick X or O ")
        if player_mark2 in ["X","O"] and player_mark2 != player_mark1:
            break
        else:
            print("enter X or O otherwise dont run my game")
    return player_mark1 , player_mark2




def make_move_player1(player_name,board,mark_choice1):


    while True:
            move = int(input(f"{player_name},with *({mark_choice1})* choose a position between 1 and 9: "))-1
            if move < 0 or move > 8  :
                print("Invalid position. Choose a number between 1 and 9.")
            elif board[move] == "-" :
                board[move] = mark_choice1
                break

def make_move_player2(player2,board,mark_choice2):
    while True:
        move = int(input(f"{player2},with *({mark_choice2})* choose a position between 1 and 9: ")) - 1
        if move < 0 or move > 8  :
            print("Invalid position. Choose a number between 1 and 9.")
        elif board[move] == "-" and board[move] != move:
            board[move] = mark_choice2
            break



#player1=player_one_input(1)
#player2=player_two_input(2)
#mark_choice1,mark_choice2=player_mark_move(player1,player2)

def check_winning(board):

       if (board[0]==board[1]==board[2]  != "-"):#rows
        print(f"the winner is who chose:{board[1]} Mark")
        return True
       elif (board[3]==board[4]==board[5] != "-"):#rows
        print(f"the winner is who chose:{board[4]} Mark")
        return True
       elif (board[6]==board[7]==board[8] != "-"):#rows
        print(f"the winner is who chose:{board[7]} Mark")
        return True
       elif (board[0]==board[4]==board[8] != "-"):#Digonl
        print(f"the winner is who chose:{board[0]} Mark")
        return True
       elif (board[2]==board[4]==board[6] != "-"):#diganol
        print(f"the winner is who chose:{board[2]} Mark")
        return True
       elif (board[0]==board[3]==board[6] != "-"):#colums
           print(f"the winner is who chose:{board[0]} Mark")
           return True
       elif (board[1] == board[4] == board[7] != "-"):#colums
           print(f"the winner is who chose:{board[1]} Mark")
           return True
       elif (board[2] == board[5] == board[8] != "-"):#colums
           print(f"the winner is who chose:{board[2]} Mark")
           return True
       return False


def check_draw(board):
        if "-" not in board:
            print("its draw")
            return True
        return False

def reset_board():
    return ["-" for _ in range(9)]


def running_game(player1,player2,mark_choice1,mark_choice2,board):
  #player 1 move
  make_move_player1(player1,board,mark_choice1)
  print_board(board)

  if check_winning(board) :
   return True
  if check_draw(board):
      return True
  #player 2 move

  make_move_player2(player2, board, mark_choice2)
  print_board(board)
  if check_winning(board):
   return True
  if check_draw(board):
      return True
  return False


#player1 = player_one_input(1)
#player2 = player_two_input(2)
#mark_choice1, mark_choice2 = player_mark_move(player1, player2)
if __name__ == '__main__':
        while True:
            board = reset_board()
            player1 = player_one_input(1)
            player2 = player_two_input(2)
            mark_choice1, mark_choice2 = player_mark_move(player1, player2)


            while True:
                    game_ended=running_game(player1, player2, mark_choice1, mark_choice2, board)
                    if game_ended:
                          break


            # Asking players to play agin
            play_again = input(" another round??? Y or N: ").strip().upper()
            if play_again == "N":
             print("Dont play !")
             break


















       # player1 = player_one_input(1)
        #player2 = player_two_input(2)
        #mark_choice1, mark_choice2 = player_mark_move(player1, player2)
        #while not running_game(player1, player2, mark_choice1, mark_choice2, board):
       #     continue
        #play_again = input("Another game ? Y or N")
        #if play_again != "Y":
         #   print("thanks for playing")
          #  break



