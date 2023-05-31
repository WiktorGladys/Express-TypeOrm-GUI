import curses
def mainMenu(root, current_row, h, w):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    main_win = curses.newwin(h - 1, w // 2, 1, 1)
    main_win.border()

    main_options = ["Enter data", "View data", "Exit"]

    for idx, element in enumerate(main_options):
        x = 1 + idx
        y = 1

        if idx == current_row:
            main_win.attron(curses.color_pair(1))
            main_win.addstr(y, x, element)
            main_win.attroff(curses.color_pair(1))
        else:
            main_win.addstr(y, x, element)

    main_win.refresh()

# 2nd window.
def secondMenu(root, current_row, h, w):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    second_win = curses.newwin(h - 1, w // 2, 1, w // 2 + 1)
    second_win.border()

    second_options = ["Option 1", "Option 2", "Option 3"]

    for idx, element in enumerate(second_options):
        x = 1 + idx
        y = 1

        if idx == current_row:
            second_win.attron(curses.color_pair(1))
            second_win.addstr(y, x, element)
            second_win.attroff(curses.color_pair(1))
        else:
            second_win.addstr(y, x, element)

    second_win.refresh()


def main(root):
    curses.curs_set(0)

    h, w = root.getmaxyx()

    current_row = 0

    mainMenu(root, current_row, h, w)

    while True:
        key = root.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 2:
            current_row += 1
        elif key == ord("q"):
            break

        mainMenu(root, current_row, h, w)
        secondMenu(root, current_row, h, w)

    root.refresh()

curses.wrapper(main)