import requests
url = "http://localhost:3000/users/update"
firstUser = input("Enter an Id of user you want update: ")
secUser = input("Enter new lastName: ")
myreq = {
    "id":firstUser,
    "name":secUser
}
requests.put(url, json=myreq)