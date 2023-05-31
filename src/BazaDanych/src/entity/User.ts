import "reflect-metadata"
import { Entity, PrimaryGeneratedColumn, Column, OneToMany } from "typeorm"
import { Lends } from "./Wypozyczenia"

@Entity()
export class User {

    @PrimaryGeneratedColumn({type: "int"})
    id!: number

    @Column("varchar", {length: 100})
    firstName: string

    @Column("varchar", {length: 100})
    lastName: string

    @Column("varchar", {length: 100})
    Username: string
    
    @Column("varchar", {length: 100})
    Password: string
    
    
    @OneToMany(() => Lends, (wypo) => wypo.user)
    LendsUser: Lends[]
}
