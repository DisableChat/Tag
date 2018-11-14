#draw
import curses



# Starting and declaring colors for the program
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

red                 = 1 # Red text with black background
yellow_background   = 2 # Yellow background hurts eyes
blue                = 3 # Blue text black background
default             = 4 # Green text with black background
yellow_text         = 5 # Yellow text with black bacground
cyan_dots           = 6 # Blue dots when race is done


# Winner function just displays a user has been tagged
def winner(stdscr) -> None:
    # Hide Cursor
    curses.curs_set(0)
    while True:

        stdscr.clear()
        for i in range(10):
            stdscr.addstr(i, 0, 'TAG!')
            for k in range(5):
                stdscr.addstr(i, k*4, 'TAG!')

        stdscr.refresh()
