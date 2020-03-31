CREATE DATABASE IF NOT EXISTS base_peliculas;
#selecionar base de datos
USE base_peliculas;


#crear tablas sin relacion 

CREATE TABLE IF NOT EXISTS idioma(
	id_idioma INT NOT NULL,
    idioma VARCHAR(45) NOT NULL,
    primary key(id_idioma)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS subtitulo(
	id_subtitulo INT NOT NULL,
    subtitulo VARCHAR(45) NOT NULL,
    primary key(id_subtitulo)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS peliculas(
	id_pelicula INT NOT NULL,
	titulo VARCHAR(45) NOT NULL,
	nacionalidad VARCHAR(20),
	idioma VARCHAR(120),
	subtitulos boolean,
	primary key(id_pelicula),
	peliculas_id_idioma INT NOT NULL,
    CONSTRAINT fkpelicula_idioma
    FOREIGN KEY (peliculas_id_idioma)
    REFERENCES idioma(id_idioma),
	peliculas_id_subtitulo INT NOT NULL,
    CONSTRAINT fkpelicula_subtitulo
    FOREIGN KEY (peliculas_id_subtitulo)
    REFERENCES subtitulo(id_subtitulo)
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS actores(
	id_actor INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
    nacionalidad VARCHAR(45) NOT NULL,
    nombre_personaje VARCHAR(45) NOT NULL,
    primary key(id_actor)
)ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS directores(
	id_director INT NOT NULL,
    nombre VARCHAR(45) NOT NULL,
    apellidopat VARCHAR(45) NOT NULL,
    apellidomat VARCHAR(45) NOT NULL,
    fecha_nacimiento DATE,
    pais_origen VARCHAR(120),
    primary key(id_director),
    peliculas_id_pelicula INT NOT NULL,
    CONSTRAINT fkdirector_peliculas
    FOREIGN KEY (peliculas_id_pelicula)
    REFERENCES peliculas(id_pelicula)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS actores_peliculas(
	peliculas_id_pelicula INT NOT NULL,
    actores_id_actor INT NOT NULL,
    PRIMARY KEY(peliculas_id_pelicula, actores_id_actor),
    CONSTRAINT fkactor_peliculas_actor
    FOREIGN KEY (actores_id_actor)
    REFERENCES actores(id_actor),
	CONSTRAINT fkactor_actor_peliculas
    FOREIGN KEY (peliculas_id_pelicula)
    REFERENCES peliculas(id_pelicula)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS generos(
	id_genero INT NOT NULL,
    genero VARCHAR(45) NOT NULL,
    primary key(id_genero)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS generos_peliculas(
	peliculas_id_pelicula INT NOT NULL,
    generos_id_genero INT NOT NULL,
    PRIMARY KEY(peliculas_id_pelicula, generos_id_genero),
    CONSTRAINT fkgeneros_peliculas_genero
    FOREIGN KEY (generos_id_genero)
    REFERENCES generos(id_genero),
	CONSTRAINT fkgenero_genero_peliculas
    FOREIGN KEY (peliculas_id_pelicula)
    REFERENCES peliculas(id_pelicula)
)ENGINE = InnoDB;

