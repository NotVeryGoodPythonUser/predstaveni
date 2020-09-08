import colorama as clr

RED = 1
BLUE = -1 

def show_table(table):
    ''' Gets table as 2-dimensional list and shows it in console
        with red and blue circles.'''
    print(clr.Style.RESET_ALL)
    for i in range(len(table[0])):
        print(f"  {i+1} ", end = "")
    print(clr.Fore.WHITE)
    for line in table:
        for pol in line:
            if pol == 0:
                print(clr.Fore.WHITE, "[ ]", end="")
            if pol == RED:
                print(" [", clr.Fore.RED,"O", clr.Fore.WHITE,"]", sep="", end="")
            if pol == BLUE:
                print(" [", clr.Fore.BLUE,"O", clr.Fore.WHITE,"]", sep="", end="")
        print()

def control_table(table):
    ''' Gets table as two dimensional list
        and controls if there are 4 circles in a row.
        Returns number of player who won or None.'''
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

def control_line(line):
    ''' Gets line as list and cotrols 
        if there are 4 i a row.
        Return number of player who won or None.'''
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
    return(None)

def is_full(table):
    ''' Gets table and checks if there is any
        free space left.
        Returns True if table is full, False if not.'''
    for pol in table[0]:
        if pol == 0:
            return(False)
    return True
