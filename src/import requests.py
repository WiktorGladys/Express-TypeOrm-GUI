import requests
url = "http://localhost:3000/login"
login = input("Login: ")
password = input("password: ")
myreq = {
     "Username":login,
    "Password":password
}
requests.post(url, json = myreq)
if requests.Response:
     print('Success!')
else:
    print('An error has occurred.')