-- типы многотабличных запросов
-- union, join, subquery

-- в основе sql лежит теори€ множеств - union, except, intersect

-- join == innner join, left, right, outer
-- дл€ union таблицы должны совпадать по структуре (количеству и типу данных в пол€х)

-- subquery: 
-- in, all, some ==  any, проверка на существование, коррелированные запросы, подзапросы в конструкции FROM, exists

 select id, subquery
 	from
 		subquery
 	WHERE
 		subquery
 	group by
 		id
 	having
 		subquery
 		
 -- если запрос использует столбец из внешнего подзапроса, то такой запрос называетс€ скоррелированным
 		
 -- JOIN 
 		
 		-- декартово произведение таблиц
 		
 		-- типы соединений
 		-- JOIN (INNER), LEFT, RIGHT, OUTER (CROSS)  b
 		-- ключеваые слова ON USING
 		
 		-- ON == WHERE - ON быстрее. USING при совпадении названий столбцов, по которым соедин€ем таблицы
 		
 		-- ћногтабличные обновлени€
 		
 		-- ћноготабличные удалени€
 		
 -- внешние ключи и ссылочна€ целостность
 
 		-- ограничени€ внешнего ключа CASCADE, SET NULL, NO ACTION, RESTRICT, SET DEFAULT
 		-- нарушение ссылочной целостности
 		-- ключевое слово FOREIGN KEY 
 		
 		
 ------------------------------------------------WEBINAR--------------------------------------------------
 		
 -- LEFT, LEFT WHERE B.KEY IS NULL, RIGHT, RIGHT WHERE A.KEY IS NULL, INNER, FULL OUTER, FULL OUTER WHERE A.KEY IS NULL OR B.KEY IS NULL
 		
 	
 
 --cross
 		
SELECT count(*) FROM users, messages m;
select * from users join messages;
select count(*) from users join messages;

-- вывести пользователей и отправленные ими сообщени€ (inner)
 
select * from users left join messages on users.id = messages.from_user_id where messages.id not null;

select * FROM users join messages where users.id = messages.from_user_id;

insert into users (firstname, lastname) values ('test', 'test2');

-- подсчитать количество сообщений, написанных каждым пользователем

select firstname 'им€', count() 'количество' from users join messages on users.id = messages.from_user_id where messages.id not null group by users.id; 
select firstname 'им€', count() 'количество' from users join messages on users.id = messages.from_user_id GROUP by users.id;
 		
 		
-- 

select * from users left join messages on users.id = messages.from_user_id;

-- full join

-- select * from users u full join messages m on users.id = messages.from_user_id;

select * from users u left join messages m on u.id = m.from_user_id;
-- union
-- select * from messages m right join users u on m.from_user_id = u.id;


-- nолучить им€, фамилию, город и аватарку пользователей

select firstname, lastname, hometown, filename
	from 
	users
	join profiles on users.id = profiles.user_id 
	join media on profiles.photo_id = media.id;
	
-- выборка документов пользовател€

select firstname, filename from users left join media m on users.id = m.user_id;

--  количество друзей дл€ каждого пользовател€

select firstname, count(*) cnt from users u left join friend_requests fr on (u.id = fr.initiator_user_id) or (u.id=fr.target_user_id)
where fr.status = 'approved' group by u.id order by cnt desc

-- получить список медиафайлов с количеством лайков

select filename, count(*) from media left join likes on media.id = likes.media_id group by filename order by count(*) desc;
