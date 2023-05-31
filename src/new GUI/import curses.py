import curses
from curses import panel
from curses import wrapper
from curses.textpad import Textbox, rectangle


class Menu(object):
    def __init__(self, items, stdscreen,x, y):
        self.window = stdscreen.subwin(x, y)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()

        self.position = 0
        self.items = items
        self.items.append(("exit", "exit"))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items) - 1
    def logowanie(self, stdscr):
     #PANEL LOGOWANIA
        stdscr.clear()
        rectangle(stdscr,0,25,10,85)
        stdscr.addstr(0,52,"Login",curses.A_UNDERLINE)
        stdscr.addstr(6,41,"Enter Username: ", curses.A_STANDOUT)
        win_register = curses.newwin(1,29,8,41)
        box_register = Textbox(win_register)
        rectangle(stdscr,7,40,9,70)
        stdscr.refresh()
        box_register.edit()
        Username = box_register.gather().strip().replace("\n","")
        stdscr.addstr(6,41,"Enter Password: ", curses.A_STANDOUT)
        win_password = curses.newwin(1,29,8,41)
        box_password = Textbox(win_password)
        rectangle(stdscr,7,40,9,70)
        stdscr.refresh()
        box_password.edit()
        Password = box_password.gather().strip().replace("\n","")
        # #REQUEST DO BAZY
        # if Login_request(Username, Password) == True:
        #     pass
        # else:
        #     stdscr.addstr(3,28,"Invalid Password or Username Click Any-key to try again")
        #     stdscr.getkey()
        #     logowanie(stdscr)

    def display(self):
        self.panel.below()
        self.panel.show()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_UNDERLINE
                else:
                    mode = curses.A_NORMAL

                msg = "%d. %s" % (index, item[0])
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.position == len(self.items) - 1:
                    break
                else:
                    self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()


class MyApp(object):
    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        submenu_items = [("ABCDE", submenu.logowanie(stdscreen)), ("flash", curses.flash)]
        submenu = Menu(submenu_items, self.screen, 20 , 20)

        main_menu_items = [
            ("beep", curses.beep),
            ("flash", curses.flash),
            ("submenu", submenu.display),
        ]
        main_menu = Menu(main_menu_items, self.screen, 0, 0)
        # submenu.display()
        while True:
            main_menu.display()


if __name__ == "__main__":
    curses.wrapper(MyApp)