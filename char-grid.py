import curses
from curses import wrapper

##
# MagikarpUsedFly
##

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
        #stdscr.addstr('key up {}')
        loc_y -= 1
    elif value == 'KEY_DOWN':
        #stdscr.addstr('key down')
        loc_y += 1
    elif value == 'KEY_LEFT':
        #stdscr.addstr('key left')
        loc_x -= 1
    else:
        #stdscr.addstr('key right')
        loc_x += 1
    return loc_y, loc_x

def main(stdscr):

    # Hide Cursor
    curses.curs_set(0)
    Y_Cor = 0
    X_Cor = 0

    # Loop to continually update Y_Cor and X_Cor, then clear the screen and
    # print the ascii symobl in correct location.
    while True:
        Y_Cor, X_Cor = get_directional_input(Y_Cor, X_Cor, stdscr.getkey())
        stdscr.clear()
        stdscr.addch(Y_Cor, X_Cor, '+')
        stdscr.refresh()


    #curses.echo()
    #stdscr.clear()
    #stdscr.refresh()
    #stdscr.getkey()

wrapper(main)
