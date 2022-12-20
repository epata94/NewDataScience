-- * �Լ�
-- - ������ �Լ�: ���� �࿡���� ���� �����ϰ� �ະ�� �ϳ��� ����� ����
-- - ������ �Լ�: ������ ���� �����Ͽ� ���� �׷�� �ϳ��� ����� ���� (��: count())
--  > ������ �Լ�: �����Լ�, �����Լ�, ��¥ �Լ�, ��ȯ�Լ�, �Ϲ��Լ�
-----------------------------------
--          �����Լ�
-----------------------------------

-- dual ���̺�: ����Ŭ ��ü���� ���� Ȯ���ϱ� �뵵�� �����ϴ� ���̺�
select * from dual;

-- initcap: �ܾ �������� ù ���ڸ� �빮�ڷ� �������� �ҹ��ڷ� ��ȯ�ϴ� �Լ�
select initcap('python specialist') from dual;
select initcap('pythonSpecialist') from dual;
-- lower: ��ü�� �ҹ��ڷ� ����� �Լ�
select lower('pythonSpecialist') from dual;
-- upper: ��ü�� �빮�ڷ� ����� �Լ�
select upper('pythonSpecialist') from dual;
-- length: ���ڿ� ���̼��� ��ȯ�ϴ� �Լ�
select length('pythonSpecialist') from dual;
select length('���̽�������') from dual;
-- concat: �� ���ڿ��� �����Ͽ� ��ȯ
select concat('���̽�','������') from dual;
-- substr: substr([���ڿ�],[�����ε���],[���ε���]) 
-- ���ڿ��� �������� �����ε������� �� �ε����� ���ڿ� ��ȯ (���ڿ��� ���� �ε����� 1����)
select substr('���̽�������',1,3) from dual;
-- instr: instr([���ڿ�],[ã�����ϴ� ���ڿ�]) ���ڿ��� �������� ã�����ϴ� ���ڿ��� 
-- �ε��� ��ȯ
select instr('���̽�������','��') from dual;
select instr('���̽�������','��') from dual; -- ��ġ�� �Ǵ� ���ڿ��� ������ 0 ��ȯ
-- rpad/lpad: �־��� �ڸ��� ��ŭ ������(rpad)/���ʿ� ������ ���ڿ��� ä���.
-- rpad/lpad([���ڿ�],[ä���ڸ���],[ä�﹮��])
select rpad('ȫ�浿',10,'*') from dual;
select lpad('ȫ�浿',10,'*') from dual;
-- Q] �������̺��� �̸� 10�ڸ��� ������ �������� '-'�� ä��� 
-- �޿� 10�ڸ��� ������ ������ '*'�� ä���� ����ϼ���.
select rpad(first_name,10,'-') as name, lpad(salary,10,'*') as sal
from employees;

-- ltrim/rtrim/trim:���ڿ��� �������� ������ ���ڸ� ���� ����, ������, �������� ����
-- ltrim/rtrim([���ڿ�],[�����ҹ��ڿ�]) ������ ���ڿ� �⺻���� ���鹮��
-- trim([���ڿ�]) ���� ���� ���� ����
select ltrim('   ���̽� ������   ') as name from dual;
-- ��Ī�� ������ �� as�� ������ �� �ִ�.
select ltrim('   ���̽� ������   ') name from dual;
select rtrim('   ���̽� ������   ') name from dual;
select trim('   ���̽� ������   ') name from dual;
select ltrim('���̽����������̽�','���̽�') name from dual;
select rtrim('���̽����������̽�','���̽�') name from dual;
-- trim �Լ��� ���� ���鹮�ڸ� ������ �� �ִ�. ���ڰ� 1���̱� ������
-- �Ʒ� �ڵ�� ������ �߻��Ѵ�.
select trim('���̽����������̽�','���̽�') name from dual;

-- ltrim ��ȭ
select ltrim('JavaSpecialist','Java') name from dual;
-- ������ ���ڿ��� ������ ������ ������� �ʴ´�.
select ltrim('JavaSpecialist','Jav') name from dual; 
-- ���Ŵ� �������� ���ϴ� ���ڸ� ���ʹ߰� �� ������ �����Ѵ�.
select ltrim('JavaSpecialist','avJ') name from dual; 
select ltrim('JavaSpecialist','vJa') name from dual;

-- replace
select replace('PythonSpecalist','Python','BigData') from dual;
select replace('Python Specalist', ' ', '') from dual; -- ���鹮�� ����

-- translate([���� ���ڿ�],[��Ī���ڿ�],[��ȯ���ڿ�])
select translate('1234abcd','abcd','ABC') from dual;
select translate('hello world!!!', 'hw', 'HW') from dual;
select translate('hello world!!!', '!', '?') from dual;
select translate('$100', '$', '') from dual; -- ��ȯ�� ���ڰ� ���ٸ� null�� ��ȯ
select translate('$100', '$', ' ') as m from dual; -- ��ȯ�� ���ڰ� ���ٸ� null�� ��ȯ
select translate('$1,000,000', '$,', ' ') as m from dual;

-- Q] ���� ���̺��� �̸��� �̸��״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��δ빮�ڷ� ����غ�����.
select last_name, lower(last_name),initcap(last_name),upper(last_name)
from employees;

