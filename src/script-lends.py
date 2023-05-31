
import requests
from datetime import date
url = "http://localhost:3000/lends"
firstUser = input("Enter an ID of book: ")
secUser = input("Enter your Id: ")
myreq = {
    "idOfBook":firstUser,
    "idOfUser":secUser
}
requests.post(url, json = myreq)
