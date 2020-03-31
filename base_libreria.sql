#DROP database libreria;
CREATE DATABASE IF NOT EXISTS libreria;
use libreria;

CREATE TABLE IF NOT EXISTS codp(
	cp INT NOT NULL,
    ciudad VARCHAR(45) NOT NULL,
	estado VARCHAR(45) NOT NULL,
    primary key(cp)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS autor(
	id_autor INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
	primary key(id_autor)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS direccion(
	id_direccion INT NOT NULL,
    calle VARCHAR(45) NOT NULL,
    numInt INT NOT NULL, 
    numExt INT NOT NULL, 
    primary key(id_direccion),
	cp_lug INT NOT NULL,
    CONSTRAINT cp_lugar
    FOREIGN KEY (cp_lug)
    REFERENCES codp(cp)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS usuario(
	id_usuario INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
    telefono INT NOT NULL,  
    correo VARCHAR(45) NOT NULL,
	direccion INT NOT NULL,
    CONSTRAINT fkusuario_direccion
    FOREIGN KEY (direccion)
    REFERENCES direccion(id_direccion),
    primary key(id_usuario)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS libro(
	id_libro INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
	cantidad INT NOT NULL,  
    edicion INT NOT NULL,  
	libro_autor INT NOT NULL,
    CONSTRAINT fklibro_autor
    FOREIGN KEY (libro_autor)
    REFERENCES autor(id_autor),
    primary key(id_libro)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS prestamo(
	id_prestamo INT NOT NULL,
	prestamo_usuario INT NOT NULL,
    CONSTRAINT fk_prestamo_usuario
    FOREIGN KEY (prestamo_usuario)
    REFERENCES usuario(id_usuario),
    prestamo_libro INT NOT NULL,
	CONSTRAINT fkprestamo_libro
    FOREIGN KEY (prestamo_libro)
    REFERENCES libro(id_libro),
	fecha_prestamo date NOT NULL, 
    fecha_devolucion date NOT NULL, 
    adeudo INT NOT NULL,
    estatus VARCHAR(45) NOT NULL,
    primary key(id_prestamo)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS detalles_prestamo(
	detalles_prestamos INT NOT NULL,
    detalles_libro INT NOT NULL,
    PRIMARY KEY(detalles_prestamos,  detalles_libro),
    CONSTRAINT fkdetalles_prestamos
    FOREIGN KEY (detalles_prestamos)
    REFERENCES prestamos(id_prestamo),
	CONSTRAINT fkdetalles_libro
    FOREIGN KEY (detalles_libro)
    REFERENCES libros(id_libro),
	cantidad INT NOT NULL,
	adeudo_total INT NOT NULL
)ENGINE = InnoDB;
