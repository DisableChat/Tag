import curses
from curses import wrapper

##
# MagikarpUsedFly
##

# Grid min and max bounds player can move in grid
MIN_BOUNDS = 0
MAX_BOUNDS = 30

##
# Messing around attempting to make a server/client run around game.
##

##
# Function:     get_directional_input
# Parameters:   loc_y and loc_x are both loaction values on screen
#   value is the value of the getkey() string value of the key input
# Description:  based on the directional input key of the user, increment or
#   deicrement the value and return the new location value.
##
def get_directional_input(loc_y, loc_x, value) -> int:

    if value == 'KEY_UP':
        if loc_y > MIN_BOUNDS:
            loc_y -= 1
        else:
            loc_y
    elif value == 'KEY_DOWN':
        if loc_y < MAX_BOUNDS:
            loc_y += 1
        else:
            loc_y
    elif value == 'KEY_LEFT':
        if loc_x > MIN_BOUNDS:
            loc_x -= 1
        else:
            loc_x
    else:
        if loc_x < MAX_BOUNDS:
            loc_x += 1
        else:
            loc_x
    return loc_y, loc_x

def main(stdscr):

    # Hide Cursor
    curses.curs_set(0)

    # Starting Possition
    Y_Cor = 2
    X_Cor = 0

    # Loop to continually update Y_Cor and X_Cor, then clear the screen and
    # print the ascii symobl in correct location.
    while True:
        stdscr.addstr(0, 0, 'Y_Cor:{} X_Cor:{}'.format(Y_Cor, X_Cor))
        #editwin = curses.newwin(5,30, 2,1)
        stdscr.addch(Y_Cor, X_Cor, '+', curses.A_UNDERLINE)
        Y_Cor, X_Cor = get_directional_input(Y_Cor, X_Cor, stdscr.getkey())
        stdscr.clear()
        stdscr.refresh()


    #curses.echo()
    #stdscr.clear()
    #stdscr.refresh()
    #stdscr.getkey()

wrapper(main)
