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
     pass
def main(stdscr):
   pass

wrapper(main)
