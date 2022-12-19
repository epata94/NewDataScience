-- 103번 사원의 이름과 부서 이름을 출력하세요.
select first_name, employees.department_id, department_name
from employees, departments
where employee_id=103 and employees.department_id=departments.department_id
;

-- 103번 사원의 이름과 매니저의 이름을 출력하세요.
-- 사원의 정보는 employees, 매니저 정보는... employees에 있음
-- 같은 테이블에서 조인을 셀프조인이라고 합니다.
-- 테이블 별칭이 반드시 필요함
-- 열을 지정할 때 별칭을 이용해서 지정

SELECT emp.first_name, emp.manager_id, man.first_name
FROM employees emp, employees man
WHERE emp.manager_id=man.employee_id and emp.employee_id=103
;
select * from departments;

-- 모든 사원의 이름과 부서번호, 부서이름을 출력하세요
select first_name, d.department_id, department_name
from employees e, departments d
where e.department_id(+)=d.department_id
;

select employee_id, department_name
from employees
cross join departments;


-- 두 테이블이 같은 열 이름으로 조인이 되어 있을 경우
select employee_id, job_id, job_title
from employees
natural join jobs;

select employee_id, department_name
from employees
natural join departments;

-- 같은 이름의 열이 2개 이상 있을 경우 조인 열을 지정
select employee_id, department_name
from employees
join departments using(department_id);
using(department_id);

-- 직접 조인 조건을 지정하려면...
select employee_id, department_name
from employees
join departments on employees.department_id=departments.department_id;

-- self join
select e.first_name as 사원이름, m.first_name as 매니저이름
from employees e
join employees m on e.manager_id=m.employee_id;

-- * 60번 부서가 있는 지역의 우편번호를 출력하세요.
select department_id, postal_code
from departments, locations
where department_id=60 and departments.location_id=locations.location_id;

select department_id, postal_code
from departments
 natural join locations
where department_id=60;

select department_id, postal_code
from departments
 join locations on departments.location_id=locations.location_id
where department_id=60;

-- 모든 사원의 이름, 부서이름, 우편번호를 출력하세요.
select first_name, department_name, postal_code
from employees e
join departments d on e.department_id=d.department_id
join locations l on d.location_id=l.location_id;

-- 계층형 쿼리
SELECT employee_id, lpad(' ', 3*(level-1)) || first_name, level
from employees
start with manager_id is null
connect by prior employee_id = manager_id
order siblings by first_name;

--
select department_id
from (
    select department_id, stddev(salary) as sd_sal from employees
    group by department_id
    order by sd_sal desc
)
where rownum=1
;


-- 실습
-- Steven King 사원이 입사한지 500일째 되는 날짜는?
SELECT hire_date+500 from employees
where first_name='Steven' and last_name='King';

-- 부서 번호가 20, 30, 40에 속하는 사원의 이름은?
select first_name
from employees
where department_id in (20, 30, 40);

-- 직무 아이디가 IT_PROG이거나 AD_VP인 사원중 급여가 7000 이상인 사원의 이름은?
select first_name
from employees
where (job_id='IT_PROG' or job_id='AD_VP') and salary >= 7000;

-- 50번 부서가 있는 지역의 우편번호는?
select postal_code
from departments d
join locations l on d.location_id=l.location_id
where department_id=50;

-- 급여의 편차가 가장 작은 부서의 번호를 출력하세요.
select department_id
from (
select department_id, stddev(salary) as sd_sal from employees
group by department_id
order by sd_sal)
where rownum=1
;

-- Lex 사원의 급여를 10% 인상한 금액은?
select salary*1.1 from employees where first_name='Lex';

-- IT 직무에 해당하지 않는 사원은?
select first_name from employees where job_id not like 'IT%';

-- 12월 입사자의 직무는?
select job_id from employees where hire_date like '%/12/%';

-- 보너스가 없는 사원은 몇명?
select count(*) from employees where commission_pct is null; --72
select count(*) from employees where commission_pct = null; --0
select count(*) from employees where commission_pct <> null; --0
select count(*) from employees where commission_pct in (null); --0

-- 급여를 가장 많이 받이 받는 사람의 이름은?
select first_name from employees
where salary = (select max(salary) from employees);

-- 102번 사원이 근무하는 부서의 이름은?
select department_name
from employees e
join departments d on e.department_id=d.department_id
where e.employee_id=102;

-- 매니저 직무인 사원은?
select first_name from employees
where job_id like '%MAN';

-- 105번 사원의 상사는?
select employee_id, first_name from employees
start with employee_id=105
connect by prior manager_id=employee_id;

-- ROWNUM 의사열은 반드시 첫번째 항목부터 조회해야 합니다.
-- where rownum between 10 and 20 이 조건은 검색이 안됩니다.

-- 50번 부서의 사원 중에서 50번 부서의  급여 평균보다 더 많은 급여를 받는 사원의 이름은?
select first_name from employees
where salary > (select avg(salary) from employees where department_id=80)
    and department_id=80
;

-- unique 제약조건은 널이 가능합니다.그런데 널의 개수는 여러개 가능합니다.