### mechanic.py ###

##***NOTE/TODO***##
# The GPDI_P1 and GPDI_P2 logic for key pressing and keeping inside bounds
# of the game can be simplified. By using the "validSpace" function.
# I just need to input the locations of all #'s (boundries) into an array
# and simply check if that location is a location that a player is attempting
# to move into, if so then return FALSE
# However, this can be a ticket for later.
##

# Grid min and max bounds player can move in grid
MIN_BOUNDS = 1
MAX_BOUNDS_X = 35
MAX_BOUNDS_Y = 25

##
# Func:         tags
# Param:        py1: int, y location of player 1
#               py2: int, y location of player 2
#               px1: int, x location of player 1
#               px2: int, x location of player 2
# Description:  checks the location values of player 1 and player 2.
#               If collision then there is a "tag"
##
def tag(py1: int, py2: int, px1: int, px2: int) -> bool:
    if py1 == py2 and px1 == px2:
        return True
    else:
        return False

##
# Func:         GPDI_P1
# Param:        loc_y: int, y location of player 1
#               loc_x: int, x location of player 1
#               value: int, the key value that was inputed by user
# Description:  Keyboard input logic, which limits user to staying within
#               bounds of the game
##
def GPDI_P1(loc_y: int, loc_x: int, value: int) -> int:

    tmpY = loc_y
    tmpX = loc_x

    if value == 'KEY_UP':
        if loc_y > MIN_BOUNDS:
            loc_y -= 1
        else:
            loc_y
    elif value == 'KEY_DOWN':
        if loc_y < MAX_BOUNDS_Y - 1:
            loc_y += 1
        else:
            loc_y
    elif value == 'KEY_LEFT':
        if loc_x > MIN_BOUNDS:
            loc_x -= 1
        else:
            loc_x
    elif value == 'KEY_RIGHT':
        if loc_x < MAX_BOUNDS_X - 1:
            loc_x += 1
        else:
            loc_x
    elif value == "v":
        loc_y = loc_y
        loc_x = loc_x

    # implmentation for the "terain" or map for game so players can't go
    # through the terrain in map
    if validSpace(loc_y, loc_x) == False:
        loc_y = tmpY
        loc_x = tmpX

    return loc_y, loc_x

##
# Func:         GPDI_P2
# Param:        loc_y: int, y location of player 2
#               loc_x: int, x location of player 2
#               value: int, the key value that was inputed by user
# Description:  Keyboard input logic, which limits user to staying within
#               bounds of the game
##
def GPDI_P2(loc_y: int, loc_x: int, value: int) -> int:

    tmpY = loc_y
    tmpX = loc_x

    if value == 'w':
        if loc_y > MIN_BOUNDS:
            loc_y -= 1
        else:
            loc_y
    elif value == 's':
        if loc_y < MAX_BOUNDS_Y - 1:
            loc_y += 1
        else:
            loc_y
    elif value == 'a':
        if loc_x > MIN_BOUNDS:
            loc_x -= 1
        else:
            loc_x
    elif value == 'd':
        if loc_x < MAX_BOUNDS_X - 1:
            loc_x += 1
        else:
            loc_x
    elif value == "v":
        loc_y = loc_y
        loc_x = loc_x

    # implmentation for the "terain" or map for game so players can't go
    # through the terrain in map
    if validSpace(loc_y, loc_x) == False:
        loc_y = tmpY
        loc_x = tmpX

    return loc_y, loc_x

##
# Func:         validSpace
# Param:        loc_y: int, y location of player
#               loc_x: int, x location of player
# Description:  Keyboard input logic, which limits user to staying within
#               bounds of the game
##
def validSpace(loc_y: int, loc_x: int) -> bool:

    # Top left block
    for i in range(5):
        for j in range(5):
            if loc_y == i and loc_x == j:
                return False

    # Bottom right block
    for i in range(18, 25, 1):
        for j in range(20, 35, 1):
            if loc_y == i and loc_x == j:
                return False

    # Top right small & block
    for i in range(3, 5, 1):
        for j in range(18, 21, 1):
            if loc_y == i and loc_x == j:
                return False

    # top right larger & block
    for i in range(3, 5, 1):
        for j in range(24, 29, 1):
            if loc_y == i and loc_x == j:
                return False

    for i in range(5, 10, 1):
        if loc_y == i and loc_x == i:
            return False

    for i in range(4, 9, 1):
        if loc_y == i + 1 and loc_x == i:
            return False

    for i in range(3, 8, 1):
        if loc_y == i + 2 and loc_x == i:
            return False

    for i in range(2, 7, 1):
        if loc_y == i + 3 and loc_x == i:
            return False

    for i in range(1, 6, 1):
        if loc_y == i + 4 and loc_x == i:
            return False
