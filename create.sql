create database qual_deputado_votar;

use qual_deputado_votar;

create table partidos (
	partido_id int auto_increment primary key,
    nome_partido varchar(30) not null
);

create table politicos (
	politico_id int auto_increment primary key,
    nome_politico varchar(60) not null,
    foto varchar(256),
    uf char(2) not null,
    esta_em_exercicio bool not null,
    partido_id int not null,
    foreign key(partido_id) references partidos(partido_id)
);

create table tipos_turno (
	tipo_turno_id int auto_increment primary key,
    tipo_turno varchar(15) not null
);

create table status_projetos (
	status_projeto_id int auto_increment primary key,
    status varchar(20) not null
);

create table projetos (
	projeto_id int auto_increment primary key,
    nome_projeto varchar(100) not null,
    data_votacao date not null,
    quorum_minimo int not null,
    resumo varchar(1000) not null,
    link_noticia varchar(1000) not null,
	status_projeto_id int not null,
    tipo_turno_id int not null,
    foreign key(status_projeto_id) references status_projetos(status_projeto_id),
    foreign key(tipo_turno_id) references tipos_turno(tipo_turno_id)
);

create table posicionamentos (
	posicionamento_id int auto_increment primary key,
    posicionamento varchar(15) not null
);

create table votos (
	voto_id int auto_increment primary key,
    posicionamento_id int not null,
    projeto_id int not null,
    politico_id int not null,
    foreign key(posicionamento_id) references posicionamentos(posicionamento_id),
    foreign key(projeto_id) references projetos(projeto_id),
    foreign key(politico_id) references politicos(politico_id)
);
