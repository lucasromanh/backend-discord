CREATE DATABASE discord;

USE discord;

-- Creación de la tabla "Usuarios"
CREATE TABLE Usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE,
    ruta_imagen_perfil VARCHAR(100)
);

-- Creación de la tabla "Servidores"
CREATE TABLE Servidores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    fecha_creacion DATE
);

-- Creación de la tabla "MiembrosServidores"
CREATE TABLE MiembrosServidores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_servidor INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_servidor) REFERENCES Servidores(id)
);

-- Creación de la tabla "Canales"
CREATE TABLE Canales (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    id_servidor INT,
    FOREIGN KEY (id_servidor) REFERENCES Servidores(id)
);

-- Creación de la tabla "Mensajes"
CREATE TABLE Mensajes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    contenido TEXT,
    fecha_envio DATETIME,
    id_usuario INT,
    id_canal INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id),
    FOREIGN KEY (id_canal) REFERENCES Canales(id)
);
