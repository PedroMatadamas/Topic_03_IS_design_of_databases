create database if not exists agenda_db;

use agenda_db;

create table if not exists contacto(
	id_contacto int not null auto_increment,
    nombre varchar(45) not  null,
    apellidopat varchar(45) not null,
    apellidomat varchar(45),
    correo varchar(45) not null,
    ntelefono varchar(10),
    primary key(id_contacto)
)engine = InnoDB;

create table if not exists cps( #Codigos postales
	cp int not null,
    ciudad varchar(45) not null,
	estado varchar(45) not null,
    primary key(cp)
)engine = InnoDB;

create table if not exists lugar(
	id_lugar int not null auto_increment,
    num_ext varchar(5) not null,
    num_int varchar(5),
	colonia varchar(45),
	calle varchar(45) NOT NULL,
    l_cp int,
    primary key(id_lugar),
	constraint fkcp_lug foreign key(l_cp)
		references cps(cp)
        on delete set null
        on update cascade
)ENGINE = InnoDB;

create table if not exists cita(
	id_cita int not null auto_increment,
	fecha date not null,
	hora time not null,
	asunto varchar(45) not null,
    c_id_lugar int,
    primary key(id_cita),
	constraint fkc_lug foreign key(c_id_lugar)
		references lugar(id_lugar)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists citas(
	id_contacto_citas int not null,
    id_cita_citas int not null,
    primary key(id_contacto_citas, id_cita_citas),
    
    constraint fk_contacto_citas foreign key(id_contacto_citas)
		references contacto(id_contacto)
        on update cascade,
	constraint fk_cita_citas foreign key(id_cita_citas)
		references cita(id_cita)
        on update cascade
)engine = InnoDB;