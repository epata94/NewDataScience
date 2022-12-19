-- 주석 달기 연습

-- 접속한 계정에서 테이블 목록 조회
select * from tabs;

-- 테이블 스키마 조회
desc employees;

-- 컬럼 및 기본 정보 조회
select * from cols 
where table_name = 'employees'; -- 대소문자 구분할것
-- Ctrl + Enter 연습할것
select * from cols 
where table_name = 'EMPLOYEES';

-- 전체 테이블 조회
select * from employees;

-- SELECT
-- projection (열 선택)
select first_name, last_name, salary
from employees;
-- 모든 열 선택
select * from departments;

-- 기본 표시 형식
select first_name, hire_date, salary
from employees;

-- 연산자 우선순위
select first_name, last_name, salary, salary+salary*0.1
from employees;

-- NULL의 정의
select first_name, department_id, commission_pct
from employees;

-- 열 별칭(alias) 정의
select first_name as 이름, salary  급여
from employees;

select first_name "Employee Name",
        salary*12 "Annual Salary"
from employees;

-- 리터럴(literal) 문자 스트링과 연결 연산자
select first_name || ' ' || last_name || '''s salary is $' || salary
    as "사원 상세 정보"
from employees;

-- 중복 행과 DISTINCT
select department_id
from employees;

select DISTINCT department_id
from employees;

-- ROWNUM, ROWID 의사열(Pseudo column)
select employee_id, first_name from employees;
select rowid, rownum, employee_id, first_name from employees;

-- 행의 제한 (Selection)
select first_name, last_name, hire_date
from employees
where last_name='King';

-- 비교연산자
select first_name, salary, hire_date
from employees
where salary >= 15000;

select first_name, salary, hire_date
from employees
where hire_date = '04/01/30';

select first_name, salary, hire_date
from employees
where first_name='Steven';

-- BETWEEN 연산자
select first_name, salary
from employees
where salary between 10000 and 12000;

-- IN 연산자
select manager_id from employees;

select employee_id, first_name, salary, manager_id
from employees
where manager_id in (101, 102, 103);

-- LIKE 연산자
-- % 기호 활용
select job_id from employees;

select first_name, last_name, job_id, department_id
from employees
where job_id like 'IT%';

-- 2003년 1월 1일부터 2003년 12월 31일 사이에 입사한 모든 사원의 이름과 입사일
select first_name, hire_date
from employees
where hire_date like '03%';

-- '_' 기호 활용
-- 두 번째 문자가 'A' 인 모든 사원의 이름과 이메일 출력
select first_name, email
from employees
where email like '_A%';

-- '_' 기호를 포함하는 텍스트 검색시 ESCAPE 옵션 활용
select first_name, job_id
from employees
where job_id like 'SA\_M%' ESCAPE '\';

-- IS NULL 연산자
select first_name, manager_id
from employees
where manager_id is null;

-- 논리 연산자
-- and 연산 
select first_name, job_id, salary
from employees
where job_id='IT_PROG' and salary>=5000;

-- or 연산
select first_name, job_id, salary
from employees
where job_id='IT_PROG' or salary>=5000;

-- 연산자 우선순위 (AND, OR 순으로)
select first_name, job_id, salary
from employees
where job_id='IT_PROG' 
    or job_id>='FI_MGR'
    and salary >= 6000;

select first_name, job_id, salary
from employees
where (job_id='IT_PROG' 
    or job_id>='FI_MGR')
    and salary >= 6000;
    
-- 데이터 정렬
-- order by (기본 오름차순 정렬)
select first_name, hire_date
from employees
order by hire_date;
-- asc (명시적으로 지정)
select first_name, hire_date
from employees
order by hire_date asc;

-- 내림차순 정렬 (desc)
select first_name, hire_date
from employees
order by hire_date desc;

-- 열 별칭
-- step1
select first_name, salary
from employees
order by salary;
-- step2
select first_name, salary*1.2 
from employees;
-- step3
select first_name, salary*1.2 
from employees
order by salary*1.2;
-- 여기서 문제점은 무엇일까?

select first_name, salary*1.2 as 인상급여
from employees
order by 인상급여;

-- BEST Option
select first_name, salary*1.2 as raise_salary
from employees
order by raise_salary;

