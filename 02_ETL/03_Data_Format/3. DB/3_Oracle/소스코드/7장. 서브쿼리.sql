-- 서브쿼리: 쿼리의 각각의 절에 의존관계를 활용하여 중첩된 쿼리를 작성해 하나의 검색결과를 자동으로 완성

--Nancy의 급여보다 많은 급여를 받는 사원의 이름과 급여를 출력하세요.
SELECT salary FROM employees WHERE first_name='Nancy'; --12008
SELECT first_name, salary FROM employees WHERE salary > 12008;

--서브쿼리 이용
SELECT first_name, salary 
FROM   employees 
WHERE  salary > (SELECT salary
              FROM   employees 
              WHERE  first_name='Nancy'); -- 단일행 서브쿼리
              
--Q] 급여를 평균 이상 받는 사원의 이름과 급여를 출력하세요.
SELECT first_name, salary 
FROM   employees 
WHERE  salary >= (SELECT avg(salary)
               FROM   employees);

-- 다중행 서브쿼리
SELECT salary 
FROM employees 
WHERE first_name='David';

-- 아래 구문은 에러를 발생: where의 조건으로 단일행의 결과가 출력되어야 하는데 여러 값이 오기 때문에 검색의 조건으로 활용할 수 없음
SELECT first_name, salary 
FROM   employees 
WHERE  salary > (SELECT salary
              FROM   employees 
              WHERE  first_name='David');

-- 다중행 서브쿼리
-- ANY/ALL
-- ANY: 하나라도 만족하면 되는 조건 / ALL: 모든 것을 만족하는 조건
-- < ANY: 가장 큰 값보다 작은 조건    (MAX 조건)
-- > ANY: 가장 작은 값보다 큰 조건    (MIN 조건)
-- < all : 가장 작은 값보다 작은 조건  (MIN 조건)
-- > all : 가장 큰 값보다 큰 조건     (MAX 조건) 
SELECT first_name, salary 
FROM   employees 
WHERE  salary > ANY (SELECT salary
              FROM   employees 
              WHERE  first_name='David'); -- 4800, 6800, 9500

-- IN에 서브쿼리 적용: 목록의 어떤 값과 같은지 확인
-- Step1
SELECT department_id 
                 FROM employees 
                 WHERE first_name='David'; -- 60, 80, 80
-- Step2
SELECT first_name, department_id, job_id
FROM employees
WHERE department_id IN (60, 80, 80);
-- Step3                 
SELECT first_name, department_id, job_id
FROM employees
WHERE department_id IN (SELECT department_id 
                 FROM employees 
                 WHERE first_name='David'); -- 60, 80, 80
                 
            
-- Q] 20번 부서에 근무하는 사원의 평균보다 많은 급여를 받는 사원의 이름과 급여를 출력하라
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
             FROM employees
             WHERE department_id=20)
; 

-- 상호연관 쿼리
--자신이 속한 부서의 평균보다 많은 급여를 받는 사원의 이름과 급여를 출력하라.
--상호연관 Sub Query를 작성해야 함
--메인쿼리의 테이블이 서브쿼리에서 사용됨
SELECT first_name, salary
FROM employees a
WHERE salary > (SELECT avg(salary)
             FROM employees b
             WHERE b.department_id=a.department_id)
;

--SELECT 절에 서브쿼리가 올 수 있다 -> Scalar Sub Query
-- 상황에 따라 Join할 대상 범위를 줄여 성능을 높일 수도 있으나 항상 그렇지는 않다.
-- 아래 조인의 결과를 대체 할 수 있다.
--Join 을 이용한 쿼리문
SELECT first_name, department_name
FROM employees e JOIN departments d ON (e.department_id=d.department_id)
ORDER BY first_name
;

SELECT first_name, (SELECT department_name
               FROM  departments d
               WHERE d.department_id=e.department_id) department_name
FROM employees e
ORDER BY first_name
;



--인라인 뷰
-- from 절에 서브쿼리. from 절에는 테이블 또는 뷰가 올수 있다. 
-- 서브쿼리도 독립적인 뷰이기 때문에 from 절에 오는 서브쿼리를 인라인 뷰라고 부른다.
-- 급여를 가장 많이 받는 사람부터 상위 10명의 사원과 급여

SELECT  first_name, salary
FROM (SELECT first_name, salary
      FROM employees
      order by salary desc
      )
WHERE rownum between 1 and 10; -- MySQL의 limit 과 같은 기능


-- 이후 skip
SELECT employee_id, 
       LPAD(' ', 3*(LEVEL-1)) || first_name || ' ' || last_name,
       LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id=manager_id
;

SELECT employee_id, 
       LPAD(' ', 3*(LEVEL-1)) || first_name || ' ' || last_name,
       LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id=manager_id
ORDER BY first_name
;

-- 이후 SKIP

SELECT employee_id, 
       LPAD(' ', 3*(LEVEL-1)) || first_name || ' ' || last_name,
       LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id=manager_id
ORDER SIBLINGS BY first_name
;

SELECT employee_id,
       LPAD(' ', 3*(LEVEL-1)) || first_name || ' ' || last_name,
       LEVEL
FROM employees
START WITH employee_id = 113
CONNECT BY PRIOR manager_id=employee_id
;
