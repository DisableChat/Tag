#helper


# Grid min and max bounds player can move in grid
MIN_BOUNDS = 0
MAX_BOUNDS = 10


def tag(py1, py2, px1, px2):
    if py1 == py2 and px1 == px2:
        return True
    else:
        return False


##
# Function:     get_directional_input
# Parameters:   loc_y and loc_x are both loaction values on screen
#   value is the value of the getkey() string value of the key input
# Description:  based on the directional input key of the user, increment or
#   deicrement the value and return the new location value.
##
def GPDI_P1(loc_y, loc_x, value) -> int:

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
    elif value == 'KEY_RIGHT':
        if loc_x < MAX_BOUNDS:
            loc_x += 1
        else:
            loc_x
    elif value == "v":
        loc_y = loc_y
        loc_x = loc_x
    return loc_y, loc_x


def GPDI_P2(loc_y, loc_x, value) -> int:

    if value == 'w':
        if loc_y > MIN_BOUNDS:
            loc_y -= 1
        else:
            loc_y
    elif value == 's':
        if loc_y < MAX_BOUNDS:
            loc_y += 1
        else:
            loc_y
    elif value == 'a':
        if loc_x > MIN_BOUNDS:
            loc_x -= 1
        else:
            loc_x
    elif value == 'd':
        if loc_x < MAX_BOUNDS:
            loc_x += 1
        else:
            loc_x
    elif value == "v":
        loc_y = loc_y
        loc_x = loc_x
    return loc_y, loc_x
