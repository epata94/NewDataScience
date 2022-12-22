-- ��������: ������ ������ ���� �������踦 Ȱ���Ͽ� ��ø�� ������ �ۼ��� �ϳ��� �˻������ �ڵ����� �ϼ�

--Nancy�� �޿����� ���� �޿��� �޴� ����� �̸��� �޿��� ����ϼ���.
SELECT salary FROM employees WHERE first_name='Nancy'; --12008
SELECT first_name, salary FROM employees WHERE salary > 12008;

--�������� �̿�
SELECT first_name, salary 
FROM   employees 
WHERE  salary > (SELECT salary
              FROM   employees 
              WHERE  first_name='Nancy'); -- ������ ��������
              
--Q] �޿��� ��� �̻� �޴� ����� �̸��� �޿��� ����ϼ���.
SELECT first_name, salary 
FROM   employees 
WHERE  salary >= (SELECT avg(salary)
               FROM   employees);

-- ������ ��������
SELECT salary 
FROM employees 
WHERE first_name='David';

-- �Ʒ� ������ ������ �߻�: where�� �������� �������� ����� ��µǾ�� �ϴµ� ���� ���� ���� ������ �˻��� �������� Ȱ���� �� ����
SELECT first_name, salary 
FROM   employees 
WHERE  salary > (SELECT salary
              FROM   employees 
              WHERE  first_name='David');

-- ������ ��������
-- ANY/ALL
-- ANY: �ϳ��� �����ϸ� �Ǵ� ���� / ALL: ��� ���� �����ϴ� ����
-- < ANY: ���� ū ������ ���� ����    (MAX ����)
-- > ANY: ���� ���� ������ ū ����    (MIN ����)
-- < all : ���� ���� ������ ���� ����  (MIN ����)
-- > all : ���� ū ������ ū ����     (MAX ����) 
SELECT first_name, salary 
FROM   employees 
WHERE  salary > ANY (SELECT salary
              FROM   employees 
              WHERE  first_name='David'); -- 4800, 6800, 9500

-- IN�� �������� ����: ����� � ���� ������ Ȯ��
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
                 
            
-- Q] 20�� �μ��� �ٹ��ϴ� ����� ��պ��� ���� �޿��� �޴� ����� �̸��� �޿��� ����϶�
SELECT first_name, salary
FROM employees
WHERE salary > (SELECT avg(salary)
             FROM employees
             WHERE department_id=20)
; 

-- ��ȣ���� ����
--�ڽ��� ���� �μ��� ��պ��� ���� �޿��� �޴� ����� �̸��� �޿��� ����϶�.
--��ȣ���� Sub Query�� �ۼ��ؾ� ��
--���������� ���̺��� ������������ ����
SELECT first_name, salary
FROM employees a
WHERE salary > (SELECT avg(salary)
             FROM employees b
             WHERE b.department_id=a.department_id)
;

--SELECT ���� ���������� �� �� �ִ� -> Scalar Sub Query
-- ��Ȳ�� ���� Join�� ��� ������ �ٿ� ������ ���� ���� ������ �׻� �׷����� �ʴ�.
-- �Ʒ� ������ ����� ��ü �� �� �ִ�.
--Join �� �̿��� ������
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



--�ζ��� ��
-- from ���� ��������. from ������ ���̺� �Ǵ� �䰡 �ü� �ִ�. 
-- ���������� �������� ���̱� ������ from ���� ���� ���������� �ζ��� ���� �θ���.
-- �޿��� ���� ���� �޴� ������� ���� 10���� ����� �޿�

SELECT  first_name, salary
FROM (SELECT first_name, salary
      FROM employees
      order by salary desc
      )
WHERE rownum between 1 and 10; -- MySQL�� limit �� ���� ���


-- ���� skip
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

-- ���� SKIP

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
