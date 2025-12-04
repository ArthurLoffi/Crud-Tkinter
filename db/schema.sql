CREATE DATABASE crud_tkinter;

CREATE TABLE usuarios(
    id int primary key auto_increment,
    email VARCHAR(200) NOT NULL,
    user VARCHAR(255) NOT NULL
);