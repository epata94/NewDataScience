-- �ּ�: ù��° SQL��
select * from employees;

-- ���� ����Ŭ ���� ����
select * from v$version;

-- ������ �������� ���̺� ��� ��ȸ
select * from tabs;

-- �÷� �� �⺻ ���� ��ȸ
-- ���̺� �̸��� '�빮��'�� �Է��� ��
SELECT * from cols
where table_name = 'employees';

SELECT * from cols
where table_name = 'EMPLOYEES';

-- select (Projection => �� ����)
select first_name, last_name, salary from employees;

-- date Ÿ��
-- YY/MM/DD �������� ������ (Default�� DD/MM/YY)
select first_name, hire_date, salary from employees;

-- ������ �켱����
-- 0.1 �޿� �λ����, salary*0.1: �λ�� �޿�
select first_name, last_name, salary, salary+salary*0.1
from employees;

-- ������ ��, Null ǥ��
select first_name, department_id, commission_pct
from employees;

-- �� ��Ī(alias) ����
select first_name as �̸�, salary �޿�
from employees;

-- ���� ���α׷����� ���̸��� �ν��ϱ� ���� �뵵�ε� �ݵ�� ����ؾ���
select first_name, last_name, salary, salary+salary*0.1 as �޿��λ��
from employees;
-- �����ϸ� ���� ��Ī�� ��� ����
select first_name, last_name, salary, salary+salary*0.1 as raised_income
from employees;

-- ���ͷ�(literal) ���� ��Ʈ���� ���� ������
select first_name || ' ' || last_name || '''s salary is $' || salary
    as "���������"
from employees;

-- �ߺ� ��� DISTINCT
select department_id from employees;
select distinct department_id from employees;

-- ROWNUM, ROWID �ǻ翭(Pseudo column)
-- ����Ŭ���� ���� �ε����� 1���� �����Ѵ�.
-- rowid�� ���ϰ����� ����, ���� �����ϰ� ���� ������ Ű (PK�ε� Ȱ�밡��)
-- rownum �˻������ ���Ͽ� 1���� ���� �ο�
select employee_id, first_name from employees;
select rowid, rownum, employee_id, first_name from employees;

-- ���� ���� (Selection): where �������� ����
select first_name, last_name, hire_date
from employees
where last_name = 'King';

-- �� ������
select first_name, salary, hire_date
from employees
where salary >= 15000;

-- ��¥��
select first_name, salary, hire_date
from employees
where hire_date='04/01/30'; -- �Ϲ��� ����ȯ�� �Ͼ�� ������ ����

-- between ������ ( between �������� and ������) ��������, ������ ����
select first_name, salary
from employees
where salary between 10000 and 12000;

-- IN ������ 
select manager_id from employees;
-- Q] �������̺��� manager_id�� 101, 102 �Ǵ� 103�� ����id, �̸�, �޿�, �Ŵ���id�� ����ϼ���
-- => IN ������ ����ؼ�
select employee_id, first_name, salary, manager_id
from employees
where manager_id in (101, 102, 103);

-- LIKE ������
-- % ��ȣ Ȱ��
select job_id from employees;

select first_name, last_name, job_id, department_id
from employees
where job_id like 'IT%';

-- Q] 2003�� 1�� 1�Ϻ��� 2003�� 12�� 31�� ���̿� �Ի��� ��� ����� �̸��� �Ի���
select first_name, hire_date
from employees
where hire_date like '03%';

-- '_' ��ȣ Ȱ�� : '_' ������ �� ���ڿ� ��Ī
-- �̸����� �� ��° ���ڰ� 'A'�� ��� ����� �̸��� �̸����� ���
select first_name, email
from employees
where email like '_A%';

-- IS NULL ������ : null�� ���� ã����
select first_name, manager_id
from employees
where manager_id is null;

-- �� ������
-- and ����
-- Q] ���� id�� IT_PROG�̰� �޿��� 5000 �̻��� ������ �̸�, ���� id, �޿��� ����Ͻÿ�.
select first_name, job_id, salary
from employees
where job_id='IT_PROG' and salary >= 5000;
-- or ����
-- Q] ���� id�� IT_PROG�̰ų� �޿��� 5000 �̻��� ������ �̸�, ���� id, �޿��� ����Ͻÿ�.
select first_name, job_id, salary
from employees
where job_id='IT_PROG' or salary >= 5000;

-- Q] ���� ���̵� 'IT_PROG' �Ǵ� 'FI_MGR' �̰� �޿��� 6000 �̻��� 
-- ������ �̸�, ����id, �޿��� ����ϼ���.
-- ����Ŭ���� and �������� �켱������ or ���� ����.
-- ���� �ǹ̸� �и��ϰ� �ϱ� ���ؼ� () �����ڸ� Ȱ���� ��
select first_name, job_id, salary
from employees
where (job_id = 'IT_PROG' or job_id='FI_MGR') and salary >=6000;

-- ������ ����
-- order by (�⺻ �������� ����)
-- select
-- from
-- where
-- order by <- �� ��ġ���� ���

select first_name, hire_date
from employees
order by hire_date;

select first_name, hire_date
from employees
order by hire_date asc; -- ��������� ������������ ����

-- �������� ���� (desc)
select first_name, hire_date
from employees
order by hire_date desc;

-- �� ��Ī ����
select first_name, salary
from employees
order by salary;

select first_name, salary*1.2 -- <= salary*1.2 : �޿��� 20% �λ��� �ݿ��� �ݾ�
from employees
order by salary*1.2;

select first_name, salary*1.2 as �λ�ȱ޿� -- <= salary*1.2 : �޿��� 20% �λ��� �ݿ��� �ݾ�
from employees
order by �λ�ȱ޿�;

select first_name, salary*1.2 as raise_salary -- <= salary*1.2 : �޿��� 20% �λ��� �ݿ��� �ݾ�
from employees
order by raise_salary;
