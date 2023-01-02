use gb_sql;

create table if not exists users (
	id SERIAL auto_increment,
	name varchar(50) not null default 'empty'
);



