-- HR ���̺� ERD ����
-- JOIN�� ���� Oracle Join vs ANSI JOIN: ����Ŭ 9i �������� �����Ǵ� SQL ǥ�� ����
--ANSI JOIN
--CROSS JOIN: �� ���� ���̺� ���� ī�׽þ� ���δ�Ʈ(Cartesian Product)�� ���� ���(��� ����)�� ���
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
-- ��� ������ �̸��� ���� �÷��鿡 ���� ����
SELECT employee_id, first_name, department_id, department_name
FROM employees 
NATURAL JOIN departments;

-- USING: using ���� ����Ͽ� ���ϴ� �÷��� ���ؼ� ��������� ����
SELECT first_name, department_name
FROM   employees 
JOIN   departments 
USING (department_id);


-- ON
-- JOING ���� ���������� ���� �߰� ���� ����, 3�� �̻� ���̺��� ���� ������ ���ɵ� ���� ������ ������ ����
SELECT first_name, department_name
FROM employees e    -- ���̺�� ��Ī 
JOIN departments d 
ON (e.department_id=d.department_id);

--���� ���̺� ����
--��� ����� �̸��� �μ��̸�, �μ��� �ּҸ� ����ϼ���.
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
JOIN  locations l 
ON    d.location_id=l.location_id;

--WHERE ������ ȥ��
SELECT e.first_name AS name,
       d.department_name AS department
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
WHERE employee_id = 103;

--ON ���� ���� �߰�
SELECT e.first_name AS name,
       d.department_name AS department
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id AND employee_id = 103;

-- 103�� ����� �̸��� �μ��̸�, �ּ� ���
-- employee_id = 103�� ����� �������� �� ��쿡 ����
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id AND employee_id = 103
JOIN  locations l 
ON    d.location_id=l.location_id;

-- ���� ������ ���: employee_id�� �پ��� �˻��� �Ϸ��� �� ���� ����
SELECT e.first_name AS name,
       d.department_name AS department, 
       l.street_address || ', ' || l.city || ', ' || l.state_province AS address
FROM  employees e 
JOIN  departments d 
ON    e.department_id=d.department_id
JOIN  locations l 
ON    d.location_id=l.location_id AND employee_id = 103;

--EXIST�� ���
SELECT first_name, department_name
FROM employees e 
JOIN departments d 
ON   e.department_id=d.department_id; --106�� �� ����

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
--[LEFT|RIGHT|FULL] [OUTER] JOIN talble2 -- OUTER�� ��������
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