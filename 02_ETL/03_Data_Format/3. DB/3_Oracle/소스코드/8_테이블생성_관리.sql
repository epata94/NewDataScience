-- 테이블 생성
CREATE TABLE test_table (
   deptno  NUMBER(2),
   dname   VARCHAR2(14),
   loc     VARCHAR2(13) );
   
-- 왼쪽에서 새로 고침
   
-- 테이블 스키마 조회
describe test_table;

insert into test_table
values(
    11,
    'IT개발',
    '서울'
);

select * from test_table;

-- 열 추가
alter table test_table
add (job varchar2(10));

describe test_table;
select * from test_table;

-- 열 이름 변경
alter table test_table
rename column deptno to department_no;
alter table test_table
rename column dname to department_name;

describe test_table;

-- 열 속성 변경
-- 크게 변경하는 것은 문제 없으나 작게는 안됨
alter table test_table
modify (department_name varchar2(20));
describe test_table;

-- 열 삭제
alter table test_table
drop column job;
describe test_table;
select * from test_table;

drop table test_table;