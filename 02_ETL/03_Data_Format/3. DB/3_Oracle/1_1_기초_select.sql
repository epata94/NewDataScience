-- �ּ� �ޱ� ����

-- ������ �������� ���̺� ��� ��ȸ
select * from tabs;

-- ���̺� ��Ű�� ��ȸ
desc employees;

-- �÷� �� �⺻ ���� ��ȸ
select * from cols 
where table_name = 'employees'; -- ��ҹ��� �����Ұ�
-- Ctrl + Enter �����Ұ�
select * from cols 
where table_name = 'EMPLOYEES';

-- ��ü ���̺� ��ȸ
select * from employees;

-- SELECT
-- projection (�� ����)
select first_name, last_name, salary
from employees;
-- ��� �� ����
select * from departments;

-- �⺻ ǥ�� ����
select first_name, hire_date, salary
from employees;

-- ������ �켱����
select first_name, last_name, salary, salary+salary*0.1
from employees;

-- NULL�� ����
select first_name, department_id, commission_pct
from employees;

-- �� ��Ī(alias) ����
select first_name as �̸�, salary  �޿�
from employees;

select first_name "Employee Name",
        salary*12 "Annual Salary"
from employees;

-- ���ͷ�(literal) ���� ��Ʈ���� ���� ������
select first_name || ' ' || last_name || '''s salary is $' || salary
    as "��� �� ����"
from employees;

-- �ߺ� ��� DISTINCT
select department_id
from employees;

select DISTINCT department_id
from employees;

-- ROWNUM, ROWID �ǻ翭(Pseudo column)
select employee_id, first_name from employees;
select rowid, rownum, employee_id, first_name from employees;

-- ���� ���� (Selection)
select first_name, last_name, hire_date
from employees
where last_name='King';

-- �񱳿�����
select first_name, salary, hire_date
from employees
where salary >= 15000;

select first_name, salary, hire_date
from employees
where hire_date = '04/01/30';

select first_name, salary, hire_date
from employees
where first_name='Steven';

-- BETWEEN ������
select first_name, salary
from employees
where salary between 10000 and 12000;

-- IN ������
select manager_id from employees;

select employee_id, first_name, salary, manager_id
from employees
where manager_id in (101, 102, 103);

-- LIKE ������
-- % ��ȣ Ȱ��
select job_id from employees;

select first_name, last_name, job_id, department_id
from employees
where job_id like 'IT%';

-- 2003�� 1�� 1�Ϻ��� 2003�� 12�� 31�� ���̿� �Ի��� ��� ����� �̸��� �Ի���
select first_name, hire_date
from employees
where hire_date like '03%';

-- '_' ��ȣ Ȱ��
-- �� ��° ���ڰ� 'A' �� ��� ����� �̸��� �̸��� ���
select first_name, email
from employees
where email like '_A%';

-- '_' ��ȣ�� �����ϴ� �ؽ�Ʈ �˻��� ESCAPE �ɼ� Ȱ��
select first_name, job_id
from employees
where job_id like 'SA\_M%' ESCAPE '\';

-- IS NULL ������
select first_name, manager_id
from employees
where manager_id is null;

-- �� ������
-- and ���� 
select first_name, job_id, salary
from employees
where job_id='IT_PROG' and salary>=5000;

-- or ����
select first_name, job_id, salary
from employees
where job_id='IT_PROG' or salary>=5000;

-- ������ �켱���� (AND, OR ������)
select first_name, job_id, salary
from employees
where job_id='IT_PROG' 
    or job_id>='FI_MGR'
    and salary >= 6000;

select first_name, job_id, salary
from employees
where (job_id='IT_PROG' 
    or job_id>='FI_MGR')
    and salary >= 6000;
    
-- ������ ����
-- order by (�⺻ �������� ����)
select first_name, hire_date
from employees
order by hire_date;
-- asc (��������� ����)
select first_name, hire_date
from employees
order by hire_date asc;

-- �������� ���� (desc)
select first_name, hire_date
from employees
order by hire_date desc;

-- �� ��Ī
-- step1
select first_name, salary
from employees
order by salary;
-- step2
select first_name, salary*1.2 
from employees;
-- step3
select first_name, salary*1.2 
from employees
order by salary*1.2;
-- ���⼭ �������� �����ϱ�?

select first_name, salary*1.2 as �λ�޿�
from employees
order by �λ�޿�;

-- BEST Option
select first_name, salary*1.2 as raise_salary
from employees
order by raise_salary;

