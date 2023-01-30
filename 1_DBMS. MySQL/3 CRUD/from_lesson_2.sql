-- проектирование БД социальной сети
-- DDL = Data Definition Language (язык определения данных)
-- CREATE, ALTER, DROP 

-- CREATE DATABASE vk;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
	id serial primary key,
	firstname varchar(100),
	lastname varchar(100),
	email varchar(100) unique,
	password_hash varchar(100),
	phone int
	-- index users_lastname_firstname_idx(lastname, firstname)
	-- id int unsigned PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE
);

-- индексы - позволяет быстрее искать данные. индексировать стоит те столбцы, по которым будет осущестяляться поиск информации


-- 1 - 1 

--ON DELETE / ON UPDATE 
--NO ACTION
--CASCADE
--RESTRICT +
--SET NULL 
--SET DEFAULT 


drop table if exists profiles;
create table if not exists profiles (
	user_id serial,
	gender char(1),
	birthday date,
	created_at datetime default current_timestamp,
	photo_id bigint unsigned,
	foreign key (user_id) references users(id) on update cascade on delete cascade,
	foreign key (photo_id) references photos(id) on update cascade on delete set null 
);



-- alter table `profiles` add constraint fk_user_id foreign key (user_id) references users(id);
-- 1 - M

drop table if exists messages;
create table if not exists messages(
	id serial primary key,
	body text,
	from_user_id bigint unsigned not null,
	to_user_id bigint unsigned not null,
	created_at datetime default current_timestamp,
	foreign key (from_user_id) references users(id),
	foreign key (to_user_id) references users(id) 
);


drop table if exists friend_requests;
create table if not exists friend_request (
	initiator_user_id bigint unsigned not null,
	target_user_id bigint unsigned not null,
	requested_at datetime default current_timestamp,
	updated_at datetime default current_timestamp,
	status varchar(10) check(status in ('requested', 'approved', 'declined', 'unfriended')),
	primary key (initiator_user_id, target_user_id),
	foreign key (initiator_user_id) references users(id),
	foreign key (target_user_id) references users(id) 
);

drop table if exists communities;
create table if not exists communities(
	id serial primary key,
	name varchar(150)
	-- index communities_name_idx(name)
);

-- M - M

drop table if exists users_communities;
create table users_communities (
	user_id bigint unsigned not null,
	community_id bigint unsigned not null,
	primary key (user_id, community_id), -- чтобы не было двух записей о пользователе и сообществе
	foreign key (user_id) references users(id),
	foreign key (community_id) references communities(id)
);


drop table if exists media_types;
create table if not exists media_types (
	id serial primary key,
	name varchar(255)
);


drop table if exists media;
create table if not exists media(
	id serial primary key,
	user_id bigint unsigned not null,
	media_type_id bigint unsigned,
	body text,
	--file blob,
	-- metadata json,
	 
	filename varchar(255),
	created_at datetime default current_timestamp,
	updated_at datetime default current_timestamp,
	foreign key (user_id) references users(id),
	foreign key (media_type_id) references media_types(id) on update cascade on delete set null
);


drop table if exists likes;
create table if not exists likes (
	id serial primary key,
	user_id bigint unsigned not null,
	media_id bigint unsigned not null,
	created_at datetime default current_timestamp,
	foreign key (user_id) references users(id),
	foreign key (media_id) references media(id)
);

drop table if exists photo_albums;
create table if not exists photo_albums (
	id serial primary key,
	name varchar(255) default null,
	user_id bigint unsigned default null,
	foreign key (user_id) references users(id)
);

drop table if exists photos;
create table if not exists photos (
	id serial primary key,
	album_id bigint unsigned not null,
	photo_id bigint unsigned not null,
	foreign key (album_id) references photo_albums(id),
	foreign key (photo_id) references media(id) 
	
)