-- Q] ���� ���̺��� �̸��� 'austin'�� ������
-- �̸��� �̸��״��, �ҹ��ڷ�, ù���ڸ� �빮�ڷ�, ��δ빮�ڷ� ����غ�����.
-- �˻��� �ҹ��ڷ� �Ұ�
select last_name, lower(last_name),initcap(last_name),upper(last_name)
from employees
where lower(last_name)='austin';

-- Q] ���� ���̵� it_prog�� (�ݵ�� �ҹ��ڷ� �˻��ؾ���) �����
-- �̸��� �տ� 3�ڸ��� ����ϰ� ������ �ڸ��� * ����ϸ�
-- salary�� ��ü 10�ڸ��� ������ ����ϰ� �������� * ����Ѵ�.
select 
    rpad (substr(first_name, 1,3), length(first_name),'*') as name,
    lpad (salary, 10, '*') as salary
from employees
where lower(job_id)='it_prog';

-----------------------------------
--          �����Լ�
-----------------------------------
-- �ݿø�: round
select round(45.966,2), round(45.923,0),round(45.923,-1)
from dual;

-- �ø�: ceil
select ceil(7.3) from dual;

-- ����: floor
select floor(7.3) from dual;

-- ����: trunc([������],[�ڸ���]) �ڸ��� ��ŭ �������� ���� ����
select trunc(45.923,2), trunc(45.923), trunc(45.923,-1)
from dual;

-- to_date([���ڽ�Ʈ��],[����])
select to_date('2022-12-20','YYYY-MM-DD') as dt from dual;

-- trunc�Լ��� �����Ͽ� �ſ� ù°���� ����
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;
-- Q] trunc�Լ��� �����Ͽ� 2022�� ù°���� ����
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;

-- DD�� �����ϸ� �ϴ����� ������ ��¥�� �����Ƿ� ���ϰ��� ��ȯ
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DD') as dt from dual;

-- �� ���� ù��° �Ͽ����� ��ȯ
select trunc(to_date('2022-12-20','YYYY-MM-DD'),'DAY') as dt from dual;
select trunc(to_date('2022-12-21','YYYY-MM-DD'),'DAY') as dt from dual;
select trunc(to_date('2022-12-31','YYYY-MM-DD'),'DAY') as dt from dual;

-- ���밪
select abs(-1000) from dual;

-- ������
select power(2,3) from dual;

-- ������
select sqrt(100) from dual;

-- ������
select mod(10,3) from dual;

-----------------------------------
--          ��¥�Լ�
-----------------------------------

-- SYSDATE: ������ ��¥�� ��ȯ(YY/MM/DD)
select sysdate from dual;

-- SYSTIMESTAMP: ������ ��¥�� �ð��� ��ȯ
select systimestamp from dual;

-- Q] �μ� ��ȣ�� 60�� ����� �̸��� ������� �ٹ��� �ָ� 'Weeks' �� �̸����� ���
select first_name,(SYSDATE-hire_date)/7 as "weeks"
from employees
where department_id=60;

-- MONTHS_BETWEEN: �� ��¥ ������ �� ���� ��ȯ
select first_name, SYSDATE, hire_date, months_between(sysdate, hire_date) as workmonth
from employees
where first_name='Diana';

-- ADD_MONTHS: �����Ͽ� ���� ����
select first_name, hire_date, ADD_MONTHS(hire_date, 1)
from employees
where first_name='Diana';

-- Q] �� ������ Ȱ���Ͽ� Diana�� �Ի��� 200������ ���� ��¥�� ���ϼ���.
select first_name, hire_date, ADD_MONTHS(hire_date, 200)
from employees
where first_name='Diana';

-- NEXT_DAT, ���ƿ��°��� �ֱ� ���� ��¥
select sysdate, next_day(sysdate,'��') from dual;
select sysdate, next_day(sysdate,'��') from dual;

-- LAST_DAY: �ش� ���� ���Ե� ���� ������ ��¥
select sysdate, last_day(sysdate) from dual;

-- Q] 1������ 12������ ������ ���� ����ϼ���. ������ ���� �� ���ڷ� ǥ��
SELECT 
  TO_CHAR(LAST_DAY(TO_DATE('01', 'MM')), 'dd') AS "1",
  TO_CHAR(LAST_DAY(TO_DATE('02', 'MM')), 'dd') AS "2",
  TO_CHAR(LAST_DAY(TO_DATE('03', 'MM')), 'dd') AS "3",
  TO_CHAR(LAST_DAY(TO_DATE('04', 'MM')), 'dd') AS "4",
  TO_CHAR(LAST_DAY(TO_DATE('05', 'MM')), 'dd') AS "5",
  TO_CHAR(LAST_DAY(TO_DATE('06', 'MM')), 'dd') AS "6",
  TO_CHAR(LAST_DAY(TO_DATE('07', 'MM')), 'dd') AS "7",
  TO_CHAR(LAST_DAY(TO_DATE('08', 'MM')), 'dd') AS "8",
  TO_CHAR(LAST_DAY(TO_DATE('09', 'MM')), 'dd') AS "9"
  from dual;