create table covid_hospital(
    기관명         varchar2(128),
    구분코드        varchar2(32),
    시도명         varchar2(64),
    시군구명        varchar2(64),
    운영가능일자      date
);
drop table covid_hospital;

select count(*) from covid_hospital;
select * from covid_hospital;
delete from covid_hospital;