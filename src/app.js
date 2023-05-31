"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
Object.defineProperty(exports, "__esModule", { value: true });
require("reflect-metadata");
var express = require("express");
var data_source_1 = require("./BazaDanych/src/data-source");
var User_1 = require("./BazaDanych/src/entity/User");
var Ksiazka_1 = require("./BazaDanych/src/entity/Ksiazka");
var Wypozyczenia_1 = require("./BazaDanych/src/entity/Wypozyczenia");
// output format: yyyy-mm-dd
var array = [];
var arrayKeys = [];
function push() {
    array.push({
        "value": generateRandomString(20),
        "time": Date.now()
    });
}
function keys() {
    arrayKeys = array.map(function (object) {
        return object.value;
    });
}
function clearArray() {
    var time = Date.now();
    array = array.filter(function (item) {
        return time < item.time + (5000 * 60 * 5);
    });
}
var intervalID = setInterval(clearArray, 5000 * 30);
var getDateInISO_8601 = function () {
    var date = new Date();
    var year = '' + date.getFullYear();
    var month = '' + (date.getMonth() + 1);
    var day = '' + date.getDate();
    if (month.length < 2) {
        month = '0' + month;
    }
    if (day.length < 2) {
        day = '0' + day;
    }
    return year + '-' + month + '-' + day;
};
var generateRandomString = function (myLength) {
    var chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890";
    var randomArray = Array.from({ length: myLength }, function (v, k) { return chars[Math.floor(Math.random() * chars.length)]; });
    var randomString = randomArray.join("");
    return randomString;
};
function checkingSesion(auth_key) {
    if (arrayKeys.find(function (elem) { return elem === auth_key; }))
        return true;
    else
        return false;
}
var app = express();
app.use(express.json());
data_source_1.AppDataSource.initialize().then(function () { return __awaiter(void 0, void 0, void 0, function () {
    return __generator(this, function (_a) {
        console.log("DataBase is working");
        return [2 /*return*/];
    });
}); }).catch(function (error) { return console.log(error); });
var myRepositoryBook = data_source_1.AppDataSource.getRepository(Ksiazka_1.Book);
var myRepositoryUsers = data_source_1.AppDataSource.getRepository(User_1.User);
var myRepositoryLends = data_source_1.AppDataSource.getRepository(Wypozyczenia_1.Lends);
// USERS !!!!!!
app.get("/users", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var users;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, myRepositoryUsers.find()];
                case 1:
                    users = _a.sent();
                    res.json(users);
                    return [2 /*return*/];
            }
        });
    });
});
app.post("/users", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, user, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 2];
                    user = new User_1.User();
                    user.Username = data.Username;
                    user.Password = data.Password;
                    user.firstName = data.firstName;
                    user.lastName = data.lastName;
                    return [4 /*yield*/, myRepositoryUsers.save(user)];
                case 1:
                    results = _a.sent();
                    return [2 /*return*/, res.send(results)];
                case 2: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
// BOOKS !!!!!!
app.get("/books", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var books;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, myRepositoryBook.find()];
                case 1:
                    books = _a.sent();
                    res.json(books);
                    return [2 /*return*/];
            }
        });
    });
});
app.post("/books", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, book, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 2];
                    book = new Ksiazka_1.Book();
                    book.author = data.author;
                    book.title = data.title;
                    return [4 /*yield*/, myRepositoryBook.save(book)];
                case 1:
                    results = _a.sent();
                    return [2 /*return*/, res.send(results)];
                case 2:
                    console.log("ASDASDA");
                    return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
// LENDS !!!!!!
app.get("/lends", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var lends;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0: return [4 /*yield*/, myRepositoryLends.find()];
                case 1:
                    lends = _a.sent();
                    res.json(lends);
                    return [2 /*return*/];
            }
        });
    });
});
app.post("/lends", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, user, book, lend, date, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 4];
                    return [4 /*yield*/, myRepositoryUsers.findOneBy({
                            id: data.idOfUser
                        })];
                case 1:
                    user = _a.sent();
                    return [4 /*yield*/, myRepositoryBook.findOneBy({
                            id: data.idOfBook
                        })
                        // console.log(user)
                    ];
                case 2:
                    book = _a.sent();
                    lend = new Wypozyczenia_1.Lends();
                    date = new Date(getDateInISO_8601());
                    lend.DateOflend = date;
                    if (book != null) {
                        lend.book = book;
                    }
                    if (user != null) {
                        lend.user = user;
                    }
                    return [4 /*yield*/, myRepositoryLends.save(lend)];
                case 3:
                    results = _a.sent();
                    console.log(results);
                    return [2 /*return*/, res.send(results)];
                case 4: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
