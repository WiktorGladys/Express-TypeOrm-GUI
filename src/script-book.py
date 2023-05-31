import requests
url = "http://localhost:3000/books"
firstUser = input("Enter Title: ")
secUser = input("Enter Author: ")
myreq = {
    "title": firstUser,
    "author": secUser
}
x = requests.post(url, json = myreq)
respone = requests.get("http://localhost:3000/login")
data = respone.text
print(data)