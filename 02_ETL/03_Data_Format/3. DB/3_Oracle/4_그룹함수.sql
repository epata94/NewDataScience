----------------------------------------------
--            �׷��Լ��� �̿��� ������ ����
----------------------------------------------

-- COUNT, SUM, AVG, MIN, MAX, VARIANCE, STDDEV
-- (salary)
select COUNT(salary), SUM(salary), AVG(salary), MIN(salary), MAX(salary), 
        VARIANCE(salary), STDDEV(salary)
from employees;

select min(hire_date),max(hire_date)
from employees;

select min(first_name),max(first_name)
from employees;

-- Q] ���� ū �޿�����?
select max(salary) from employees;
-- Q] ������� �޿��� ����, ���, ǥ������, �׸��� �л��� ���ϼ���.
-- �� �Ҽ��� ���� �� ���� �ڸ����� �ݿø��Ұ�
select sum(salary) as �հ�,
    round(avg(salary), 2) as ���,
    round(stddev(salary), 2) as ���,
    round(variance(salary), 2) as ���
from employees;

-- ��հ��� ���Ҷ� ��������
select commission_pct from employees;
select
    round (sum(salary*commission_pct),2) sum_bonus,
    -- count�Լ��� null���� ����.
    round (sum(salary*commission_pct)/count(*),2) avg_bonus1, --  �λ���� ���
    -- avg�Լ��� null���� �����Ѵ�.
    round (avg(salary*commission_pct),2) avg_bonus2     -- �λ���� ��� avg �Լ��� ���ؼ�
from employees;

-- GROUP BY
select department_id
from employees
group by department_id;

-- Group by �� ���� �Լ� ����
select department_id, AVG(salary)
from employees
group by department_id;

-- �ϳ� �̻��� ���� �׷�ȭ �ϱ�
-- select/group by �� �����ϴ� ���̸��� ��ġ�ؾ� �Ѵ�.
select department_id,job_id, SUM(salary)
from employees
group by department_id,job_id;

-- �׷� �Լ��� �߸� ����� ���
-- �������� ���� �׷��Լ��� ȥ���ؼ� ����� ������ �������� ���� ����ϴ�
-- group by���� �ݵ�� �����ؾ� �Ѵ�.
select department_id, count(first_name)
from employees;

select department_id, count(first_name)
from employees
group by department_id;

-- group by�� ����
-- select
-- from
-- where
-- group by <- �� ��ġ���� ���

-- having: groub by �� ����� ���͸� �� �� ���
-- select
-- from
-- where
-- group by 
-- having
-- order by
select department_id, round(avg(salary),2)
from employees
group by department_id
having avg(salary) >= 8000;

select job_id, avg(salary) payroll
from employees
where job_id NOT LIKE 'SA%'
group by job_id
having avg(salary) > 8000
order by payroll;

-- grouping sets: �������� �׷���� �����ϰ� ó��, union all�� ����� ��ü
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id;
select job_id, round(avg(salary),2)
from employees
group by job_id;

-- ���� �̸��� grouping�� ���� ��ġ������ �ʴ´�.
select to_char(department_id), round(avg(salary),2)
from employees
group by department_id
union all
select job_id, round(avg(salary),2)
from employees
group by job_id;

-- �� ����� grouping sets �Լ��� ���� ����
select department_id, job_id, round(avg(salary),2)
from employees
group by grouping sets (department_id, job_id)
order by department_id, job_id;

-- grouping set Ȯ��
-- grouping set ( (�׷��1),(�׷��2) ...)
select department_id, job_id, manager_id, round(avg(salary),2) as avg_sal
from employees
group by grouping sets ((department_id, job_id),(job_id, manager_id))
order by department_id, job_id, manager_id;

-- ROLLUP, CUBE
-- ROLLUP: �� ������ �Ұ�, �� �Ұ谪�� �հ踦 ����, �׷캰�� �Ұ谪�� ����
-- �μ���, ������ �޿��� ��հ� ����� ���� ����϶�.
-- step1
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by department_id, job_id
order by department_id, job_id;

-- step2
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by rollup(department_id, job_id) -- ROLLUP�� ������ ���谡 �����ϴ�. /������ ���� �հ谡 ��µȴ�.
order by department_id, job_id;

-- CUBE: ROLLUP�� ����� �� ���� �Ұ赵 ���� ����
select department_id, job_id, round(avg(salary),2), count(*)
from employees
group by cube(department_id, job_id) 
order by department_id, job_id;
