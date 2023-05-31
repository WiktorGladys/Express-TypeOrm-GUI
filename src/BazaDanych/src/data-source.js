"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AppDataSource = void 0;
require("reflect-metadata");
var typeorm_1 = require("typeorm");
var User_1 = require("./entity/User");
var Ksiazka_1 = require("./entity/Ksiazka");
var Wypozyczenia_1 = require("./entity/Wypozyczenia");
exports.AppDataSource = new typeorm_1.DataSource({
    type: "sqlite",
    database: "database.sqlite",
    synchronize: true,
    logging: false,
    entities: [User_1.User, Ksiazka_1.Book, Wypozyczenia_1.Lends],
    migrations: [],
    subscribers: [],
});
