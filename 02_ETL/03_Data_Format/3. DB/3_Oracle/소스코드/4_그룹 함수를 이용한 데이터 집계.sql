--------------------------------
--4장 그룹함수를 이용한 데이터 집계
--------------------------------
--4.1 그룹함수
SELECT * FROM employees;
-- COUNT, SUM, AVG, MIN, MAX, STDDEV, VARIANCE
SELECT  COUNT(salary), AVG(salary), MAX(salary), MIN(salary), SUM(salary), STDDEV(salary)
FROM    employees
WHERE   job_id LIKE 'SA%';

SELECT   MIN(hire_date), MAX(hire_date)
FROM     employees;

SELECT MIN(first_name), MAX(first_name)
FROM   employees;

--모든 사원의 수를 출력하라
SELECT COUNT(*) FROM employees;

SELECT COUNT(commission_pct) 
FROM employees; -- 커미션을 받는 사원의 수를 출력

--가장 큰 급여액은?
SELECT MAX(salary) FROM employees;
--가장 많은 급여를 받는 사원의 이름은? --> 서브쿼리로 해결해야 함.

--사원들의 급여의 총합, 평균과 표준편차, 그리고 분산을 구하세요. 소수점 이하 두 번째 자리까지만 표현하세요.
SELECT SUM(salary) AS 합계, 
       ROUND(AVG(salary), 2) AS 평균, --,2는 소수점 두 번째 자리까지 반올림
       ROUND(STDDEV(salary), 2) AS 표준편차,
       ROUND(VARIANCE(salary), 2) AS 분산
FROM employees;
-- skip
-- Q] 전체 사원의 급여 인상분(alary*commission_pct)의 평균을 구하세요.
--    단, 평균은 소수점 2자리로 반올림한다
-- 688.691588785046728971962616822429906542
SELECT AVG(NVL(salary*commission_pct,0))
FROM   employees;
-- 2105.428571428571428571428571428571428571
SELECT AVG(salary*commission_pct)
FROM   employees;

-- 2105.43
SELECT ROUND(AVG(salary*commission_pct), 2) AS avg_bonus
FROM employees; --커미션 평균, null은 연산에서 제외된다.

-- 강의할것
SELECT 
  ROUND(SUM(salary*commission_pct), 2) sum_bonus, 
  COUNT(*) count, 
  -- count(*)는 NULL 포함하여 개수를 세기 때문에 분모가 늘어나 값이 줄어든다.
  ROUND(SUM(salary*commission_pct)/count(*), 2) avg_bonus1,
  ROUND(AVG(salary*commission_pct), 2) avg_bonus2
FROM employees; --NULL은 연산에서 제외된다.

--GROUP BY
SELECT    department_id
FROM      employees
GROUP BY  department_id;

SELECT    department_id,  AVG(salary)
FROM      employees
GROUP BY  department_id;

-- 하나 이상의 열로 그룹화
SELECT    department_id, job_id, SUM(salary)
FROM      employees
GROUP BY  department_id, job_id;

SELECT  COUNT(first_name) 
FROM    employees;
-- 그룹 함수를 잘못 사용한 질의
-- 개별적인 열과 그룹함수를 혼합해서 사용할 때에는 개별적인 열을 명시하는
-- GROUP BY 절을 포함해야 한다.
SELECT  department_id, COUNT(first_name)
FROM    employees;


SELECT  department_id, COUNT(first_name)
FROM    employees
GROUP BY department_id;

SELECT    department_id, AVG(salary)
FROM      employees
WHERE     AVG(salary) > 2000
GROUP BY  department_id;

