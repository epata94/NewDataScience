--1. 성이 'Bull'인 사람의 이름과 성을 출력 (검색조건은 반드시 모두 대문자 'BULL'로 해야함)
select first_name, last_name from employees
where upper(last_name) = 'BULL';

--2. 이메일에 'lee'(대/소문자 구분 안함)을 포함하는 사원의 급여는?
select salary from employees
where lower (email) like '%lee%';

--3. 직원의 급여를 아래 포맷대로 출력하세요.
--(성, 이름 순으로 출력)
King,Steven'급여는 24000$ 입니다.
select last_name || ',' || first_name || '''급여는 ' || salary || '$ 입니다.' from employees;

--4. Steven King 사원이 입사한지 500일째 되는 날짜는?
SELECT hire_date+500 from employees
where first_name='Steven' and last_name='King';

--5. 부서 번호가 20, 30, 40에 속하는 사원의 이름은?
select first_name
from employees
where department_id in (20, 30, 40);

--6. Lex 사원의 급여를 10% 인상한 금액은?
select salary*1.1 from employees where first_name='Lex';

--7. IT 직무에 해당하지 않는 사원을 이름순을 오름차순 정렬하여 출력
select first_name from employees where job_id not like 'IT%'
order by first_name;

--8. 12월 입사자의 직무는?
select job_id from employees where hire_date like '%/12/%';

--9. 보너스가 없는 사원은 몇명?
select count(*) from employees where commission_pct is null; --72

--10. 직무 ID가 'SA_' 로 시작하는 직원의 이름, 입사일 그리고 입사일로 부터 24개월 지난 날을 '승진대상일' 이란 열이름으로 출력
SELECT first_name, hire_date, ADD_MONTHS(hire_date, 24) as 승진대상일
FROM employees
WHERE job_id like 'SA_%';

--11. 직원의 이름과 급여를 1000단위로 조회할수 있도록 급여K 라는 열을 만들어 출력하세요.
--FIRST_NAME	급여K
--Steven		24
--Neena		17
--Lex			17
--Alexander	9
--Bruce		6
--David		4

select first_name, trunc(salary,-3)/1000 as 급여k from employees;

--12. 직원 별 이름, 성, 그리고 입사환영회식일을 출력한다. 입사환영회식일은 입사한 주의 금요일이다.
select first_name, last_name, NEXT_DAY(hire_date,'금') as 입사환영회식일
from employees

