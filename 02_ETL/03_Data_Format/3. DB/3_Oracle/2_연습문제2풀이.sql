--1. ���� 'Bull'�� ����� �̸��� ���� ��� (�˻������� �ݵ�� ��� �빮�� 'BULL'�� �ؾ���)
select first_name, last_name from employees
where upper(last_name) = 'BULL';

--2. �̸��Ͽ� 'lee'(��/�ҹ��� ���� ����)�� �����ϴ� ����� �޿���?
select salary from employees
where lower (email) like '%lee%';

--3. ������ �޿��� �Ʒ� ���˴�� ����ϼ���.
--(��, �̸� ������ ���)
King,Steven'�޿��� 24000$ �Դϴ�.
select last_name || ',' || first_name || '''�޿��� ' || salary || '$ �Դϴ�.' from employees;

--4. Steven King ����� �Ի����� 500��° �Ǵ� ��¥��?
SELECT hire_date+500 from employees
where first_name='Steven' and last_name='King';

--5. �μ� ��ȣ�� 20, 30, 40�� ���ϴ� ����� �̸���?
select first_name
from employees
where department_id in (20, 30, 40);

--6. Lex ����� �޿��� 10% �λ��� �ݾ���?
select salary*1.1 from employees where first_name='Lex';

--7. IT ������ �ش����� �ʴ� ����� �̸����� �������� �����Ͽ� ���
select first_name from employees where job_id not like 'IT%'
order by first_name;

--8. 12�� �Ի����� ������?
select job_id from employees where hire_date like '%/12/%';

--9. ���ʽ��� ���� ����� ���?
select count(*) from employees where commission_pct is null; --72

--10. ���� ID�� 'SA_' �� �����ϴ� ������ �̸�, �Ի��� �׸��� �Ի��Ϸ� ���� 24���� ���� ���� '���������' �̶� ���̸����� ���
SELECT first_name, hire_date, ADD_MONTHS(hire_date, 24) as ���������
FROM employees
WHERE job_id like 'SA_%';

--11. ������ �̸��� �޿��� 1000������ ��ȸ�Ҽ� �ֵ��� �޿�K ��� ���� ����� ����ϼ���.
--FIRST_NAME	�޿�K
--Steven		24
--Neena		17
--Lex			17
--Alexander	9
--Bruce		6
--David		4

select first_name, trunc(salary,-3)/1000 as �޿�k from employees;

--12. ���� �� �̸�, ��, �׸��� �Ի�ȯ��ȸ������ ����Ѵ�. �Ի�ȯ��ȸ������ �Ի��� ���� �ݿ����̴�.
select first_name, last_name, NEXT_DAY(hire_date,'��') as �Ի�ȯ��ȸ����
from employees

