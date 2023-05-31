import requests
#import datetime
from datetime import date
#from datetime import datetime
#from dateutil import parser
url = "http://localhost:3000/lends/update"
secUser = input("Enter Id of Lends you want to return: ")
#firstUser = "12/10/23"
#datetime_object = datetime.strptime(firstUser,'%d/%m/%y')
#d = date.fromisoformat(firstUser)
myreq = {
    "id":secUser
}
requests.put(url, myreq)
