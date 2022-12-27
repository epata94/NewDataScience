create table weather(
    DATE_TIME	    timestamp,
    NX      	    number(8,3),
    NY	            number(8,3),
    기온              number(8,3),
    시간1_강수량	    number(8,3),
    강수형태	        number(8,3),
    습도              number(8,3),
    풍속             number(8,3),
    풍향	            number(8,3),
    동서바람성분	    number(8,3),
    남북바람성분      number(8,3)
);

insert into weather values (
'202212280900',
58,125,0,0,-2.8,60,250,3,2.8,-0.8
);
commit;
select * from weather;

create table test_table2(
    my_index VARCHAR2(10)
);

insert into test_table2 values ('2');
select * from test_table2;

drop table weather;
describe weather;

delete from weather;
commit;
select rownum, date_time from weather where rownum=3;
select rownum, date_time from weather;
delete from weather where rownum in (3);

DELETE FROM weather
WHERE ROWID =
(SELECT rid FROM (SELECT ROWNUM rn, ROWID rid FROM weather) WHERE rn = 1);
select * from weather;
commit;





-- 자동 생성 sql
INSERT INTO WEATHER (DATE_TIME, NX, NY, "기온", "시간1_강수량", "강수형태", "습도", "풍속", "풍향", "동서바람성분", "남북바람성분") VALUES (to_timestamp('202212271500'),58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);
INSERT INTO WEATHER (DATE_TIME, NX, NY, "기온", "시간1_강수량", "강수형태", "습도", "풍속", "풍향", "동서바람성분", "남북바람성분") VALUES ('20221227 1500',58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);
