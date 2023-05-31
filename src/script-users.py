import requests

url = 'http://localhost:3000/users'
fistUser = input("Enter firstName: ")
lastUser = input("Enter lastName: ")
thirdUser = input("Enter Username: ")
fourthUser = input("Enter Password: ")
myreq = {
    "firstName": fistUser,
    "lastName": lastUser,
    "Username":thirdUser,
    "Password":fourthUser
}
requests.post(url, json = myreq)
response = requests.get(url)
response.raise_for_status()
data = response.json()
print(data)
