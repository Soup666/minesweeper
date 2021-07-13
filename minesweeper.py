# Imports
import random

SIZE = 5
BOARD = [["0" for row in range(SIZE)] for col in range(SIZE)]
DISPLAYED_BOARD = [["_" for row in range(SIZE)] for col in range(SIZE)]

def get_coords(index):
	row = index // SIZE
	col = index % SIZE
	return row, col

def populate_board():
	for i in range(SIZE + 1):
		while True:
			position = random.randint(0, SIZE**2 - 1)
			row, col = get_coords(position)
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
	if (row != SIZE) and (col != SIZE) and (row != -1) and (col != -1):
		if BOARD[row][col] != '*':
			original = int(BOARD[row][col])
			new = original + 1
			BOARD[row][col] = str(new)

def check_adjacents(row, col):
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
	if BOARD[row][col] == '*':
		print("Game over! Here is the full board!")
		display_board(BOARD)
		exit()
	if BOARD[row][col] == '0':
		DISPLAYED_BOARD[row][col] = '0'
		check_adjacents(row, col)
	else:
		DISPLAYED_BOARD[row][col] = BOARD[row][col]

def display_board(board):
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


if __name__ == '__main__':
	populate_board()
	print(" __   __  ___   __    _  _______    _______  _     _  _______  _______  _______  _______  ______   ")
	print("|  |_|  ||   | |  |  | ||       |  |       || | _ | ||       ||       ||       ||       ||    _ |  ")
	print("|       ||   | |   |_| ||    ___|  |  _____|| || || ||    ___||    ___||    _  ||    ___||   | ||  ")
	print("|       ||   | |       ||   |___   | |_____ |       ||   |___ |   |___ |   |_| ||   |___ |   |_||_ ")
	print("|       ||   | |  _    ||    ___|  |_____  ||       ||    ___||    ___||    ___||    ___||    __  |")
	print("| ||_|| ||   | | | |   ||   |___    _____| ||   _   ||   |___ |   |___ |   |    |   |___ |   |  | |")
	print("|_|   |_||___| |_|  |__||_______|  |_______||__| |__||_______||_______||___|    |_______||___|  |_|")
	print("___________________________________________________________________________________________________")
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
