select * from music_for_send.music m where is_send = 0;

update music_for_send.music set is_send = 0 where id in (812, 808);

select * from music_for_send.music m ;

select id, title, link from music_for_send.music_result_concat_multiple_values where link = 'https://youtu.be/_B5O7tkH1LY';

select * from music_for_send.music_result_concat_multiple_values mrcmv;

delete from music_for_send.tags where tag in ('tag_1', 'tag_2');

select * from music_for_send.music_result_concat_multiple_values order by id desc limit 5; 
select * from music_for_send.tags t order by id desc limit 5;
select * from music_for_send.channels c order by id desc limit 5;
select * from music_for_send.music_tag mt order by id desc limit 5;

delete from music_for_send.music where id in (1087,1088);

select * from my_current.current_result_concat_multiple_values crcmv ;

select * from my_current.`current` c ;

SELECT * from my_current.tags;
SELECT * from my_current.categories c ;

delete from my_current.categories where id in (3,4,8,6,7,5)

