import curses
import requests
import logging
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
def Adding_book_req(Title, Author, stdscr):
     url = "http://localhost:3000/books"
     myreq = {
           "title":Title,
           "author":Author,
           "auth_key":auth
     }
     x = requests.post(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Lending_book_req(idOfBook, idOfUser, stdscr):
     url = "http://localhost:3000/lends"
     myreq = {
          "idOfBook":idOfBook,
          "idOfUser":idOfUser,
          "auth_key":auth
     }
     x = requests.post(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Update_Lends_req(id, stdscr):
     url = "http://localhost:3000/lends/update"
     myreq = {
          "id":id,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Update_Users_lastName_req(id, lastName, stdscr):
     url = "http://localhost:3000/users/update/lastname"
     myreq = {
          "id":id,
          "lastName":lastName,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Update_Books_req(id, title, stdscr):
     url = "http://localhost:3000/books/update"
     myreq = {
          "id":id,
          "title":title,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Update_Users_Password_req(id, Password, stdscr):
     url = "http://localhost:3000/users/update/password"
     myreq = {
          "id":id,
          "Password":Password,
          "auth_key":auth
     }
     x = requests.put(url, json=myreq)
     if x.status_code == 405:
          stdscr.addstr(3,39,"ERROR! Your session has expired!!", curses.A_UNDERLINE)
          stdscr.addstr(4,41,"Press any key to login again", curses.A_UNDERLINE)
          stdscr.getkey()
          logowanie(stdscr)
     else:
          pass
def Register_request(Username, Password, firstName, lastName):
     url = 'http://localhost:3000/users'
     myreq = {
        "firstName": firstName,
        "lastName": lastName,
        "Username":Username,
        "Password":Password
     }
     requests.post(url, json = myreq)
     if requests.Response:
        return True
     else:
         return False
# def getBooks(stdscr):
#      url = "http://localhost:3000/books"
#      respone = requests.get(url)
#      data = respone.json()
#      stdscr.addstr(0,0,data)

def logowanie(stdscr):
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
        #REQUEST DO BAZY
        if Login_request(Username, Password) == True:
            pass
        else:
            stdscr.addstr(3,28,"Invalid Password or Username Click Any-key to try again")
            stdscr.getkey()
            logowanie(stdscr)
        # stdscr.getch()
def main(stdscr):
    while True:
        y, x = stdscr.getmaxyx()
        stdscr.clear()
        curses.resizeterm(y, x)
     #    stdscr.refresh()
     #    stdscr.clear()
     #    stdscr.addstr(0,0,x)
        stdscr.getkey()
        rectangle(stdscr,0,25,10,83)
        stdscr.addstr(0,51,"Welcome",curses.A_UNDERLINE)
        stdscr.addstr(5,28, "Press Left-arrow to login or Right-arrrow to register")
        key = stdscr.getkey()
        if key == "KEY_LEFT":
            logowanie(stdscr)
            break
        elif key == "KEY_RIGHT":
            #PANEL REJESTROWANIA
            stdscr.clear()
            rectangle(stdscr,0,25,10,85)
            stdscr.addstr(0,51,"Register",curses.A_UNDERLINE)
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
            stdscr.addstr(6,41,"Enter firstName: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            firstName = box_register.gather().strip().replace("\n","")
            stdscr.addstr(6,41,"Enter lastName: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            lastName = box_register.gather().strip().replace("\n","")
            Register_request(Username, Password, firstName, lastName)
            logowanie(stdscr)
            break
    # stdscr.clear()
    # stdscr.addstr(0,0,"TEST")
    # stdscr.getch()
    # getBooks(stdscr)
    # # stdscr.addstr(0,0,Books)
    # stdscr.getch()

    while True:
        #GLOWNE MENU
        stdscr.clear()
        rectangle(stdscr,0,25,10,83)
        stdscr.addstr(0,51,"Menu",curses.A_UNDERLINE)
        stdscr.addstr(3,28, "Press Up-arrow to enter Update Menu")
        stdscr.addstr(5,28,"Press Right-arrow to lend a book")
        stdscr.addstr(7,28,"Press Left-arrow to add a book to library")
        key_a = stdscr.getkey()
        if key_a == "KEY_UP":
             
            while True: 
                #MENU UPDATE
                stdscr.clear()
                rectangle(stdscr,0,25,10,83)
                stdscr.addstr(0,48,"Update Menu",curses.A_UNDERLINE)
                stdscr.addstr(2,28, "Press Up-arrow to update a lend")
                stdscr.addstr(4,28,"Press Right-arrow to upadate a user")
                stdscr.addstr(6,28,"Press Left-arrow to update a book")
                stdscr.addstr(8,28,"Press Down-arrow to go back")
                key_b = stdscr.getkey()
                if key_b == "KEY_UP":
                     #UPDATE LENDS
                     stdscr.clear()
                     rectangle(stdscr,0,25,10,83)
                     stdscr.addstr(0,48,"Update Lends",curses.A_UNDERLINE)
                     stdscr.addstr(6,41,"Enter a ID of Lend: ", curses.A_STANDOUT)
                     win_register = curses.newwin(1,29,8,41)
                     box_register = Textbox(win_register)
                     rectangle(stdscr,7,40,9,70)
                     stdscr.refresh()
                     box_register.edit()
                     id = box_register.gather().strip().replace("\n","")
                     Update_Lends_req(id, stdscr)
                elif key_b == "KEY_RIGHT":
                     #MENU UPDATE DO USERS
                     while True:
                        stdscr.clear()
                        rectangle(stdscr,0,25,10,83)
                        stdscr.addstr(0,46,"Update Menu Users",curses.A_UNDERLINE)
                        stdscr.addstr(2,28, "Press Right-arrow to update a Password")
                        stdscr.addstr(4,28,"Press Left-arrow to upadate a lastName")
                        stdscr.addstr(6,28,"Press Down-arrow to go back")
                        key_c = stdscr.getkey()
                        if key_c == "KEY_DOWN":
                             break
                        elif key_c == "KEY_RIGHT":
                             stdscr.clear()
                             rectangle(stdscr,0,25,10,83)
                             stdscr.addstr(0,48,"Update Users Password",curses.A_UNDERLINE)
                             stdscr.addstr(6,41,"Enter a Id of user: ", curses.A_STANDOUT)
                             win_register = curses.newwin(1,29,8,41)
                             box_register = Textbox(win_register)
                             rectangle(stdscr,7,40,9,70)
                             stdscr.refresh()
                             box_register.edit()
                             id = box_register.gather().strip().replace("\n","")
                             stdscr.addstr(6,41,"Enter a new Password: ", curses.A_STANDOUT)
                             win_register = curses.newwin(1,29,8,41)
                             box_register = Textbox(win_register)
                             rectangle(stdscr,7,40,9,70)
                             stdscr.refresh()
                             box_register.edit()
                             Password = box_register.gather().strip().replace("\n","")
                             Update_Users_Password_req(id, Password, stdscr)
                        elif key_c == "KEY_LEFT":
                             stdscr.clear()
                             rectangle(stdscr,0,25,10,83)
                             stdscr.addstr(0,48,"Update Users lastName",curses.A_UNDERLINE)
                             stdscr.addstr(6,41,"Enter a Id of user: ", curses.A_STANDOUT)
                             win_register = curses.newwin(1,29,8,41)
                             box_register = Textbox(win_register)
                             rectangle(stdscr,7,40,9,70)
                             stdscr.refresh()
                             box_register.edit()
                             id = box_register.gather().strip().replace("\n","")
                             stdscr.addstr(6,41,"Enter a new lastName: ", curses.A_STANDOUT)
                             win_register = curses.newwin(1,29,8,41)
                             box_register = Textbox(win_register)
                             rectangle(stdscr,7,40,9,70)
                             stdscr.refresh()
                             box_register.edit()
                             lastName = box_register.gather().strip().replace("\n","")
                             Update_Users_lastName_req(id, lastName, stdscr)
                elif key_b == "KEY_LEFT":
                     #UPDATE BOOKS
                     stdscr.clear()
                     rectangle(stdscr,0,25,10,83)
                     stdscr.addstr(0,48,"Update Book",curses.A_UNDERLINE)
                     stdscr.addstr(6,41,"Enter a ID of book: ", curses.A_STANDOUT)
                     win_register = curses.newwin(1,29,8,41)
                     box_register = Textbox(win_register)
                     rectangle(stdscr,7,40,9,70)
                     stdscr.refresh()
                     box_register.edit()
                     id = box_register.gather().strip().replace("\n","")
                     stdscr.addstr(6,41,"Enter a new Title: ", curses.A_STANDOUT)
                     win_register = curses.newwin(1,29,8,41)
                     box_register = Textbox(win_register)
                     rectangle(stdscr,7,40,9,70)
                     stdscr.refresh()
                     box_register.edit()
                     title = box_register.gather().strip().replace("\n","")
                     Update_Books_req(id, title, stdscr)
                elif key_b == "KEY_DOWN":
                     break
        elif key_a == "KEY_LEFT":
            #DODAWANIE KSIAZKI
            stdscr.clear()
            rectangle(stdscr,0,25,10,83)
            stdscr.addstr(0,48,"Adding book",curses.A_UNDERLINE)
            stdscr.addstr(6,41,"Enter a Title of a book: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            Title = box_register.gather().strip().replace("\n","")
            stdscr.addstr(6,41,"Enter an Author of a book: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            Author = box_register.gather().strip().replace("\n","")
            Adding_book_req(Title, Author, stdscr)
        elif key_a == "KEY_RIGHT":
            #WYPOZYCZENIE
            stdscr.clear()
            rectangle(stdscr,0,25,10,83)
            stdscr.addstr(0,48,"Lending book",curses.A_UNDERLINE)
            stdscr.addstr(6,41,"Enter your ID: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            idOfUser = box_register.gather().strip().replace("\n","")
            stdscr.addstr(6,41,"Enter ID of a book you want to lend: ", curses.A_STANDOUT)
            win_register = curses.newwin(1,29,8,41)
            box_register = Textbox(win_register)
            rectangle(stdscr,7,40,9,70)
            stdscr.refresh()
            box_register.edit()
            idOfBook = box_register.gather().strip().replace("\n","")
            Lending_book_req(idOfBook, idOfUser, stdscr)


wrapper(main)
