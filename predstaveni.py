import colorama as clr
from colorama import Fore, Style

RED = 1
BLUE = -1

def show_table(table):
    print(Style.RESET_ALL)
    for i in range(len(table[0])):
        print(f"  {i+1} ", end = "")
    print()
    for line in table:
        for pol in line:
            if pol == 0:
                print(Fore.WHITE, "[ ]", end="")
            if pol == RED:
                print(" [", Fore.RED,"O", Fore.WHITE,"]", sep="", end="")
            if pol == BLUE:
                print(" [", Fore.BLUE,"O", Fore.WHITE,"]", sep="", end="")
        print()

def control_line(line):
    symbol = 0
    count = 0
    for pole in line:
        if pole == symbol:
            count += 1
        else:
            symbol = pole
            count = 1
        if count == 4 and symbol !=0:
            return(symbol)

def control_table(table):
    #lines
    for line in table:
        win = control_line(line)
        if win: return(win)
    #columns
    for i in range(len(table[0])):
        column = [line[i] for line in table]
        win = control_line(column)
        if win: return(win)
    #\ diagonals
    for i in range(4-len(table), len(table[0])-4):
        diag = []
        for j in range(len(table)):
            if (i+j >= 0) and (i+j < len(table[0])):
            	diag.append(table[j][i+j])
        win = control_line(diag)
        if win: return(win)
    #/ diagonals
    for i in range(4, len(table[0])+len(table)-4):
        diag = []
        for j in range(len(table)):
            if (i-j >= 0) and (i-j < len(table[0])):
            	diag.append(table[j][i-j])
        win = control_line(diag)
        if win: return(win)
    #no win
    return(None)

def put_disk(table, col, player):
	column = [row[col] for row in table]
	rows = list(range(len(column)))[::-1]
	for i in rows:
		if column[i] == 0:
			print("free space found: ", col, i)
			table[i][col] = player
			print(table)
			return(True)
	return(False)

def ask_put_disk(table, player):
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

def is_full(table):
	for pol in table[0]:
		if pol == 0:
			return(False)
	return True

def game():
	clr.init()
# 	table = 6*[7*[0]]
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

win = game()
if win == BLUE:
	print(Fore.BLUE, "Blue player wins")
if win == RED:
	print(Fore.RED, "Red player wins")