#draw
import curses

# Winner function just displays a user has been tagged
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


def scrnSetup(stdscr: None) -> None:
    # Hide Cursor
    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
    yellow_background   = 2 # Yellow background hurts eyes

    stdscr.bkgd(curses.color_pair(yellow_background))

def printLoc(stdscr, CorY: int, CorX: int, startLoc_y: int, startLoc_x: int) -> None:
    stdscr.addstr(startLoc_y, startLoc_x, 'Y_Cor:{} X_Cor:{}'.format(CorY, CorX))

def printPlayerMove(stdscr, move: int, startLoc_y: int, startLoc_x: int) -> None:
    stdscr.addstr(startLoc_y, startLoc_x, 'Player Move:{}'.format(move))

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
