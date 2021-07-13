# Imports
import random

# Constants
SIZE = 5
BOARD = [["0" for row in range(SIZE)] for col in range(SIZE)]
DISPLAYED_BOARD = [["_" for row in range(SIZE)] for col in range(SIZE)]

# Functions
def get_position(index):
	'''
	Take in a number index and return the corresponding row and column
	'''
	row = index // SIZE
	col = index % SIZE
	return row, col


def populate_board():
	'''
	Populate the board with a certain number of bombs, depending on the size
	No. bombs = Size + 1
	'''
	for i in range(SIZE + 1):
		while True:
			index = random.randint(0, SIZE**2 - 1)
			row, col = get_position(index)
			if BOARD[row][col] != "*":
				BOARD[row][col] = "*"
				increment_adjacents(row-1, col)
				increment_adjacents(row+1, col)
				increment_adjacents(row, col+1)
				increment_adjacents(row, col-1)
				increment_adjacents(row+1, col-1)
				increment_adjacents(row+1, col+1)
				increment_adjacents(row-1, col-1)
				increment_adjacents(row-1, col+1)
				break
			else:
				continue

				
def increment_adjacents(row, col):
	'''
	Increment the specified tile if it is valid
	A valid tile isn't out of bounds and isn't a bomb
	'''
	if (row != SIZE) and (col != SIZE) and (row != -1) and (col != -1):
		if BOARD[row][col] != '*':
			original = int(BOARD[row][col])
			new = original + 1
			BOARD[row][col] = str(new)

def check_adjacents(row, col):
	'''
	Check all unexplored adjacent tiles to see if they have a 0 value
	If so, explore this tile and recusively check its adjacent tiles
	This builds up a stack of check_adjancents() calls
	'''
	if row > 0:
		if BOARD[row-1][col] == '0' and DISPLAYED_BOARD[row-1][col] == "_":
			DISPLAYED_BOARD[row-1][col] = '0'
			check_adjacents(row-1, col)
	if row < SIZE-1:
		if BOARD[row+1][col] == '0' and DISPLAYED_BOARD[row+1][col] == "_":
			DISPLAYED_BOARD[row+1][col] = '0'
			check_adjacents(row+1, col)
	if col < SIZE-1:
		if BOARD[row][col+1] == '0' and DISPLAYED_BOARD[row][col+1] == "_":
			DISPLAYED_BOARD[row][col+1] = '0'
			check_adjacents(row, col+1)
	if col > 0:	
		if BOARD[row][col-1] == '0' and DISPLAYED_BOARD[row][col-1] == "_":
			DISPLAYED_BOARD[row][col-1] = '0'
			check_adjacents(row, col-1)

def move(row, col):
	'''
	Take the player's move
	End the game if the player selects a bomb
	Explore the tile if it is not a bomb, calling check_adjacents() if it is a 0
	'''
	if BOARD[row][col] == '*':
		print("Game over! Here is the full board!")
		display_board(BOARD)
		input()
		exit()
	if BOARD[row][col] == '0':
		DISPLAYED_BOARD[row][col] = '0'
		check_adjacents(row, col)
	else:
		DISPLAYED_BOARD[row][col] = BOARD[row][col]

def display_board(board):
	'''
	Display the board's arrays in a more user friendly layout
	Add an axis and use | to separate tiles
	'''
	print(".", end =" | ")
	for i in range(SIZE):
		print(i, end =" | ")
	print()
	count = 0
	for r in board:
		print(count, end =" | ")
		for c in r:
			print(c, end =" | ")
		print()
		count = count + 1


# Main
if __name__ == '__main__':
	populate_board()
	print("\nWelcome to Minesweeper. Enter q at any time to quit.\n")
	while True:
		print("Current board:")
		display_board(DISPLAYED_BOARD)
		while True:
			choice = input("Make a move (row, column): ")
			if choice.lower() == 'q':
				exit()
			try:
				row, column = choice.split(', ')
				break
			except:
				print("Ensure you are entering coordinates as 'row, column'")
		move(int(row), int(column))
