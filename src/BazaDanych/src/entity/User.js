"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.User = void 0;
require("reflect-metadata");
var typeorm_1 = require("typeorm");
var Wypozyczenia_1 = require("./Wypozyczenia");
var User = exports.User = /** @class */ (function () {
    function User() {
    }
    __decorate([
        (0, typeorm_1.PrimaryGeneratedColumn)({ type: "int" })
    ], User.prototype, "id", void 0);
    __decorate([
        (0, typeorm_1.Column)("varchar", { length: 100 })
    ], User.prototype, "firstName", void 0);
    __decorate([
        (0, typeorm_1.Column)("varchar", { length: 100 })
    ], User.prototype, "lastName", void 0);
    __decorate([
        (0, typeorm_1.Column)("varchar", { length: 100 })
    ], User.prototype, "Username", void 0);
    __decorate([
        (0, typeorm_1.Column)("varchar", { length: 100 })
    ], User.prototype, "Password", void 0);
    __decorate([
        (0, typeorm_1.OneToMany)(function () { return Wypozyczenia_1.Lends; }, function (wypo) { return wypo.user; })
    ], User.prototype, "LendsUser", void 0);
    User = __decorate([
        (0, typeorm_1.Entity)()
    ], User);
    return User;
}());
