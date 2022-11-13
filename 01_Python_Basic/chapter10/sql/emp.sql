-- 사원 테이블 생성 
create or replace table emp(
eno int auto_increment primary key,  -- 기본키, 사번 자동 증가 
ename varchar(20) not null,
hiredate date not null,
sal int,
bonus int default 0,   -- 생략시 기본값 0
dname varchar(50)
);

-- 사원번호 시작값 지정 
alter table emp auto_increment = 1001;

-- 레코드 추가 
insert into emp(ename, hiredate, sal, bonus, dname) 
              values('홍길동', '2008-03-10', 300, 15, '영업부');
insert into emp(ename, hiredate, sal, dname) 
              values('강호동', '2010-03-10', 250, '판매부');              
insert into emp(ename, hiredate, sal, bonus, dname) 
              values('유관순', '2008-03-10', 200, 10, '회계부');
select  * from emp;
commit work;
 
 
 
 
 

