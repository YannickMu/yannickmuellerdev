/*
This SQL-Script is for the Database of yannickmueller.dev.
DBMS: mariadb
ENGINE: InnoDB
Author: Yannick Müller
*/

DROP DATABASE IF EXISTS App;
CREATE DATABASE App;
USE App;

CREATE TABLE Login (
    id_User INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL UNIQUE,
    fname VARCHAR(20) NOT NULL,
    lname VARCHAR(25) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(17),
    password VARCHAR(250) NOT NULL,
    salt VARCHAR(8) NOT NULL,
    PRIMARY KEY(id_User)
)ENGINE = InnoDB;

CREATE TABLE ToDo (
    id_ToDo INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(25) NOT NULL,
    description VARCHAR(200),
    checked BOOLEAN NOT NULL DEFAULT FALSE,
    fk_User INT NOT NULL,
    PRIMARY KEY(id_ToDo),
    FOREIGN KEY(fk_User) REFERENCES Login(id_User)
)ENGINE = InnoDB;
