--------------------------------
--4�� �׷��Լ��� �̿��� ������ ����
--------------------------------
--4.1 �׷��Լ�
SELECT * FROM employees;
-- COUNT, SUM, AVG, MIN, MAX, STDDEV, VARIANCE
SELECT  COUNT(salary), AVG(salary), MAX(salary), MIN(salary), SUM(salary), STDDEV(salary)
FROM    employees
WHERE   job_id LIKE 'SA%';

SELECT   MIN(hire_date), MAX(hire_date)
FROM     employees;

SELECT MIN(first_name), MAX(first_name)
FROM   employees;

--��� ����� ���� ����϶�
SELECT COUNT(*) FROM employees;

SELECT COUNT(commission_pct) 
FROM employees; -- Ŀ�̼��� �޴� ����� ���� ���

--���� ū �޿�����?
SELECT MAX(salary) FROM employees;
--���� ���� �޿��� �޴� ����� �̸���? --> ���������� �ذ��ؾ� ��.

--������� �޿��� ����, ��հ� ǥ������, �׸��� �л��� ���ϼ���. �Ҽ��� ���� �� ��° �ڸ������� ǥ���ϼ���.
SELECT SUM(salary) AS �հ�, 
       ROUND(AVG(salary), 2) AS ���, --,2�� �Ҽ��� �� ��° �ڸ����� �ݿø�
       ROUND(STDDEV(salary), 2) AS ǥ������,
       ROUND(VARIANCE(salary), 2) AS �л�
FROM employees;
-- skip
-- Q] ��ü ����� �޿� �λ��(alary*commission_pct)�� ����� ���ϼ���.
--    ��, ����� �Ҽ��� 2�ڸ��� �ݿø��Ѵ�
-- 688.691588785046728971962616822429906542
SELECT AVG(NVL(salary*commission_pct,0))
FROM   employees;
-- 2105.428571428571428571428571428571428571
SELECT AVG(salary*commission_pct)
FROM   employees;

-- 2105.43
SELECT ROUND(AVG(salary*commission_pct), 2) AS avg_bonus
FROM employees; --Ŀ�̼� ���, null�� ���꿡�� ���ܵȴ�.

-- �����Ұ�
SELECT 
  ROUND(SUM(salary*commission_pct), 2) sum_bonus, 
  COUNT(*) count, 
  -- count(*)�� NULL �����Ͽ� ������ ���� ������ �и� �þ ���� �پ���.
  ROUND(SUM(salary*commission_pct)/count(*), 2) avg_bonus1,
  ROUND(AVG(salary*commission_pct), 2) avg_bonus2
FROM employees; --NULL�� ���꿡�� ���ܵȴ�.

--GROUP BY
SELECT    department_id
FROM      employees
GROUP BY  department_id;

SELECT    department_id,  AVG(salary)
FROM      employees
GROUP BY  department_id;

-- �ϳ� �̻��� ���� �׷�ȭ
SELECT    department_id, job_id, SUM(salary)
FROM      employees
GROUP BY  department_id, job_id;

SELECT  COUNT(first_name) 
FROM    employees;
-- �׷� �Լ��� �߸� ����� ����
-- �������� ���� �׷��Լ��� ȥ���ؼ� ����� ������ �������� ���� ����ϴ�
-- GROUP BY ���� �����ؾ� �Ѵ�.
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

-- AS ���� ����
SELECT   job_id, AVG(salary) PAYROLL
FROM     employees
WHERE    job_id NOT LIKE 'SA%'
GROUP BY job_id
HAVING   AVG(salary) > 8000
ORDER BY PAYROLL;

-- �Ʒ� grouping sets�� ���� ��� �ܰ�1
-- ���� �̸��� grouping �� ���� ��ġ���� �ʴ´�. �ι�° grouping�� ���� job_id
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id -- department_id�� �޿� ���
union all
select job_id, round(avg(salary),2)
from employees
group by job_id -- job_id �� �޿����
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

-- grouping set Ȯ��
-- grouping set( (�׷��1), (�׷��2) .. )
SELECT   department_id, job_id, manager_id, ROUND(AVG(salary), 2) AS avg_sal
FROM     employees
GROUP BY 
GROUPING SETS ((department_id, job_id), (job_id, manager_id))
ORDER BY department_id, job_id, manager_id;
-- �Ʒ� �ڵ��� ���� ���
SELECT    department_id, job_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  department_id, job_id
ORDER BY department_id, job_id;

SELECT    job_id, manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  job_id,manager_id
ORDER BY job_id,manager_id;

-- �׳� union all �ϸ� ��������. ���� ��ġ���� �ʱ� ������
-- �̷� ��쿡�� union all�� ������ �ذ��Ϸ��� ���� ���� grouping set�� ����ϴ� ���� ����.
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
-- manager_id�� department_id�� null �̱� ������ �ش� ���� ���� ��ó���� �ؾ��Ѵ�.
SELECT    department_id, job_id, NULL as manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  department_id, job_id
union all
SELECT    NULL as department_id, job_id, manager_id, ROUND(AVG(salary), 2)
FROM      employees
GROUP BY  job_id,manager_id;

-- SKIP
SELECT DECODE(GROUPING(department_id), 1, '��� �μ�', department_id) AS �μ���,
       DECODE(GROUPING(job_id), 1, '��� ����', job_id) AS ������,
       COUNT(*) AS �����,
       SUM(salary) AS �ѱ޿���
FROM employees
GROUP BY GROUPING SETS (department_id, job_id)
ORDER BY �μ���, ������;


--ROLLUP, CUBE
--�μ���, ������ �޿��� ��հ� ����� ���� ����϶�.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY department_id, job_id
ORDER BY department_id, job_id;

--���� ����� �� �μ��� ��հ�, ����� ���� ����ϰ� �ͽ��ϴ�.
--��ü ���, ��ü ����� ���� ����ϰ� �ͽ��ϴ�.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY ROLLUP(department_id, job_id) --ROLLUP�� ������(department_id, job_id��) ���踦 ����Ѵ�.
ORDER BY department_id, job_id;

--���� ����� ������ �޿���հ� ����� ���� ����ϰ� �ͽ��ϴ�.
SELECT department_id, job_id, ROUND(AVG(salary),2), COUNT(*) 
FROM employees
GROUP BY CUBE(department_id, job_id) --CUBE�� ������ �������� ���踦 ����Ѵ�.
ORDER BY department_id, job_id;

-- GROUPING
-- skip
SELECT 
  NVL2(department_id, department_id||'', 
                      DECODE(GROUPING(department_id), 1, '�Ұ�')) AS �μ�, 
  NVL(job_id, DECODE(GROUPING(job_id), 1, '�Ұ�')) AS ����,
  ROUND(AVG(salary),2) AS ���, 
  COUNT(*) AS ����Ǽ�
FROM 
  employees
GROUP BY 
  CUBE(department_id, job_id)
ORDER BY 
  �μ�, ����;


-- GROUPING_ID
-- skip
SELECT 
  NVL2(department_id, 
       department_id||'', 
       decode(GROUPING_ID(department_id, job_id), 2, '�Ұ�',
                                        3, '�հ�')) AS �μ���ȣ,
  NVL(job_id, 
      decode(GROUPING_ID(department_id, job_id), 1, '�Ұ�',
                                       3, '�հ�')) AS ����,
  GROUPING_ID(department_id, job_id) AS GID,
  ROUND(AVG(salary),2) AS ���, 
  COUNT(*) AS ����Ǽ�
FROM 
  employees
GROUP BY CUBE(department_id, job_id)
ORDER BY �μ�, ����;
