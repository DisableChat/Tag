import curses
from curses import wrapper
import mechanic
import draw

##
# MagikarpUsedFly
##


def main(stdscr):

    draw.scrnSetup(stdscr)

    # Player move 1 for player1 and 2 for player 2
    move =      1
    playerOne = 1
    playerTwo = 2
    # Starting Possition
    Y_Cor =     8
    X_Cor =     8
    Y2_Cor =    7
    X2_Cor =    8


    # Loop to continually update Y_Cor and X_Cor, then clear the screen and
    # print the ascii symobl in correct location.
    while True:

        draw.printLoc(stdscr, Y_Cor, X_Cor, 0, 0)
        draw.printLoc(stdscr, Y2_Cor, X2_Cor, 1, 0)
        draw.printPlayerMove(stdscr, move, 2, 0)


        draw.printPlayer(stdscr, playerOne, Y_Cor, X_Cor)
        draw.printPlayer(stdscr, playerTwo, Y2_Cor, X2_Cor)


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
