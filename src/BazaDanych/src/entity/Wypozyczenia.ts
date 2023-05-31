import "reflect-metadata"
import { Entity, PrimaryGeneratedColumn, Column, ManyToMany, ManyToOne } from "typeorm"
import { User } from "./User"
import { Book } from "./Ksiazka"

@Entity()
export class Lends {

    @PrimaryGeneratedColumn({type: "int"})
    id!: number
    
    @Column("date")
    DateOflend: Date

    @Column("date", {nullable: true})
    DateOfreturn: Date

    @ManyToOne(() => User, (users) => users.LendsUser,{
        eager:true,
        cascade:true,
    })
    user: User

    @ManyToOne(() => Book, (books) => books.LendsBook,{
        eager:true,
        cascade:true,
    })
    book: Book
}