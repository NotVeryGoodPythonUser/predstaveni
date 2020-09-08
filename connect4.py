import colorama as clr
from colorama import Fore, Style

from table import show_table, control_table, is_full

RED = 1
BLUE = -1

def game():
	'''starts and runs game '''
	clr.init()
	table = [[0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0]]
	player = BLUE

	while not is_full(table):
		show_table(table)
		if player == BLUE:
			print(Fore.BLUE, "Blue player's turn")
		elif player == RED:
			print(Fore.RED, "Red player's turn")
		ask_put_disk(table, player)
		win = control_table(table)
		if win:
			show_table(table)
			return(win)
		print(Style.RESET_ALL)
		player *= -1
	show_table(table)
	return(None)

def ask_put_disk(table, player):
	''' Asks player where to put disk.
		If the player gives invalid input asks again.'''
	while True:
		column = input("Enter number of column: ")
		try:
			column = int(column)
		except:
			print("invalid input: must be number")
			continue
		if (column <= 0) or (column > len(table[0])):
			print("invalid input: must be number of column")
			continue
		valid = put_disk(table, column-1, player)
		if valid:
			break
		else:
			print("invalid input: column is full")
			continue

def put_disk(table, col, player):
	''' Writes number of player into column.
		When column is full returns False, else returns True'''
	column = [row[col] for row in table]
	rows = list(range(len(column)))[::-1]
	for i in rows:
		if column[i] == 0:
			print("free space found: ", col, i)
			table[i][col] = player
			print(table)
			return(True)
	return(False)

win = game()
if win == BLUE:
	print(Fore.BLUE, "Blue player wins")
if win == RED:
	print(Fore.RED, "Red player wins")