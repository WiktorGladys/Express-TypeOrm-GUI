import "reflect-metadata"
import * as express from "express"
import { Request, Response } from "express"
import {AppDataSource} from "./BazaDanych/src/data-source"
import {User} from "./BazaDanych/src/entity/User"
import { Book } from "./BazaDanych/src/entity/Ksiazka"
import { Lends } from "./BazaDanych/src/entity/Wypozyczenia"
// output format: yyyy-mm-dd
var array: any[] = []
var arrayKeys = []
function push() {
   array.push({
      "value": generateRandomString(20),
      "time": Date.now()
   });
}
function keys(){
    arrayKeys = array.map(function(object){
        return object.value
    })
}
function clearArray(){
        var time = Date.now();
        array = array.filter(function(item) {
           return time < item.time + (5000 * 60 * 5);
        }); 
}
var intervalID = setInterval(clearArray, 5000 * 30);
const getDateInISO_8601 = (): string => {
    const date = new Date();
    const year = '' + date.getFullYear();
    let month = '' + (date.getMonth() + 1);
    let day = '' + date.getDate();
    if (month.length < 2) {
      month = '0' + month;
    }
    if (day.length < 2) {
      day = '0' + day;
    }
    return year + '-' + month + '-' + day;
  };
const generateRandomString = (myLength) => {
    const chars =
      "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890";
    const randomArray = Array.from(
      { length: myLength },
      (v, k) => chars[Math.floor(Math.random() * chars.length)]
    );
  
    const randomString = randomArray.join("");
    return randomString;
  };
function checkingSesion (auth_key){
    if(arrayKeys.find(elem => elem === auth_key))
        return true
    else
        return false
}
const app = express()
app.use(express.json())
AppDataSource.initialize().then(async () => {
    console.log("DataBase is working")

}).catch(error => console.log(error))
const myRepositoryBook = AppDataSource.getRepository(Book)
const myRepositoryUsers = AppDataSource.getRepository(User)
const myRepositoryLends = AppDataSource.getRepository(Lends)
// USERS !!!!!!
app.get("/users", async function (req: Request, res: Response) {
    const users = await myRepositoryUsers.find()
    res.json(users)
})

app.post("/users",  async function (req: Request, res: Response) {
    const data = req.body
    if(checkingSesion(data.auth_key) == true)
    {
        const user = new User()
        user.Username = data.Username
        user.Password = data.Password
        user.firstName = data.firstName
        user.lastName = data.lastName
        const results = await myRepositoryUsers.save(user)
        return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }
   
    
})
// BOOKS !!!!!!
app.get("/books", async function (req: Request, res: Response) {
    const books = await myRepositoryBook.find()
    res.json(books)
})
app.post("/books",  async function (req: Request, res: Response) {
    const data = req.body
    if(checkingSesion(data.auth_key) == true)
    {
       
        const book = new Book()
        book.author = data.author
        book.title = data.title
        const results = await myRepositoryBook.save(book)
        return res.send(results)
    }
    else {
        console.log("ASDASDA")
        return res.sendStatus(405)
    }

})
// LENDS !!!!!!
app.get("/lends", async function (req: Request, res: Response) {
    const lends = await myRepositoryLends.find()
    res.json(lends)
})
app.post("/lends",  async function (req: Request, res: Response) {
    const data = req.body
    if (checkingSesion(data.auth_key) == true)
    {
        
        const user = await myRepositoryUsers.findOneBy({
            id: data.idOfUser
        })
        const book = await myRepositoryBook.findOneBy({
            id: data.idOfBook
        })
        // console.log(user)
        const lend = new Lends()
        const date = new Date(getDateInISO_8601())
        lend.DateOflend = date
        if(book != null){
            lend.book = book
        }
        if(user != null){
            lend.user = user
        }
        const results = await myRepositoryLends.save(lend)
        console.log(results)
        return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }
    
})
// UPDATE USERS !!!!!!
app.put("/users/update/lastname", async function (req: Request, res: Response) {
    const data = req.body
    if (checkingSesion(data.auth_key) == true)
    {
        
        const usertoUpdate = await myRepositoryUsers.findOneBy({
            id: data.id
        })
        if(usertoUpdate != undefined){
             usertoUpdate.lastName = data.lastName
        }
    //    myRepositoryUsers.merge(usertoUpdate!, data.lastName)
       const results = await myRepositoryUsers.save(usertoUpdate!)
       return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }
})
app.put("/users/update/password", async function (req: Request, res: Response) {
    const data = req.body
    if(checkingSesion(data.auth_key) == true)
    {
       
        const usertoUpdate = await myRepositoryUsers.findOneBy({
            id: data.id
        })
        console.log(usertoUpdate)
        if(usertoUpdate != undefined){
             usertoUpdate.Password = data.Password
        }
        
    //    myRepositoryUsers.merge(usertoUpdate!, data.Password)
       const results = await myRepositoryUsers.save(usertoUpdate!)
       console.log(usertoUpdate)
       return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }

})
// UPDATE BOOKS !!!!!!
app.put("/books/update", async function (req: Request, res: Response) {
    const data = req.body
    if (checkingSesion(data.auth_key) == true)
    {
        
        const booktoUpdate = await myRepositoryBook.findOneBy({
            id: data.id
        })
       if(booktoUpdate != undefined){
            booktoUpdate.title = data.title
       }
       const results = await myRepositoryBook.save(booktoUpdate!)
       return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }
  
})
// UPDATE LENDS !!!!!!
app.put("/lends/update", async function (req: Request, res: Response) {
    const data = req.body
    if(checkingSesion(data.auth_key) == true)
    {

        const date = new Date(getDateInISO_8601())
        const lendtoUpdate = await myRepositoryLends.findOneBy({
            id: data.id
        })
        console.log(lendtoUpdate)
        if(lendtoUpdate != undefined){
            lendtoUpdate.DateOfreturn = date
        }
        console.log(lendtoUpdate)
        const results = await myRepositoryLends.save(lendtoUpdate!)
         return res.send(results)
    }
    else{
        return res.sendStatus(405)
    }
    
})

// // DELETE USERS
// app.delete("/users/:id", async function (req: Request, res: Response) {
//     const results = await myRepositoryUsers.delete(req.params.id)
//     return res.send(results)
// })
// // DELETE BOOKS
// app.delete("/books/:id", async function (req: Request, res: Response) {
//     const results = await myRepositoryBook.delete(req.params.id)
//     return res.send(results)
// })
// // DELETE LENDS
// app.delete("/lends/:id", async function (req: Request, res: Response) {
//     const results = await myRepositoryLends.delete(req.params.id)
//     return res.send(results)
// })
//LOGIN USERS
app.get("/login",  async function (req: Request, res: Response) {
    res.send(arrayKeys[arrayKeys.length - 1])
})
app.post("/login",  async function (req: Request, res: Response) {
    const data = req.body
    // global.auth = generateRandomString(20)
    const user = await myRepositoryUsers.findOneBy({
        Username: data.Username,
        Password: data.Password
    })
    console.log(user)
    push()
    console.log(array)
    keys()
    console.log(arrayKeys)
    if(user != null){
        return res.sendStatus(202)
    }
    else {
        return res.sendStatus(404)
    }
    
})
app.listen(3000)