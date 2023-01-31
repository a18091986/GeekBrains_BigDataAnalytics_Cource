-------------------------------------------ВИДЕО--------------------------------------------

select * from users;

-- арифметические операторы 
-- + - * / % DIV

-- beetwen, not between, 

-- in (1,2,3....)

-- like % - любое количество символов, _ - ровно один символ

-- rlike, regexp - поиск с помощью регулярных выражений

-- запрос выводит данные в том порядке, в котором они храняться в БД, но БД не гарантирует хранение в порядке добавления

-- order by - asc - прямой порядок, desc - обратный порядок

-- limit 2,4 (limit 2 offset 4)

-- select distinct

-- group by

-- предопределенные функции mysql 
-- DATE(), NOW(), DATE_FORMAT(), UNIX_TIMESTAMP(), FROM_UNIXTIME(), TO_DAYS()
-- FLOOR,  
-- TIMESTAMPDIFF(YEAR, datetime column, now())
-- select * from users order by rand();
-- математические функции: rand(), sqrt(), sin(), round(...., 4), floor, ceiling,
-- строковые функции substring(str, 1, 4), concat(), 
-- if (условие, 'var_1', 'var_2')
-- case

-- GROUP BY, GROUP_CONCAT(column separator ' '), 
-- Агрегационные функции count, min, max, mean,  
-- having - аналогично where для group BY 
-- WITH ROLLUP 

select * from users;

select substring(lastname, 1, 3) as first_3, count() from users group by first_3;-- with ROLLUP;

select lastname, count(), GROUP_concat(lastname) as total from users group by (substring(lastname, 1, 2)) ;


create table tbl (x int, y int, summ int as (x+y) stored);
insert into tbl (x, y) values (10,20),(30,40);
select * from tbl;

select 20 between 2 and 4;

select 3 between 2 and 5;

select 2 in (2,3,4);

select 2 in (2,3,NULL);

select 2 in ( 3,NULL);

select * from users;

select * from users where lastname like 'Con%';

select * from users where lastname like 'Con___';

select current_timestamp;

select STRFTIME('%Y', 'now');

select strftime('%m', created_at) from media; 

--select * from users order by rand();

-- select database();


-------------------------------------------ВЕБИНАР--------------------------------------------

select * from users;

select 
--	id, 
	firstname, 
	lastname, 
	(select hometown from profiles where user_id = users.id) as 'city', 
	(select filename from media where id = (select photo_id from profiles where user_id = users.id)) as 'main_photo'
from users;

select * from media where user_id = 1 and media_type_id = (select id from media_types where name = 'Photo');

select * from media where user_id = 1 and (filename like '%jpg' or filename like '%avi');


select count(*) from media where user_id = 1 and media_type_id = (select id from media_types where name = 'Photo'); 


select media_type_id, (select name from media_types where id = media.media_type_id) as type, count(*) from media group by type;


select count(*) as cnt from media group by  STRFTIME('%m', created_at) order by cnt desc;  

--select MONTH(created_at) from media;

select count(*), (select firstname from users where id = media.user_id) from media group by user_id order by count(*) asc;



select *, (select name from media_types where id = media.media_type_id) from media where user_id in (
	select target_user_id from friend_requests where initiator_user_id = 1 and status = 'approved'
	UNION 
	select initiator_user_id from friend_requests where target_user_id = 1 and status = 'approved'
)

select user_id, 
	birthday, 
	case(gender)
		when 'm' then 'male'
		when 'f' then 'female'
		else 'не указан'
	end as gender
	from profiles where user_id in (
	select target_user_id from friend_requests where initiator_user_id = 1 and status = 'approved'
	UNION 
	select initiator_user_id from friend_requests where target_user_id = 1 and status = 'approved'
)

alter table friend_requests add check (initiator_user_id <> target_user_id);


