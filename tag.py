### tag.py ###

import curses
from curses import wrapper
import sys
import mechanic
import draw

##
# MagikarpUsedFly
##

##
# Func:         main
# Param:        stdscn: None, curses screen var
# Description:  calls functions to run "tag" game
##
def main(stdscr):

    draw.scrnSetup(stdscr)

    # Draw border around "map" of tag evniroment
    gridSize_X = mechanic.MAX_BOUNDS_X
    gridSize_Y = mechanic.MAX_BOUNDS_Y

    # Player move 1 for player1 and 2 for player 2
    move =      1
    playerOne = 1
    playerTwo = 2

    # Starting Possitions
    Y_Cor =     20
    X_Cor =     10
    Y2_Cor =    8
    X2_Cor =    26

    ## TODO:
    # Make more specific error handling
    # Giant try/except doesn't give specific errors so its harder to trace.
    ##
    try:
        # Loop to continually update Y_Cor and X_Cor, then clear the screen and
        # print the ascii symobl in correct location.
        while True:

            # Display the locations of each player and whos turn it is
            draw.printLoc(stdscr, Y_Cor, X_Cor, gridSize_Y + 1, 0)
            draw.printLoc(stdscr, Y2_Cor, X2_Cor, gridSize_Y + 2, 0)
            draw.printPlayerMove(stdscr, move, gridSize_Y + 3, 0)

            # Print the boundries and map
            draw.printBoundaries(stdscr, gridSize_X, gridSize_Y)
            draw.printMap(stdscr)

            # Print the players
            draw.printPlayer(stdscr, playerOne, Y_Cor, X_Cor)
            draw.printPlayer(stdscr, playerTwo, Y2_Cor, X2_Cor)

            # Player 1 move
            if move == 1:
                if mechanic.tag(Y_Cor, Y2_Cor, X_Cor, X2_Cor):
                    wrapper(draw.winner)

                # Update players locatoin
                playerOne_y, playerOne_x = mechanic.GPDI_P1(Y_Cor, X_Cor, stdscr.getkey())
                if not mechanic.tag(playerOne_y, Y_Cor, playerOne_x, X_Cor):
                    X_Cor = playerOne_x
                    Y_Cor = playerOne_y
                    move = 2

            # Player 2 move
            elif move == 2:
                if mechanic.tag(Y_Cor, Y2_Cor, X_Cor, X2_Cor):
                    wrapper(draw.winner)

                # Update players locatoin
                playerTwo_y, playerTwo_x = mechanic.GPDI_P2(Y2_Cor, X2_Cor, stdscr.getkey())
                if not mechanic.tag(playerTwo_y, Y2_Cor, playerTwo_x, X2_Cor):
                    X2_Cor = playerTwo_x
                    Y2_Cor = playerTwo_y
                    move = 1

            stdscr.clear()
            stdscr.refresh()

    # User ctr^c
    except KeyboardInterrupt:
        sys.exit("Keyboard Interrupt, Quitting...")
    except error as e:
        print(e)

wrapper(main)
