-- HR 테이블 ERD 설명
-- JOIN의 종류 Oracle Join vs ANSI JOIN: 오라클 9i 버전부터 지원되는 SQL 표준 문법
--ANSI JOIN
--CROSS JOIN: 두 개의 테이블에 대한 카테시안 프로덕트(Cartesian Product)와 같은 결과(모든 조합)를 출력
-- select table1.column1, table2.column2
-- from table1
-- cross join table2;
select employee_id from employees;
select department_name from departments;
SELECT employee_id, department_name
FROM  employees 
CROSS JOIN departments;

SELECT * FROM departments;
SELECT * FROM locations;
SELECT * FROM employees;
-- NATURAL JOIN
-- 모든 동일한 이름을 갖는 컬럼들에 대해 조인
SELECT employee_id, first_name, department_id, department_name
FROM employees 
NATURAL JOIN departments;

-- USING: using 절을 사용하여 원하는 컬럼에 대해서 명시적으로 조인
SELECT first_name, department_name
FROM   employees 
JOIN   departments 
USING (department_id);


-- ON
-- JOING 이후 서브쿼리와 같은 추가 서술 가능, 3개 이상 테이블에서 조인 수행이 가능등 보다 복잡한 조인이 가능
SELECT first_name, department_name
FROM employees e    -- 테이블명 별칭 
JOIN departments d 
ON (e.department_id=d.department_id);

--여러 테이블 조인
--모든 사원의 이름과 부서이름, 부서의 주소를 출력하세요.
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
JOIN  locations l 
ON    d.location_id=l.location_id;

--WHERE 절과의 혼용
SELECT e.first_name AS name,
       d.department_name AS department
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
WHERE employee_id = 103;

--ON 절의 조건 추가
SELECT e.first_name AS name,
       d.department_name AS department
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id AND employee_id = 103;

-- 103번 사원의 이름과 부서이름, 주소 출력
-- employee_id = 103의 결과만 얻으려고 할 경우에 유용
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id AND employee_id = 103
JOIN  locations l 
ON    d.location_id=l.location_id;

-- 위와 동일한 결과: employee_id로 다양한 검색을 하려고 할 때에 유용
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
JOIN  locations l 
ON    d.location_id=l.location_id AND employee_id = 103;

--EXIST절 사용
SELECT first_name, department_name
FROM employees e 
JOIN departments d 
ON   e.department_id=d.department_id; --106개 행 인출

SELECT first_name, department_name
FROM   employees e 
LEFT JOIN   departments d 
ON     e.department_id=d.department_id
WHERE  e.department_id IS NULL;

SELECT first_name, department_name
FROM   employees e 
LEFT JOIN   departments d 
ON     e.department_id=d.department_id
WHERE  e.department_id IS NULL;

-- OUTER JOIN
--SELECT
--FROM table1
--[LEFT|RIGHT|FULL] [OUTER] JOIN talble2 -- OUTER는 생략가능
--ON

SELECT e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
FROM   employees e
LEFT JOIN job_history j
ON       e.employee_id = j.employee_id
ORDER BY j.employee_id;

SELECT e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
FROM   job_history j
FULL JOIN employees e
ON       e.employee_id = j.employee_id
ORDER BY j.employee_id;