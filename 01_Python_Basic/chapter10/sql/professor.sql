-- 교수 테이블 
create or replace table prof(
 pno int auto_increment primary key,    -- 교수번호(기본키)
 name  varchar(10) not null, 
 position varchar (15) not null, -- 직위(전임강사,조/부/정교수) 
 hiredate  date not null,   
 pay int not null,     
 bonus int,             
 deptno int          -- 학과번호(101~301) 
);

-- 교수번호 시작값 지정 
alter table prof auto_increment = 1001;

insert into prof(name, position, hiredate, pay, bonus, deptno)
values('조인형','정교수','1980-06-23',550,90, 101);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values('박승곤','조교수','1987-01-30',380,60,101);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('송도권','전임강사','1998-03-22',270,null,101);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('양선희','전임강사','2001-09-01', 250,null,102);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('김영조','조교수','1985-11-30',350,80,102);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('주승재','정교수','1982-04-29',490,90,102);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('김도형','정교수','1981-10-23',530,110,103);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('나한열','조교수','1997-07-01',330,50,103);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('김현정','전임강사','2002-02-24',290,null,103);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('심슨','정교수','1981-10-23',570,130,201);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('최슬기','조교수','2009-08-30',330,null,201);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('박원범','조교수','1999-12-01',310,50,202);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('차범철','전임강사','2009-01-28',260,null,202);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('바비','정교수','1985-09-18',500,80,203);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('전민','전임강사','2010-06-28',220,null,301);
insert into prof(name, position, hiredate, pay, bonus, deptno)
values ('허은','조교수','2001-05-23',290,30,301);

select * from prof;
commit work;

-- function
select count(*) from prof; -- 16
select count(bonus) from prof; -- 10
select sum(pay), avg(bonus) from prof;

-- group by 범주형 칼럼 
-- 직급별 급여 평균  
select position, avg(pay) from prof group by position;
select position, avg(pay) from prof group by position order by avg(pay) desc;

-- 학과별 급여, 보너서 평균 
select deptno, avg(pay), avg(bonus) from prof group by deptno;
select deptno, avg(pay), avg(bonus) from prof 
group by deptno having avg(pay) >= 350;

-- 그룹, 조건, 정렬 
select deptno, avg(pay), avg(bonus) from prof 
group by deptno having avg(pay) >= 350
order by avg(pay) desc;










