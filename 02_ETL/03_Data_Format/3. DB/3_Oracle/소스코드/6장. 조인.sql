SELECT * FROM employees;
SELECT * FROM departments;

SELECT first_name, department_name
FROM employees, departments
;

SELECT first_name, employees.department_id, department_name
FROM employees, departments; 

SELECT e.first_name, e.department_id, d.department_name
FROM employees e, departments d;


SELECT e.first_name, e.department_id, d.department_name
FROM employees e, departments d
WHERE e.department_id = d.department_id; 


SELECT e.first_name AS employee_name, m.first_name AS manager_name
FROM employees e, employees m --e는 사원 테이블, m은 manager 테이블
WHERE e.manager_id = m.employee_id AND e.employee_id=103;

SELECT * FROM jobs;

SELECT  e.first_name, e.salary, j.job_title
FROM    employees e, jobs j
WHERE   e.salary
BETWEEN j.min_salary AND j.max_salary
ORDER BY first_name;

SELECT employee_id, first_name, department_id
FROM   employees;

SELECT e.employee_id, e.first_name, e.department_id, d.department_name
FROM   employees e, departments d
WHERE  e.department_id(+) = d.department_id
ORDER BY e.employee_id; 
--모든 사원을 조회하는데 있어서 직책 변동 기록이 있는 사원이 있다면 그 변동내역까지 조회하는 쿼리를 작성.
SELECT e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
FROM   employees e, job_history j
WHERE  e.employee_id = j.employee_id
ORDER BY j.employee_id;

SELECT e.employee_id, e.first_name, e.hire_date,
       j.start_date, j.end_date, j.job_id, j.department_id
FROM   employees e, job_history j
WHERE  e.employee_id = j.employee_id(+)
ORDER BY j.employee_id;
--ANSI JOIN
--CROSS JOIN
SELECT employee_id, department_name
FROM  employees 
CROSS JOIN departments;

SELECT * FROM departments;
SELECT * FROM locations;
SELECT * FROM employees;
--NATURAL JOIN
SELECT employee_id, first_name, department_id, department_name
FROM employees 
NATURAL JOIN departments;


--CREATE TABLE emp2 AS select employee_id, first_name, department_id from employees;

SELECT first_name, department_name
FROM   employees 
JOIN   departments 
USING (department_id);



SELECT first_name, department_name
FROM employees e 
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

SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id AND employee_id = 103
JOIN  locations l 
ON    d.location_id=l.location_id;

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