import os
import copy


class TicTacToe:
  
	#self.turn = 1 means it is the users turn
	def __init__(self, choice):
		self.board = [['1','2','3'], ['4','5','6'], ['7','8','9']]
		if choice == 'y' or choice == 'Y':
			self.turn = 1
		else:
			self.turn = 0
		self.num_moves = 0
		self.last_character = 'O'
		self.last_move = 0

	def printBoard(self):
		print "\n    " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2]
		for num in range (1,3):
			print "  _____________\n"
			print "    " + self.board[num][0] + " | " + self.board[num][1] + " | " + self.board[num][2] 						
		print "\n"

	#Returns 1 if the user won and 0 if the computer won, and 2 if its a cat's game
	#Otherwise -1 is returned
	def isWinning(self):
		#TODO: record last move and simply check if that last move was a winning move
		if ((self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X') or (self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X') or (self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X') or (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X') or (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X') or (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X') or (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or (self.board[2][0] == 'X' and self.board[1][1] == 'X' and self.board[0][2] == 'X') or (self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O') or (self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O') or (self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O') or (self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O') or (self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O') or (self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O') or (self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O') or (self.board[2][0] == 'O' and self.board[1][1] == 'O' and self.board[0][2] == 'O')):
			return (self.turn+1)%2
		else:
			if self.num_moves == 9:
				return 2
			else: return -1

	def isUsersTurn(self):
		if self.turn == 1: return True
		else: return False 

	def isValidSpot(self, choice):
		if choice > 9 or choice < 1: 
			return False

		if str(choice) == self.board[(choice-1)/3][(choice-1)%3]: return True
		else: return False 

	def lastMove(self):
		return self.last_move

	def performTurn(self, choice):
		next_choice_map = { 'O': 'X', 'X':'O'}
		self.board[(choice-1)/3][(choice-1)%3] = next_choice_map[self.last_character]
		self.last_character = next_choice_map[self.last_character]
		self.num_moves += 1 
		self.turn = (self.turn+1)%2
		self.last_move = choice

	def getNumMoves(self):
		return self.num_moves
	
def minimax_alpha_beta_pruning(board):

	max_utility = None
	max_move = None
	alpha = None
	beta = None
	valid_transitions = [] 

	#iterate through the choices and keep track of the valid transitions
	for num in range(1, 10):
		if board.isValidSpot(num):
			copy_board = copy.deepcopy(board)
			copy_board.performTurn(num)
			valid_transitions.append(copy_board)

	#for each of the transitions, check the utility and choose the max utility
	for transition in valid_transitions:
		copy_trans = copy.deepcopy(transition)
		utility = min_utility(copy_trans, alpha, beta)
	
		if max_utility == None or utility > max_utility:
			max_utility = utility
			max_move = transition.lastMove()

		if alpha is None or utility > alpha:
			alpha = utility
	
	return max_move

def min_utility(board, alpha, beta):
	if board.isWinning() == 0: return 1
	if board.isWinning() == 1: return -1
	if board.isWinning() == 2: return 0

	valid_transitions = []
	for num in range(1,10):
		if board.isValidSpot(num):
			copy_board = copy.deepcopy(board)
			copy_board.performTurn(num)
			valid_transitions.append(copy_board)

	min_utility = None
	min_move = None

	for transition in valid_transitions:
		copy_trans = copy.deepcopy(transition)
		utility = max_utility(copy_trans, alpha, beta)
	
		if min_utility == None or utility < min_utility:
			min_utility = utility
			min_move = copy_trans.lastMove()

		if alpha is not None and utility <= alpha:
			return utility 

		if beta is None or utility < beta:
			beta = utility
		
	return min_utility

def max_utility(board, alpha, beta):
	if board.isWinning() == 0: return 1
	if board.isWinning() == 1: return -1
	if board.isWinning() == 2: return 0
		
	valid_transitions = []
	for num in range(1, 10):
		if board.isValidSpot(num):
			copy_board = copy.deepcopy(board)
			copy_board.performTurn(num)
			valid_transitions.append(copy_board)

	max_utility = None
	max_move = None

	for transition in valid_transitions:
		copy_trans = copy.deepcopy(transition)
		utility = min_utility(copy_trans, alpha, beta)

		if utility == None or utility > max_utility:
			max_utility = utility
			max_move = copy_trans.lastMove()
	
		if beta is not None and utility >= beta:
			return utility

		if alpha is None or utility > alpha:
			alpha = utility
	
	return max_utility

def main():
	print "Welcome to Tic Tac Toe."
	valid_choice = False
	while (not valid_choice):
		choice = raw_input("Would you like to go first? Y/N " )
		if choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':
			print "Invalid entry.  Try again.\n"
		else: valid_choice = True
	game = TicTacToe(choice)
	while(game.isWinning() == -1):
		game.printBoard()
		if game.isUsersTurn():
			input = raw_input("Enter your choice of spot: ")
			try:
				spot = int(input)
				if game.isValidSpot(spot):
					game.performTurn(spot)
				else:
					print "Invalid entry. Try again.\n"
					continue
			except ValueError:
				print "Invalid entry. Try again.\n"		
				continue
		else:
			print "Computer's choice:\n"
			gamecopy = copy.deepcopy(game)
			computer_choice = minimax_alpha_beta_pruning(gamecopy)
			game.performTurn(computer_choice) 
	game.printBoard()

        if game.isWinning() == 0: print "Sorry, the computer beat you...\nGooodbye!"
	elif game.isWinning() == 1: print "Congratulations! You beat the computer!\nGoodbye!"
	else: print "Cat's game. You both lose!"		


if __name__ == "__main__" :
	main()
