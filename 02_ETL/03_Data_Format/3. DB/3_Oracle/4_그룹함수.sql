----------------------------------------------
--            그룹함수를 이용한 데이터 집계
----------------------------------------------

-- COUNT, SUM, AVG, MIN, MAX, VARIANCE, STDDEV
-- (salary)
select COUNT(salary), SUM(salary), AVG(salary), MIN(salary), MAX(salary), 
        VARIANCE(salary), STDDEV(salary)
from employees;

select min(hire_date),max(hire_date)
from employees;

select min(first_name),max(first_name)
from employees;

-- Q] 가장 큰 급여액은?
select max(salary) from employees;
-- Q] 사원들의 급여의 총합, 평균, 표준편차, 그리고 분산을 구하세요.
-- 단 소수점 이하 두 번쨰 자리까지 반올림할것
select sum(salary) as 합계,
    round(avg(salary), 2) as 평균,
    round(stddev(salary), 2) as 평균,
    round(variance(salary), 2) as 평균
from employees;

-- 평균값을 구할때 주의할점
select commission_pct from employees;
select
    round (sum(salary*commission_pct),2) sum_bonus,
    -- count함수는 null값도 센다.
    round (sum(salary*commission_pct)/count(*),2) avg_bonus1, --  인상분의 평균
    -- avg함수는 null값은 제외한다.
    round (avg(salary*commission_pct),2) avg_bonus2     -- 인상분의 평균 avg 함수를 통해서
from employees;

-- GROUP BY
select department_id
from employees
group by department_id;

-- Group by 와 집계 함수 응용
select department_id, AVG(salary)
from employees
group by department_id;

-- 하나 이상의 열로 그룹화 하기
-- select/group by 에 지정하는 열이름이 일치해야 한다.
select department_id,job_id, SUM(salary)
from employees
group by department_id,job_id;

-- 그룹 함수를 잘못 사용한 경우
-- 개별적인 열과 그룹함수를 혼합해서 사용할 때에는 개별적인 열을 명시하는
-- group by절을 반드시 포함해야 한다.
select department_id, count(first_name)
from employees;

select department_id, count(first_name)
from employees
group by department_id;

-- group by의 순서
-- select
-- from
-- where
-- group by <- 이 위치에서 사용

-- having: groub by 한 결과를 필터링 할 때 사용
-- select
-- from
-- where
-- group by 
-- having
-- order by
select department_id, round(avg(salary),2)
from employees
group by department_id
having avg(salary) >= 8000;

select job_id, avg(salary) payroll
from employees
where job_id NOT LIKE 'SA%'
group by job_id
having avg(salary) > 8000
order by payroll;

-- grouping sets: 복수개의 그룹셋을 유연하게 처리, union all의 기능을 대체
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id;
select job_id, round(avg(salary),2)
from employees
group by job_id;

-- 열의 이름이 grouping한 대상과 일치하지는 않는다.
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id
union all
select job_id, round(avg(salary),2)
from employees
group by job_id;

-- 위 결과를 grouping sets 함수를 통해 구현
select department_id, job_id, round(avg(salary),2)
from employees
group by grouping sets (department_id, job_id)
order by department_id, job_id;

-- grouping set 확장
-- grouping set ( (그룹셋1),(그룹셋2) ...)
select department_id, job_id, manager_id, round(avg(salary),2) as avg_sal
from employees
group by grouping sets ((department_id, job_id),(job_id, manager_id))
order by department_id, job_id, manager_id;

-- ROLLUP, CUBE
-- ROLLUP: 각 열별로 소계, 및 소계값의 합계를 제공, 그룹별로 소계값을 제공
-- 부서별, 직무별 급여의 평균과 사원의 수를 출력하라.
-- step1
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by department_id, job_id
order by department_id, job_id;

-- step2
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by rollup(department_id, job_id) -- ROLLUP은 레벨별 집계가 가능하다. /마지막 행은 합계가 출력된다.
order by department_id, job_id;

-- CUBE: ROLLUP의 결과에 각 열별 소계도 같이 제공
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by cube(department_id, job_id) 
order by department_id, job_id;
