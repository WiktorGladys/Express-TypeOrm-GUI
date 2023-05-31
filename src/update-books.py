import requests
url = "http://localhost:3000/books/update"
firstUser = input("Enter an Id of book you want update: ")
secUser = input("Enter new Title: ")
myreq = {
    "id":firstUser,
    "title":secUser
}
requests.put(url, json = myreq)