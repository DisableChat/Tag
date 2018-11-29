### draw for Tag.py ###
import curses

#NOTE/TODO Count: 1
# drawmap()

##
# Func:         winner
# Param:        stdscn: None, curses screen var
# Description:  winner function displays winner of tag game
#               (called when someone "tags" a player)
##
def winner(stdscr: None) -> None:
    # Hide Cursor
    curses.curs_set(0)
    while True:
        stdscr.clear()
        for i in range(5, 15, 1):
            for k in range(10, 34, 4):
                stdscr.addstr(i, k, 'TAG!', curses.A_STANDOUT)

        stdscr.refresh()

##
# Func:         scrnSetup
# Param:        stdscn: None, curses screen var
# Description:  sets up colors and hides cursor
##
def scrnSetup(stdscr: None) -> None:
    # Hide Cursor
    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
    yellow_background   = 2 # Yellow background hurts eyes

    stdscr.bkgd(curses.color_pair(yellow_background))

##
# Func:         printLoc
# Param:        stdscrn: None, curses screen var
#               CorY: int, y cordinate (current for player)
#               Corx: int, x cordinate (current for player)
#               startLoc_y: int, starting y location for player
#               startLoc_x: int, starting x location for player
# Description:  Prints the location of a player
##
def printLoc(stdscr, CorY: int, CorX: int, startLoc_y: int, startLoc_x: int) -> None:
    stdscr.addstr(startLoc_y, startLoc_x, 'Y_Cor:{} X_Cor:{}'.format(CorY, CorX))

##
# Func:         printLoc
# Param:        stdscrn: None, curses screen var
#               move: int, player turn value (1 for player 1, 2 for player 2)
#               startLoc_y: int, starting y location for text
#               startLoc_x: int, starting x location for text
# Description:  Prints which player's turn it is
##
def printPlayerMove(stdscr, move: int, startLoc_y: int, startLoc_x: int) -> None:
    stdscr.addstr(startLoc_y, startLoc_x, 'Player Move:{}'.format(move))

##
# Func:         printPlayer
# Param:        stdscn: None, curses screen var
#               Player: int, player value (1 or 2)
#               CorY: int, y cordinate (current for player)
#               Corx: int, x cordinate (current for player)
# Description:  prints the player piece and their corosponding color
##
def printPlayer(stdscr, Player: int, CorY: int, CorX: int) -> None:

    # Hide Cursor
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    cyan_dots  = 6 # Blue dots color
    default    = 4 # Green text with black background

    if Player == 1:
        stdscr.addch(CorY, CorX, '@', curses.color_pair(cyan_dots))
    else:
        stdscr.addch(CorY, CorX, '@', curses.color_pair(default))

##
# Func:         printBoundaries
# Param:        stdscn: None, curses screen var
#               gridSize_Y: int, y value for boundary length
#               gridSize_X: int, x value for boundary length
# Description:  prints the boundries of the game
##
def printBoundaries(stdscr: None, gridSize_X: int, gridSize_Y: int) -> None:

    for i in range(gridSize_X + 1):
        stdscr.addstr(0, i, '#', curses.A_REVERSE)
        stdscr.addstr(gridSize_Y, i, '#', curses.A_REVERSE)

    for k in range(gridSize_Y):
        stdscr.addstr(k, 0, '#', curses.A_REVERSE)
        stdscr.addstr(k, gridSize_X, '#', curses.A_REVERSE)


##***NOTE/TODO***##
# Make a function for the double for loop and single for loop so you can pass
# start y and start x cordinate as well as the incrment value, so then you can
# call that funtion instead of having the repdiviness as seen belowe for printMap()
##

##
# Func:         printMap
# Param:        stdscn: None, curses screen var
# Description:  Prints the terrain of the map
##
def printMap(stdscr: None) -> None:

    # Top left block
    for i in range(1, 5, 1):
        for j in range(1, 5, 1):
            stdscr.addch(i, j, '#', curses.A_BOLD)

    # Bottom right block
    for i in range(18, 25, 1):
        for j in range(20, 35, 1):
            stdscr.addch(i, j, '#', curses.A_BOLD)

    # Top right small & block
    for i in range(3, 5, 1):
        for j in range(18, 21, 1):
            stdscr.addch(i, j, '&', curses.A_BOLD)

    # top right larger & block
    for i in range(3, 5, 1):
        for j in range(24, 29, 1):
            stdscr.addch(i, j, '&', curses.A_BOLD)


    for i in range(5, 10, 1):
        stdscr.addch(i, i, '%', curses.A_BOLD)

    for i in range(4, 9, 1):
        stdscr.addch(i + 1, i, '%', curses.A_BOLD)

    for i in range(3, 8, 1):
        stdscr.addch(i + 2, i , '%', curses.A_BOLD)

    for i in range(2, 7, 1):
        stdscr.addch(i + 3, i , '%', curses.A_BOLD)

    for i in range(1, 6, 1):
        stdscr.addch(i + 4, i , '%', curses.A_BOLD)
