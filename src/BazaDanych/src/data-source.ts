import "reflect-metadata"
import { DataSource } from "typeorm"
import { User } from "./entity/User"
import { Book } from "./entity/Ksiazka"
import { Lends } from "./entity/Wypozyczenia"

export const AppDataSource = new DataSource({
    type: "sqlite",
    database: "database.sqlite",
    synchronize: true,
    logging: false,
    entities: [User, Book, Lends],
    migrations: [],
    subscribers: [],
})
