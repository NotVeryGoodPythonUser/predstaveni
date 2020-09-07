from colorama import Fore, Style
table = 6*[7*[-1]]

def show_table(table):
    print(Style.RESET_ALL)
    for i in range(len(table)):
        print(f" {i+1} ")
    for line in table:
        for pol in line:
            if pol == 0:
                print(Fore.WHITE, "[ ]", end="")
            if pol == 1:
                print("[", Fore.RED,"O", Fore.WHITE,"]", sep="", end="")
            if pol == -1:
                print("[", Fore.BLUE,"O", Fore.WHITE,"]", sep="", end="")
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
            

show_table(table)
