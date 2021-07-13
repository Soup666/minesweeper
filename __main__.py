from pprint import pprint
import random

SIZE = 10
DEV_BOARD = [[0 for row in range(SIZE)] for column in range(SIZE)]
USER_BOARD = [[' ' for row in range(SIZE)] for column in range(SIZE)]

DEBUG_CHECKED_TILES = []

def print_board(board):
	print("    " + ''.join([(f"{column_index}, ") for column_index in range(SIZE-1)]) + (f"{SIZE-1}"))
	print("" + ''.join("---" for i in range(SIZE+2)))
	index = 0
	for row in board:
		print((f"{index} | ") + ''.join([(f"{i}  ") for i in row]))
		index += 1

def check_coord(x,y):
	global DEBUG_CHECKED_TILES

	if x < 0 or x > SIZE-1 or y < 0 or y > SIZE-1 or [x,y] in DEBUG_CHECKED_TILES:
		return

	if DEV_BOARD[x][y] == 0:
		USER_BOARD[x][y] = '0'
		DEBUG_CHECKED_TILES.append([x,y])
		check_coord(x+1,y)
		check_coord(x-1,y)
		check_coord(x,y+1)
		check_coord(x,y-1)
	elif DEV_BOARD[x][y] == '*':
		USER_BOARD[x][y] = DEV_BOARD[x][y]
		print("Game over!")
		return True
	else:
		USER_BOARD[x][y] = DEV_BOARD[x][y]

def increment_adjacent(x,y):
	for _x in range(3):
		for _y in range(3):
			if DEV_BOARD[x+_x-1][y+_y-1] == '*':
				continue
			try:
				#print((f"{_x-1}, {_y-1}"))
				DEV_BOARD[x+_x-1][y+_y-1] += 1
			except Exception as e:
				print(e)
				


def populate_board(amount):
	for i in range(amount):
		x = random.randint(1, SIZE-2)
		y = random.randint(1, SIZE-2)
		DEV_BOARD[x][y] = '*'
		try:
			increment_adjacent(x,y)
		except Exception as e:
			pass


def main():
	populate_board(10)

	while True:
		print_board(USER_BOARD)
		user = input("Enter \"x,y\": ").upper()
		if user == 'Q':
			return
		else:
			coord = user.split(',')
			coord[0] = int(coord[0])
			coord[1] = int(coord[1])
			print(coord)

			if check_coord(coord[0],coord[1]):
				return
			DEBUG_CHECKED_TILES = []

if __name__ == '__main__':
	main()

		