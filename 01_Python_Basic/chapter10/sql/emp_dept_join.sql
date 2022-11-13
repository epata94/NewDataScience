-- 전체 테이블 보기 

show tables;

select * from goods;

-- 사원 table 생성 
drop table emp;

create or replace table emp(
eno int auto_increment primary key,
ename varchar(25) not null,
hiredate date not null,
pay int default 0,
bonus int default 0,
dname varchar(50)
);

-- 사번 시작값 지정 
alter table emp auto_increment = 1001;

-- 사원 추가 
insert into emp(ename,hiredate,pay,bonus,dname)
       values('홍길동','2008-03-10', 300, 15, '영업부');
insert into emp(ename,hiredate,pay,dname)
       values('강호동','2010-03-10', 250, '판매부');
insert into emp(ename,hiredate,pay,bonus,dname)
       values('유관순','2008-03-10', 200, 10, '회계부');
insert into emp(ename,hiredate,pay,bonus,dname)
       values('강감찬','2007-01-10', 400, 25, '영업부');
       
select * from emp;

commit work; -- db 반영 

-- 부서 정보 
create or replace table dept(
dname varchar(50) not null,
daddr varchar(100)
);

insert into dept values('영업부', '뉴욕시');
insert into dept values('판매부', '서울시');
insert into dept values('회계부', '대전시');
select * from dept;

commit work;

/*
inner join 
select columns
from table1 inner join table2
on join 조건식;
*/ 

-- 3개 레코드 검색 
select e.eno, e.ename, e.pay, d.dname, d.daddr
from emp e inner join dept d
on e.dname = d.dname and e.pay >= 250;

/*
 * outer join 
 * select columns
 * from table1  left/right outer join table2
 * on join 조건식;
 */

-- 4개 레코드 검색 
select e.eno, e.ename, e.pay, d.dname
from emp e left outer join dept d
on e.dname = d.dname and e.pay >= 250;

-- 3개 레코드 검색(103 정상 출력) 
select e.eno, e.ename, e.pay, d.dname
from emp e right outer join dept d
on e.dname = d.dname and d.dname = '회계부';




















