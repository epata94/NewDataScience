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

insert into weather values (
'202212281000',
58,125,0,0,-2.8,60,3,250,2.8,-0.8
);
insert into weather values (
'202212281100',
58,125,0,0,-1.8,65,13,270,3.8,0.8
);

insert into weather values (
'202212281200',
58,125,0,0,0.8,58,10,200,1.8,1.8
);
commit;
insert into weather values (
'202212281300',
58,125,0,0,1.8,50,10,200,1.8,1.8
);
commit;
drop table weather;
select * from weather;

delete from weather;
select column_name from cols where table_name='WEATHER';
drop table covid_hospital;
delete from covid_hospital;
select count(*) from covid_hospital;
select * from covid_hospital;