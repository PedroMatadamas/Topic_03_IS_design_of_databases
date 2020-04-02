
CREATE DATABASE IF NOT EXISTS tienda;
use tienda;

CREATE TABLE IF NOT EXISTS codp(
	cp INT NOT NULL,
    ciudad VARCHAR(45) NOT NULL,
	estado VARCHAR(45) NOT NULL,
    primary key(cp)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS cliente(
	id_cliente INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
    calle VARCHAR(45) NOT NULL,
    NoExt VARCHAR(45) NOT NULL,
    NoInt VARCHAR(45),
    colonia VARCHAR(45),
    telefono VARCHAR(45),  
    correo VARCHAR(45) ,
	cp_lug VARCHAR(45),
    CONSTRAINT cp_lugar
    FOREIGN KEY (cp_lug)
    REFERENCES codp(cp)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
    primary key(id_cliente)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS producto(
	id_producto INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
	descripcion VARCHAR(45) NOT NULL,
    precio INT NOT NULL, 
    primary key(id_producto)
)ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS orden(
	id_orden INT NOT NULL,
	orden_cliente INT NOT NULL,
    CONSTRAINT fkorden_cliente_orden
    FOREIGN KEY (orden_cliente)
    REFERENCES cliente(id_cliente)
	ON DELETE SET NULL
    ON UPDATE CASCADE,
    orden_producto INT NOT NULL,
	CONSTRAINT fkorden_producto_orden
    FOREIGN KEY (orden_producto)
    REFERENCES producto(id_producto)
	ON DELETE SET NULL
    ON UPDATE CASCADE,
	dia INT NOT NULL,
	mes INT NOT NULL,
	año INT NOT NULL,
    total INT NOT NULL,
    estatus VARCHAR(45) NOT NULL,
    primary key(id_orden)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS detalles(
	detalles_orden INT NOT NULL,
    detalles_procucto INT NOT NULL,
    PRIMARY KEY(detalles_orden, detalles_procucto),
    CONSTRAINT fkdetalles_detalles_orden
    FOREIGN KEY (detalles_orden)
    REFERENCES orden(id_orden)
	ON DELETE SET NULL
    ON UPDATE CASCADE,
	CONSTRAINT fkdetalles_detalles_procucto
    FOREIGN KEY (detalles_procucto)
    REFERENCES producto(id_producto)
	ON DELETE SET NULL
    ON UPDATE CASCADE,
	cantidad INT NOT NULL,
	total_productos INT NOT NULL
)ENGINE = InnoDB;