-- HAVING
-- SELECT column, group_function(column)
-- FROM table
--  [WHERE ? ?condition(s)]
--  [GROUP BY group_by_expression]
--  [HAVING group_condition]
--  [ORDER BY {column|expr [[ASC]|DESC], ...};

SELECT   department_id, ROUND(AVG(salary), 2)
FROM     employees
GROUP BY department_id
HAVING   AVG(salary) >= 8000;

-- AS 생략 가능
SELECT   job_id, AVG(salary) PAYROLL
FROM     employees
WHERE    job_id NOT LIKE 'SA%'
GROUP BY job_id
HAVING   AVG(salary) > 8000
ORDER BY PAYROLL;

-- 아래 grouping sets과 같은 결과 단계1
-- 열의 이름이 grouping 한 대상과 일치하지 않는다. 두번째 grouping한 것은 job_id
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id -- department_id별 급여 평균
union all
select job_id, round(avg(salary),2)
from employees
group by job_id -- job_id 별 급여평균
order by 1;

-- grouping set
-- HAVING
-- SELECT column, group_function(column)
-- FROM table
--  [WHERE ? ?condition(s)]
--  [GROUP BY [GROUPING SETS] group_by_expression]
--  [HAVING group_condition]
--  [ORDER BY {column|expr [[ASC]|DESC], ...};
select department_id, job_id, round(avg(salary), 2)
from employees
group by grouping sets (department_id, job_id)
order by department_id, job_id;

-- grouping set 확장
-- grouping set( (그룹셋1), (그룹셋2) .. )
SELECT   department_id, job_id, manager_id, ROUND(AVG(salary), 2) AS avg_sal
FROM     employees
GROUP BY 
GROUPING SETS ((department_id, job_id), (job_id, manager_id))
ORDER BY department_id, job_id, manager_id;
-- 아래 코드의 합한 결과
SELECT    department_id, job_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  department_id, job_id
ORDER BY department_id, job_id;

SELECT    job_id, manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  job_id,manager_id
ORDER BY job_id,manager_id;

-- 그냥 union all 하면 에러난다. 열이 일치하지 않기 때문에
-- 이럴 경우에는 union all로 문제를 해결하려고 하지 말고 grouping set을 사용하는 것이 좋다.
SELECT    department_id, job_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  department_id, job_id
ORDER BY department_id, job_id
union all
SELECT    job_id, manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  job_id,manager_id
ORDER BY job_id,manager_id;

-- skip
-- manager_id와 department_id가 null 이기 때문에 해당 값에 대한 열처리를 해야한다.
SELECT    department_id, job_id, NULL as manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  department_id, job_id
union all
SELECT    NULL as department_id, job_id, manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  job_id,manager_id;

-- SKIP
SELECT DECODE(GROUPING(department_id), 1, '모든 부서', department_id) AS 부서명,
       DECODE(GROUPING(job_id), 1, '모든 업무', job_id) AS 업무명,
       COUNT(*) AS 사원수,
       SUM(salary) AS 총급여액
FROM employees
GROUP BY GROUPING SETS (department_id, job_id)
ORDER BY 부서명, 업무명;


--ROLLUP, CUBE
--부서별, 직무별 급여의 평균과 사원의 수를 출력하라.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY department_id, job_id
ORDER BY department_id, job_id;

--위의 결과에 각 부서별 평균과, 사원의 수도 출력하고 싶습니다.
--전체 평균, 전체 사원의 수를 출력하고 싶습니다.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY ROLLUP(department_id, job_id) --ROLLUP은 레벨별(department_id, job_id별) 집계를 출력한다.
ORDER BY department_id, job_id;

--위의 결과에 직무별 급여평균과 사원의 수도 출력하고 싶습니다.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY CUBE(department_id, job_id) --CUBE는 가능한 조합으로 집계를 출력한다.
ORDER BY department_id, job_id;

-- GROUPING
-- skip
SELECT 
  NVL2(department_id, department_id||'', 
                      DECODE(GROUPING(department_id), 1, '소계')) AS 부서, 
  NVL(job_id, DECODE(GROUPING(job_id), 1, '소계')) AS 직무,
  ROUND(AVG(salary),2) AS 평균, 
  COUNT(*) AS 사원의수
FROM 
  employees
GROUP BY 
  CUBE(department_id, job_id)
ORDER BY 
  부서, 직무;


-- GROUPING_ID
-- skip
SELECT 
  NVL2(department_id, 
       department_id||'', 
       decode(GROUPING_ID(department_id, job_id), 2, '소계',
                                        3, '합계')) AS 부서번호,
  NVL(job_id, 
      decode(GROUPING_ID(department_id, job_id), 1, '소계',
                                       3, '합계')) AS 직무,
  GROUPING_ID(department_id, job_id) AS GID,
  ROUND(AVG(salary),2) AS 평균, 
  COUNT(*) AS 사원의수
FROM 
  employees
GROUP BY CUBE(department_id, job_id)
ORDER BY 부서, 직무;