// UPDATE USERS !!!!!!
app.put("/users/update/lastname", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, usertoUpdate, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 3];
                    return [4 /*yield*/, myRepositoryUsers.findOneBy({
                            id: data.id
                        })];
                case 1:
                    usertoUpdate = _a.sent();
                    if (usertoUpdate != undefined) {
                        usertoUpdate.lastName = data.lastName;
                    }
                    return [4 /*yield*/, myRepositoryUsers.save(usertoUpdate)];
                case 2:
                    results = _a.sent();
                    return [2 /*return*/, res.send(results)];
                case 3: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
app.put("/users/update/password", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, usertoUpdate, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 3];
                    return [4 /*yield*/, myRepositoryUsers.findOneBy({
                            id: data.id
                        })];
                case 1:
                    usertoUpdate = _a.sent();
                    console.log(usertoUpdate);
                    if (usertoUpdate != undefined) {
                        usertoUpdate.Password = data.Password;
                    }
                    return [4 /*yield*/, myRepositoryUsers.save(usertoUpdate)];
                case 2:
                    results = _a.sent();
                    console.log(usertoUpdate);
                    return [2 /*return*/, res.send(results)];
                case 3: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
// UPDATE BOOKS !!!!!!
app.put("/books/update", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, booktoUpdate, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 3];
                    return [4 /*yield*/, myRepositoryBook.findOneBy({
                            id: data.id
                        })];
                case 1:
                    booktoUpdate = _a.sent();
                    if (booktoUpdate != undefined) {
                        booktoUpdate.title = data.title;
                    }
                    return [4 /*yield*/, myRepositoryBook.save(booktoUpdate)];
                case 2:
                    results = _a.sent();
                    return [2 /*return*/, res.send(results)];
                case 3: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
// UPDATE LENDS !!!!!!
app.put("/lends/update", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, date, lendtoUpdate, results;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    if (!(checkingSesion(data.auth_key) == true)) return [3 /*break*/, 3];
                    date = new Date(getDateInISO_8601());
                    return [4 /*yield*/, myRepositoryLends.findOneBy({
                            id: data.id
                        })];
                case 1:
                    lendtoUpdate = _a.sent();
                    console.log(lendtoUpdate);
                    if (lendtoUpdate != undefined) {
                        lendtoUpdate.DateOfreturn = date;
                    }
                    console.log(lendtoUpdate);
                    return [4 /*yield*/, myRepositoryLends.save(lendtoUpdate)];
                case 2:
                    results = _a.sent();
                    return [2 /*return*/, res.send(results)];
                case 3: return [2 /*return*/, res.sendStatus(405)];
            }
        });
    });
});
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
app.get("/login", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        return __generator(this, function (_a) {
            res.send(arrayKeys[arrayKeys.length - 1]);
            return [2 /*return*/];
        });
    });
});
app.post("/login", function (req, res) {
    return __awaiter(this, void 0, void 0, function () {
        var data, user;
        return __generator(this, function (_a) {
            switch (_a.label) {
                case 0:
                    data = req.body;
                    return [4 /*yield*/, myRepositoryUsers.findOneBy({
                            Username: data.Username,
                            Password: data.Password
                        })];
                case 1:
                    user = _a.sent();
                    console.log(user);
                    push();
                    console.log(array);
                    keys();
                    console.log(arrayKeys);
                    if (user != null) {
                        return [2 /*return*/, res.sendStatus(202)];
                    }
                    else {
                        return [2 /*return*/, res.sendStatus(404)];
                    }
                    return [2 /*return*/];
            }
        });
    });
});
app.listen(3000);
