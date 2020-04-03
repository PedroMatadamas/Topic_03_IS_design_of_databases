drop database libreria_db;
create database if not exists libreria_db;

use libreria_db;

create table if not exists cps( #Codigos postales
	cp varchar(6) not null,
    ciudad varchar(45) not null,
	estado varchar(45) not null,
    primary key(cp)
)engine = InnoDB;




create table if not exists autor(
	id_autor int not null auto_increment,
    a_nombre varchar(25) not null,
    a_apellidoPat varchar(25) not null,
    a_apellidoMat varchar(25),
    primary key (id_autor)
)engine = InnoDB;



create table if not exists direccion(
	id_dir int not null auto_increment,
    d_calle varchar(45) not null,
    d_col varchar(45),
    d_numExt varchar(5) not null,
    d_numInt varchar(5),
    d_cp varchar(6),
    primary key(id_dir),
    constraint fkd_cp foreign key(d_cp)
		references cps(cp)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists usuario(
	id_usuario int not null auto_increment,
    u_nombre varchar(25) not null,
    u_apellidopat varchar(25) not null,
    u_apellidomat varchar(25),
    u_tel varchar(10) not null,
    correo varchar(45) not null,
    u_id_dir int,
    primary key(id_usuario),
    constraint fku_id_dir foreign key(u_id_dir)
		references direccion(id_dir)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists prestamo(
	id_prestamo int not null auto_increment,
    pF_prestamo date not null, #Fecha prestamo 
    pF_devolu date not null,   #Fecha devolucion
    p_adeudo float not null,
    p_id_usuario int,
    primary key(id_prestamo),
    constraint fkp_id_usuario foreign key(p_id_usuario)
		references usuario(id_usuario)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists libro(
	id_libro int not null auto_increment,
    l_nombre varchar(50) not null,
    l_cantidad int not null,
    l_edicion varchar(50) not null,
    l_id_autor int,
    primary key(id_libro),
    
    constraint fkl_id_autor foreign key(l_id_autor)
		references autor(id_autor)
        on delete set null
        on update cascade
)engine = InnoDB;

create table if not exists detallesprestamo(
	d_id_prestamo int not null,
    d_id_libro int not null,
    d_cantidad int not null,
    d_adeudoTotal float,
    primary key(d_id_prestamo, d_id_libro),
    constraint fkd_id_prestamo 
    foreign key(d_id_prestamo)
		references prestamo(id_prestamo)
        on update cascade,
	constraint fkd_id_libro foreign key(d_id_libro)
		references libro(id_libro)
        on update cascade
)engine = InnoDB;

