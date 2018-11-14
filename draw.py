#draw
import curses

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
