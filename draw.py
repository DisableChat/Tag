### draw for Tag.py ###
import curses

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
        for i in range(10):
            stdscr.addstr(i, 0, 'TAG!')
            for k in range(5):
                stdscr.addstr(i, k*4, 'TAG!')

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
        stdscr.addstr(0, i, '#')
        stdscr.addstr(gridSize_Y, i, '#')

    for k in range(gridSize_Y):
        stdscr.addstr(k, 0, '#')
        stdscr.addstr(k, gridSize_X, '#')

##
# Func:         printMap
# Param:        stdscn: None, curses screen var
# Description:  Prints the terrain of the map
##
def printMap(stdscr: None) -> None:

    j = 1
    for i in range(5):
        stdscr.addch(i, j, '#')
        for j in range(5):
            stdscr.addch(i, j, '#')

    j1 = 20
    for i1 in range(18, 25, 1):
        stdscr.addch(i1, j1, '#')
        for j1 in range(20, 35, 1):
            stdscr.addch(i1, j1, '#')
