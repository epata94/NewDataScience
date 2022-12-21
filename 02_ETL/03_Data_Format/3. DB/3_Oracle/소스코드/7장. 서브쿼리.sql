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
SELECT first_name, salary 
FROM   employees 
WHERE  salary > ANY (SELECT salary
              FROM   employees 
              WHERE  first_name='David'); -- 4800, 6800, 9500



SELECT first_name, department_id, job_id
FROM employees
WHERE department_id IN (SELECT department_id 
                 FROM employees 
                 WHERE first_name='David');
                 
                 
--20번 부서에 근무하는 사원의 평균보다 많은 급여를 받는 사원의 이름과 급여를 출력하라
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
             FROM employees
             WHERE department_id=20)
; 

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
SELECT first_name, (SELECT department_name
               FROM  departments d
               WHERE d.department_id=e.department_id) department_name
FROM employees e
ORDER BY first_name
;



--Join 을 이용한 쿼리문
SELECT first_name, department_name
FROM employees e JOIN departments d ON (e.department_id=d.department_id)
ORDER BY first_name
;

--인라인 뷰
SELECT row_number, first_name, salary
FROM (SELECT first_name, salary,
      row_number() OVER (ORDER BY salary DESC) AS row_number
      FROM employees)
WHERE row_number between 1 and 10;

SELECT row_number, first_name, salary
FROM (SELECT first_name, salary,
      row_number() OVER (ORDER BY salary DESC) AS row_number
      FROM employees)
WHERE row_number between 11 and 20;

SELECT ROWID, ROWNUM, employee_id, first_name
FROM employees;

SELECT rnum, first_name, salary
FROM (SELECT first_name, salary, rownum AS rnum
      FROM (SELECT first_name, salary
            FROM employees
            ORDER BY salary DESC)
     )
WHERE rnum between 11 and 20;


SELECT rownum, first_name, salary
FROM (SELECT first_name, salary
      FROM employees
      ORDER BY salary DESC)
WHERE rownum between 1 and 10;

SELECT first_name, salary
FROM (SELECT first_name, salary
      FROM employees
      ORDER BY salary DESC)
WHERE rownum between 11 and 20;

SELECT rnum, first_name, salary
FROM (SELECT first_name, salary, rownum AS rnum
      FROM (SELECT first_name, salary
            FROM employees
            ORDER BY salary DESC)
     )
WHERE rnum between 11 and 20;


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
