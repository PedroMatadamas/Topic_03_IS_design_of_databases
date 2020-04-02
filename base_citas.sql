CREATE DATABASE IF NOT EXISTS cita;
USE cita;

CREATE TABLE IF NOT EXISTS contacto(
	id_contacto INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
    correo VARCHAR(45) NOT NULL,
    ntelefono VARCHAR(45),
    primary key(id_contacto)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS codp(
	cp INT NOT NULL,
    ciudad VARCHAR(45) NOT NULL,
	estado VARCHAR(45) NOT NULL,
    primary key(cp)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS lugar(
	id_lugar INT NOT NULL,
    num_ext INT NOT NULL,
    num_int INT NOT NULL,
	colonia VARCHAR(45) NOT NULL,
	calle VARCHAR(45) NOT NULL,
    primary key(id_lugar),
	cp_lug INT NOT NULL,
    CONSTRAINT cp_lugar
    FOREIGN KEY (cp_lug)
    REFERENCES codp(cp)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS cita(
	id_cita INT NOT NULL,
	dia INT NOT NULL,
	mes INT NOT NULL,
	año INT NOT NULL,
	hora TIME,
	asunto VARCHAR(45) NOT NULL,
    primary key(id_cita),
	lugar_cita INT NOT NULL,
    CONSTRAINT lugar_cita
    FOREIGN KEY (lugar_cita)
    REFERENCES lugar(id_lugar)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS citas(
	contacto_citas INT NOT NULL,
    cita_citas INT NOT NULL,
    PRIMARY KEY(contacto_citas, cita_citas),
    CONSTRAINT fkcitas_contacto_citas
    FOREIGN KEY (contacto_citas)
    REFERENCES contacto(id_contacto),
	CONSTRAINT fkcitas_cita_citas
    FOREIGN KEY (cita_citas)
    REFERENCES cita(id_cita)
)ENGINE = InnoDB;

