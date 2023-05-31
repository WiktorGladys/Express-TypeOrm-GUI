import "reflect-metadata"
import { Entity, PrimaryGeneratedColumn, Column, OneToMany } from "typeorm"
import { Lends} from "./Wypozyczenia"

@Entity()
export class Book {

    @PrimaryGeneratedColumn({type: "int"})
    id!: number

    @Column("varchar", {length: 100})
    title: string

    @Column("varchar", {length: 100})
    author: string

    @OneToMany(() => Lends, (wypo) => wypo.book)
    LendsBook: Lends[]
}