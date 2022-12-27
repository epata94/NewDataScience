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

drop table weather;
describe weather;

delete from weather;

select * from weather;

-- 자동 생성 sql
INSERT INTO WEATHER (DATE_TIME, NX, NY, "기온", "시간1_강수량", "강수형태", "습도", "풍속", "풍향", "동서바람성분", "남북바람성분") VALUES (to_timestamp('202212271500'),58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);
INSERT INTO WEATHER (DATE_TIME, NX, NY, "기온", "시간1_강수량", "강수형태", "습도", "풍속", "풍향", "동서바람성분", "남북바람성분") VALUES ('20221227 1500',58,125,3.4,0.0,0.0,46.0,1.4,225.0,1.0,1.0);
