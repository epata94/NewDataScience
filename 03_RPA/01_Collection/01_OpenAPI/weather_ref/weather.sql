create table weather(
    date_time       timestamp,
    nx              number(8,3),
    ny              number(8,3),
    �ð�1_������      number(8,3),
    ��������        number(8,3),
    ���              number(8,3),
    ����          number(8,3),
    ǳ��          number(8,3),
    ǳ��          number(8,3),
    �����ٶ�����  number(8,3),
    ���Ϲٶ�����  number(8,3)
);

select * from weather;
delete from weather;
select column_name from cols where table_name='WEATHER';
drop table covid_hospital;
delete from covid_hospital;
select count(*) from covid_hospital;
select * from covid_hospital;