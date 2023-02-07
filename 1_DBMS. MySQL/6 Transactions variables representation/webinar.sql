--- хранимые процедуры (stored_procedure)

-- критерии выбора пользователей: 1. из одного города 2. состоят в одной группе 3. друзья друзей
-- будем показывать по 5 пользователей в случайной комбинации

use vk;

delimiter //
drop procedure if exists sp_friendship_offers;
create procedure sp_friendship_offers(for_user_id bigint)
begin
--друзья
--общее табличное выражение
	with friends as (
		select initiator_user_id as id from friend_requests where target_user_id = for_user_id and status = 'approved'
		UNION
		select taget_user_id as id  from friend_requests where initiator_user_id = for_user_id and status = 'approved'
		) 
--общий город
	select p2.user_id
	from profiles p1
	join profiles p2 on p1.hometown = p2.hometown 
	where p1.user_id = for_user_id and p2.user_id <> for_user_id
	union
--состоят в одной группе
	select uc2.user_id
	from users_communities uc1
	join users_communities uc2 on uc1.community_id = uc2.community_id 
	where uc1.user_id = for_user_id and uc2.user_id <> for_user_id
	union
--друзья друзей
	select fr.initiator_user_id
	from friends f
	join friend_requests fr on fr.target_user_id = f.id
	where fr.initiator_user_id != for_user_id and status = 'approved'
	union 
	select fr.target_user_id
	from friends f
	join friend_requests fr on fr.initiator_user_id = f.id
	where fr.targetr_user_id != for_user_id and status = 'approved'
	order by rand()
	limit 5
end//
delimiter ;

call sp_friendship_offers(1);

-- пользовательские функции

drop function if exists vk.friendship_direction;

delimiter //

create function vk.friendship_direction(check_user bigint)
returns float reads sql data
begin
	declare requests_to_user int;
	declare requests_from_user int;

	set requests_to_user = (
		select count(*) from friend_requests where target_user_id = check_user_id 
	);

	set requests_from_user = (
		select count(*) from friends_requests where initiator_user_id = check_user_id
	);

--	select count(*) into requests_from_user from friend_requests where initiator_user_id = check_user_id;

	return requests_to_user / requests_from_user;

	
end //

delimiter ; 

select truncate(friendship_direction(1), 2)*100 as user_popularity;

create procedure sp_user_add(out tran_result varchar(100)) 
begin
	declare '_rollback' bit default b'0';
	
	declare continue handler for sqlexception
	begin
		set '_rollback' = b'1';
	end;
 
	start transaction;
	insert into users (firstname, lastname, email, phone) values ('new', 'user', 'new@mail.com', 12352134);
	--set @last_user_id = (select id from users where email = 'new@mail.com');
	set @last_user_id = last_insert_id();
	insert into profiles (user_id, gender, birthday, hometown) values (@last_user_id, 'M', '1999-10-10', 'Moscow');
	if '_rollback' then
		set tran_result = 'ROLL';
		rollback;
	else
		set tran_result = 'COM';
		commit;
	end if;
end

call sp_user_add(@tran_result); 

select @tran_result;



-- транзакции

-- представления

-- триггеры


