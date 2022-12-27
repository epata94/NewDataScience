create table weather(
    date_time       timestamp,
    nx              number(8,3),
    ny              number(8,3),
    시간1_강수량      number(8,3),
    강수형태        number(8,3),
    기온              number(8,3),
    습도          number(8,3),
    풍향          number(8,3),
    풍속          number(8,3),
    동서바람성분  number(8,3),
    남북바람성분  number(8,3)
);

select * from weather;
delete from weather;
select column_name from cols where table_name='WEATHER';
drop table covid_hospital;
delete from covid_hospital;
select count(*) from covid_hospital;
select * from covid_hospital;