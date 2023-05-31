import curses
import requests
from curses import wrapper
from curses.textpad import Textbox, rectangle
def Login_request(login, password):
        global auth
        url = "http://localhost:3000/login"
        myreq = {
              "Username":login,
              "Password":password
        }
        x = requests.post(url, json = myreq)
        response = requests.get(url)
        auth = response.text
        if x.status_code == 202 :
            return True
        else:
            return False
def Register_request(Username, Password, firstName, lastName):
     url = 'http://localhost:3000/users'
     myreq = {
        "firstName": firstName,
        "lastName": lastName,
        "Username":Username,
        "Password":Password
     }
     requests.post(url, json = myreq)
def Update_Users_Password_req(id, Password):
     url = "http://localhost:3000/users/update/password"
     myreq = {
          "id":id,
          "Password":Password,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
def Update_Users_lastName_req(id, lastName):
     url = "http://localhost:3000/users/update/lastname"
     myreq = {
          "id":id,
          "lastName":lastName,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
def Adding_Books_req(Title, Author):
     url = "http://localhost:3000/books"
     myreq = {
           "title":Title,
           "author":Author,
           "auth_key":auth
     }
     x = requests.post(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
def Update_Books_req(id, title):
     url = "http://localhost:3000/books/update"
     myreq = {
          "id":id,
          "title":title,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
def Lending_book_req(idOfBook, idOfUser):
     url = "http://localhost:3000/lends"
     myreq = {
          "idOfBook":idOfBook,
          "idOfUser":idOfUser,
          "auth_key":auth
     }
     x = requests.post(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
def Update_Lends_req(id):
     url = "http://localhost:3000/lends/update"
     myreq = {
          "id":id,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          return True
     else:
          return False
class MenuDisplay:

    def __init__(self, menu):
        # set menu parameter as class property
        self.menu = menu
        # run curses application
        curses.wrapper(self.mainloop)

    def mainloop(self, stdscr):
        # turn off cursor blinking
        curses.curs_set(0)

        # color scheme for selected row
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # set screen object as class property
        self.stdscr = stdscr

        # get screen height and width
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()

        # specify the current selected row
        current_row = 0

        # print the menu
        self.print_menu(current_row)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(self.menu) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.menu[current_row] == "Log in":
                    self.login()
                    break
                elif self.menu[current_row] == "Register":
                    self.register()
                elif self.menu[current_row] == "Users":
                    MenuDisplay(menu_users)
                elif self.menu[current_row] == "Back":
                    MenuDisplay(menu)
                elif self.menu[current_row] == "Update User's Password":
                    self.Update_Users_Password()
                elif self.menu[current_row] == "Update User's lastName":
                    self.Update_Users_lastName()
                elif self.menu[current_row] == "Lends":
                    MenuDisplay(menu_lends)
                elif self.menu[current_row] == "Create new Lend":
                    self.Lending_Books()
                elif self.menu[current_row] == "Update Lend":
                    self.Update_Lends()
                elif self.menu[current_row] == "Books":
                    MenuDisplay(menu_books)
                elif self.menu[current_row] == "Add Book":
                    self.Adding_Books()
                elif self.menu[current_row] == "Update Book":
                    self.Update_Books()
                # self.print_center(self.menu[current_row])
                # self.stdscr.getch()
                # if user selected last row (Exit), confirm before exit the program
                if current_row == len(self.menu) - 1:
                    if self.confirm("Are you sure you want to exit?"):
                        break

            self.print_menu(current_row)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        for idx, row in enumerate(self.menu):
            x = self.screen_width // 2 - len(row) // 2 
            y = self.screen_height // 2 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.color_print(y, x, row, 1)
            else:
                self.stdscr.addstr(y, x+1, row)
        self.stdscr.refresh()

    def color_print(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))
    def login(self):
     #PANEL LOGOWANIA
        self.stdscr.clear()
        Username = self.print_Input_box("Enter Username:")
        Password = self.print_Input_box("Enter Password:")
        if Login_request(Username, Password) == True:
            self.print_center("Succesfully logined!")
            curses.napms(500)
            MenuDisplay(menu)
        else:
            self.print_center_ERROR("Invalid Username or Password!")
            self.stdscr.getkey()
            self.login()
    def register(self):
        self.stdscr.clear()
        Username = self.print_Input_box("Enter Username:")
        Password = self.print_Input_box("Enter Password:")
        firstName = self.print_Input_box("Enter firstName:")
        lastName = self.print_Input_box("Enter lastName:")
        Register_request(Username,Password,firstName,lastName)
        self.print_center("Succesfully Registered!")
        curses.napms(500)
    def Update_Users_Password(self):
        self.stdscr.clear()
        Id = self.print_Input_box("Enter ID:")
        Password = self.print_Input_box("Enter new Password:")
        if Update_Users_Password_req(Id, Password) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
    def Update_Users_lastName(self):
        self.stdscr.clear()
        Id = self.print_Input_box("Enter ID:")
        lastName = self.print_Input_box("Enter new lastName:")
        if Update_Users_lastName_req(Id, lastName) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
    def Adding_Books(self):
        self.stdscr.clear()
        Author = self.print_Input_box("Enter Author:")
        Title = self.print_Input_box("Enter Title:")
        self.print_center(Title)
        self.stdscr.getkey()
        if Adding_Books_req(Author, Title) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
    def Update_Books(self):
        self.stdscr.clear()
        Id = self.print_Input_box("Enter ID:")
        Title = self.print_Input_box("Enter new Title:")
        if Update_Books_req(Id, Title) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
    def Lending_Books(self):
        self.stdscr.clear()
        idOfBook = self.print_Input_box("Enter Book's ID:")
        idOfUser = self.print_Input_box("Enter User's ID:")
        if Lending_book_req(idOfBook, idOfUser) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
    def Update_Lends(self):
        self.stdscr.clear()
        Id = self.print_Input_box("Enter Id:")
        if Update_Lends_req(Id) != True:
            self.print_center("Succes")
            curses.napms(600)
        else:
            self.print_center_ERROR("Your session has expired! Please Login Again!")
            curses.napms(600)
            self.login()
            
    def print_confirm(self, selected="yes"):
        # clear yes/no line
        curses.setsyx(self.screen_height // 2 + 1, 0)
        self.stdscr.clrtoeol()

        y = self.screen_height // 2 + 1
        options_width = 10

        # print yes
        option = "yes"
        x = self.screen_width // 2 - options_width // 2 + len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        # print no
        option = "no"
        x = self.screen_width // 2 + options_width // 2 - len(option)
        if selected == option:
            self.color_print(y, x, option, 1)
        else:
            self.stdscr.addstr(y, x, option)

        self.stdscr.refresh()

    def confirm(self, confirmation_text):
        self.print_center(confirmation_text)

        current_option = "yes"
        self.print_confirm(current_option)

        while 1:
            key = self.stdscr.getch()

            if key == curses.KEY_RIGHT and current_option == "yes":
                current_option = "no"
            elif key == curses.KEY_LEFT and current_option == "no":
                current_option = "yes"
            elif key == curses.KEY_ENTER or key in [10, 13]:
                return True if current_option == "yes" else False

            self.print_confirm(current_option)

    def print_center(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()
   
    def print_Input_box(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y-4, x, text, curses.A_REVERSE)
        rectangle(self.stdscr,y-3,x-3,y-1,x+19)
        self.stdscr.refresh()
        self.win = curses.newwin(1,21,y-2,x-2)
        self.box = Textbox(self.win)
        self.stdscr.refresh()
        self.box.edit()
        variable = self.box.gather().strip().replace("\n","")
        return variable
    
    def print_center_ERROR(self, text):
        self.stdscr.clear()
        x = self.screen_width // 2 - len(text) // 2
        y = self.screen_height // 2
        self.stdscr.addstr(y, x, text,curses.A_STANDOUT)
        self.stdscr.refresh()


if __name__ == "__main__":
    menu_session_start = ['Log in', 'Register','Exit']
    menu = ['Users', 'Books', 'Lends', 'Exit']
    menu_users = ["Update User's Password","Update User's lastName","Back" ,"Exit" ]
    menu_books = ['Add Book', "Update Book","Back", "Exit"]
    menu_lends = ["Create new Lend", "Update Lend", "Back", "Exit"]
    MenuDisplay(menu_session_start)
