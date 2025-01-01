
import curses
def main(stdscr):
    curses.start_color()  # Bắt đầu sử dụng màu
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr(0, 0, "Hello, welcome to student system( Enter to continue)!", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()


curses.wrapper(main)