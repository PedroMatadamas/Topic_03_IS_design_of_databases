drop database peliculas_db;
create database if not exists peliculas_db;

use peliculas_db;

create table if not exists directores(
	id_director int not null auto_increment,
    d_nombre varchar(25) not null,
    d_apellidoPat varchar(25) not null,
    d_apellidoMat varchar(25),
    d_nacionalidad varchar(25) not null,
    primary key (id_director)
)engine = InnoDB;

create table if not exists actores(
	id_actor int not null auto_increment,
    a_nombre varchar(25) not null,
    a_apellidoPat varchar(25) not null,
    a_apellidoMat varchar(25),
    a_nacionalidad varchar(25) not null,
    primary key(id_actor)
)engine = InnoDB;


create table if not exists idiomas(
	id_idioma int not null auto_increment,
    idioma varchar(25) not null,
    primary key(id_idioma)
)engine = InnoDB;

create table if not exists subtitulos(
	id_subtitulo int not null,
    substiulo varchar(45) not null,
    primary key(id_subtitulo)
)engine = InnoDB;

create table if not exists titulos(
	titulo varchar(45) not null,   
    tF_publi date not null, #titulo fecha de publicación
    resumen varchar(250) not null,
    primary key(titulo)
)engine = InnoDB;

create table if not exists peliculas(
	id_pelicula int not null auto_increment,
    p_titulo varchar(45),
    idioma int,
    subtitulos int,
    primary key(id_pelicula),
    #Idioma
    constraint fk_idioma foreign key(idioma)
		references idiomas(id_idioma)
        on delete set null
        on update cascade,
	#Subtitulos
    constraint fk_subtitulos foreign key(subtitulos)
		references subtitulos(id_subtitulo)
        on delete set null
        on update cascade,
	#Detalles
    constraint fkp_titulo foreign key(p_titulo)
		references titulos(titulo)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists genero(
	id_genero int not null auto_increment,
    genero varchar(25) not null,
    primary key(id_genero)
)engine = InnoDB;

create table if not exists genpelicula(
	gp_id_genero int not null,
    gp_id_pelicula int not null,
    primary key(gp_id_genero,  gp_id_pelicula),
    constraint fkgp_id_genero foreign key(gp_id_genero)
		references genero(id_genero)
        on update cascade,
        
	constraint fkgp_id_pelicula foreign key(gp_id_pelicula)
		references peliculas(id_pelicula)
        on update cascade
)engine = InnoDB;

create table if not exists dirpeliculas(
	dp_id_director int not null,
    dp_id_pelicula int not null,
    primary key(dp_id_director, dp_id_pelicula),
    constraint fkdp_id_director foreign key(dp_id_director)
		references directores(id_director)
        on update cascade,
	constraint fkdp_id_pelicula foreign key(dp_id_pelicula)
		references peliculas(id_pelicula)
        on update cascade
)engine = InnoDB;

create table if not exists actorpeliculas(
	ap_id_actor int not null,
	ap_id_pelicula int not null,
    primary key(ap_id_actor,  ap_id_pelicula),
	
    constraint fkap_id_pelicula foreign key(ap_id_pelicula)
		references peliculas(id_pelicula)
        on update cascade,
        
	constraint fkap_id_actor foreign key(ap_id_actor)
		references actores(id_actor)
        on update cascade
)engine = InnoDB;
