import curses
from curses import wrapper
import mechanic
import draw

##
# MagikarpUsedFly
##


def main(stdscr):

    # Hide Cursor
    curses.curs_set(0)

    # Player move 1 for player1 and 2 for player 2
    move =      1

    # Starting Possition
    Y_Cor =     8
    X_Cor =     8
    Y2_Cor =    7
    X2_Cor =    8


    # Loop to continually update Y_Cor and X_Cor, then clear the screen and
    # print the ascii symobl in correct location.
    while True:

        stdscr.addstr(0, 0, 'Y_Cor:{} X_Cor:{}'.format(Y_Cor, X_Cor))
        stdscr.addstr(1, 0, 'Y2_Cor:{} X2_Cor:{}'.format(Y2_Cor, X2_Cor))
        stdscr.addstr(12,12, 'Player Move:{}'.format(move))

        stdscr.addch(Y_Cor, X_Cor, '+', curses.A_UNDERLINE)
        stdscr.addch(Y2_Cor, X2_Cor, '@', curses.A_UNDERLINE)


        if move == 1:
            if mechanic.tag(Y_Cor, Y2_Cor, X_Cor, X2_Cor):
                wrapper(draw.winner)
            playerOne_y, playerOne_x = mechanic.GPDI_P1(Y_Cor, X_Cor, stdscr.getkey())
            if not mechanic.tag(playerOne_y, Y_Cor, playerOne_x, X_Cor):
                X_Cor = playerOne_x
                Y_Cor = playerOne_y
                move = 2

        elif move == 2:
            if mechanic.tag(Y_Cor, Y2_Cor, X_Cor, X2_Cor):
                wrapper(draw.winner)
            playerTwo_y, playerTwo_x = mechanic.GPDI_P2(Y2_Cor, X2_Cor, stdscr.getkey())
            if not mechanic.tag(playerTwo_y, Y2_Cor, playerTwo_x, X2_Cor):
                X2_Cor = playerTwo_x
                Y2_Cor = playerTwo_y
                move = 1
                
        stdscr.clear()
        stdscr.refresh()



wrapper(main)
