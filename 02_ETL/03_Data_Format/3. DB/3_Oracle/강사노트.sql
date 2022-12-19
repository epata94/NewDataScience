-- 103�� ����� �̸��� �μ� �̸��� ����ϼ���.
select first_name, employees.department_id, department_name
from employees, departments
where employee_id=103 and employees.department_id=departments.department_id
;

-- 103�� ����� �̸��� �Ŵ����� �̸��� ����ϼ���.
-- ����� ������ employees, �Ŵ��� ������... employees�� ����
-- ���� ���̺��� ������ ���������̶�� �մϴ�.
-- ���̺� ��Ī�� �ݵ�� �ʿ���
-- ���� ������ �� ��Ī�� �̿��ؼ� ����

SELECT emp.first_name, emp.manager_id, man.first_name
FROM employees emp, employees man
WHERE emp.manager_id=man.employee_id and emp.employee_id=103
;
select * from departments;

-- ��� ����� �̸��� �μ���ȣ, �μ��̸��� ����ϼ���
select first_name, d.department_id, department_name
from employees e, departments d
where e.department_id(+)=d.department_id
;

select employee_id, department_name
from employees
cross join departments;


-- �� ���̺��� ���� �� �̸����� ������ �Ǿ� ���� ���
select employee_id, job_id, job_title
from employees
natural join jobs;

select employee_id, department_name
from employees
natural join departments;

-- ���� �̸��� ���� 2�� �̻� ���� ��� ���� ���� ����
select employee_id, department_name
from employees
join departments using(department_id);
using(department_id);

-- ���� ���� ������ �����Ϸ���...
select employee_id, department_name
from employees
join departments on employees.department_id=departments.department_id;

-- self join
select e.first_name as ����̸�, m.first_name as �Ŵ����̸�
from employees e
join employees m on e.manager_id=m.employee_id;

-- * 60�� �μ��� �ִ� ������ �����ȣ�� ����ϼ���.
select department_id, postal_code
from departments, locations
where department_id=60 and departments.location_id=locations.location_id;

select department_id, postal_code
from departments
 natural join locations
where department_id=60;

select department_id, postal_code
from departments
 join locations on departments.location_id=locations.location_id
where department_id=60;

-- ��� ����� �̸�, �μ��̸�, �����ȣ�� ����ϼ���.
select first_name, department_name, postal_code
from employees e
join departments d on e.department_id=d.department_id
join locations l on d.location_id=l.location_id;

-- ������ ����
SELECT employee_id, lpad(' ', 3*(level-1)) || first_name, level
from employees
start with manager_id is null
connect by prior employee_id = manager_id
order siblings by first_name;

--
select department_id
from (
    select department_id, stddev(salary) as sd_sal from employees
    group by department_id
    order by sd_sal desc
)
where rownum=1
;


-- �ǽ�
-- Steven King ����� �Ի����� 500��° �Ǵ� ��¥��?
SELECT hire_date+500 from employees
where first_name='Steven' and last_name='King';

-- �μ� ��ȣ�� 20, 30, 40�� ���ϴ� ����� �̸���?
select first_name
from employees
where department_id in (20, 30, 40);

-- ���� ���̵� IT_PROG�̰ų� AD_VP�� ����� �޿��� 7000 �̻��� ����� �̸���?
select first_name
from employees
where (job_id='IT_PROG' or job_id='AD_VP') and salary >= 7000;

-- 50�� �μ��� �ִ� ������ �����ȣ��?
select postal_code
from departments d
join locations l on d.location_id=l.location_id
where department_id=50;

-- �޿��� ������ ���� ���� �μ��� ��ȣ�� ����ϼ���.
select department_id
from (
select department_id, stddev(salary) as sd_sal from employees
group by department_id
order by sd_sal)
where rownum=1
;

-- Lex ����� �޿��� 10% �λ��� �ݾ���?
select salary*1.1 from employees where first_name='Lex';

-- IT ������ �ش����� �ʴ� �����?
select first_name from employees where job_id not like 'IT%';

-- 12�� �Ի����� ������?
select job_id from employees where hire_date like '%/12/%';

-- ���ʽ��� ���� ����� ���?
select count(*) from employees where commission_pct is null; --72
select count(*) from employees where commission_pct = null; --0
select count(*) from employees where commission_pct <> null; --0
select count(*) from employees where commission_pct in (null); --0

-- �޿��� ���� ���� ���� �޴� ����� �̸���?
select first_name from employees
where salary = (select max(salary) from employees);

-- 102�� ����� �ٹ��ϴ� �μ��� �̸���?
select department_name
from employees e
join departments d on e.department_id=d.department_id
where e.employee_id=102;

-- �Ŵ��� ������ �����?
select first_name from employees
where job_id like '%MAN';

-- 105�� ����� ����?
select employee_id, first_name from employees
start with employee_id=105
connect by prior manager_id=employee_id;

-- ROWNUM �ǻ翭�� �ݵ�� ù��° �׸���� ��ȸ�ؾ� �մϴ�.
-- where rownum between 10 and 20 �� ������ �˻��� �ȵ˴ϴ�.

-- 50�� �μ��� ��� �߿��� 50�� �μ���  �޿� ��պ��� �� ���� �޿��� �޴� ����� �̸���?
select first_name from employees
where salary > (select avg(salary) from employees where department_id=80)
    and department_id=80
;

-- unique ���������� ���� �����մϴ�.�׷��� ���� ������ ������ �����մϴ�.