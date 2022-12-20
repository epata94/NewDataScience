-- * �Լ��� ����
--  - ���� �� �Լ�: ����, ����, ��¥, ��ȯ, �Ϲ��Լ�
--  - ���� �� �Լ�

-- * ���� �� �Լ�
-- - ���ڿ� �Լ�
SELECT * FROM dual; -- dual: ����Ŭ ��ü���� �����Ǵ� ���̺�
SELECT sysdate FROM dual; 
SELECT initcap('javaspecialist') FROM dual; -- ù ���ڸ� �빮�ڷ�, �������� �ҹ��ڷ�
SELECT lower('JavaSpecialist') FROM dual;
SELECT upper('JavaSpecialist') FROM dual;
SELECT length('JavaSpecialist') FROM dual; -- ���ڿ� ���̼�
SELECT length('�ڹ��������׷�') FROM dual;

-- ���� ���ڵ��� utf-8�̱� ������, EUC-KR ���ڵ��� ����ϸ� 10�� ���
SELECT concat('Java', 'Specialist') FROM dual;
SELECT substr('JavaSpecialist', 5, 7) FROM dual; -- 5��° ���� ���� 7���� (�ε��� 1���� ����)
SELECT substr('�ڹ��������׷�', 3, 3) FROM dual;
SELECT instr('JavaSpecialist',  'S') FROM dual; -- ã�� ������ ��ġ ��ȯ
SELECT instr('JavaSpecialist',  'b') FROM dual; -- ��ã���� 0�� ��ȯ
SELECT instr('�ڹ��������׷�',  '��') FROM dual;
-- �־��� �ڸ��� ��ŭ ������(rpad) �Ǵ� ����(lpad)�� ä���.
SELECT rpad(first_name, 10, '-') AS name, lpad(salary, 10, '*') AS sal FROM employees;

SELECT ltrim('   JavaSpecialist   ') FROM dual; -- ������ ���ڸ� ���� �������� ����(default: ���鹮��)
SELECT rtrim('   JavaSpecialist   ') FROM dual; -- ������ ���ڸ� ������ �������� ����(default: ���鹮��)
SELECT trim('   JavaSpecialist   ') FROM dual; -- ������ ���ڸ� ���� �������� ����(default: ���鹮��)
SELECT ltrim('JavaSpecialist', 'Java') FROM dual; -- ������ ���ڴ� ������ ������� �ʴ´�.
-- Q] �Ʒ� ������ ���� �����?
SELECT ltrim('JavaSpecialist', 'Jav') FROM dual; 
SELECT ltrim('JavaSpecialist', 'avJ') FROM dual; 
SELECT ltrim('JavaSpecialist', 'vJa') FROM dual; 

SELECT replace('JavaSpecialist', 'Java', 'BigData') FROM dual;
SELECT replace('Java Specialist', ' ', '') FROM dual;
-- translate([���� ���ڿ�],[��Ī���ڿ�],[��ȯ���ڿ�]) 
SELECT translate('1234abcd', 'abcd', 'ABC') FROM dual;
SELECT TRANSLATE('hello world!!!', 'hw', 'HW') from dual;
SELECT TRANSLATE('hello world!!!', '!', '?') from dual;
SELECT TRANSLATE('010 1234 5678', ' ', '-') from dual;

SELECT TRANSLATE('$100', '$', '') as m from dual; -- ��ȯ���ڰ� ���ٸ� null�� ��Ī
-- Q] $100 ���� '$' ���� ���̸��� m���� (TRIM �Լ� ���)
SELECT TRIM(TRANSLATE('$100', '$', ' ')) as m from dual;
-- Q] $1,000,000 ���� '$',',' ���� ���̸��� m���� (TRIM �Լ� ���)
SELECT TRIM(TRANSLATE('$1,000,000', '$,', ' ')) as m from dual;

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees;

-- �ҹ��ڷ� �̸��� �˻��� ���� �ʴ´�.
SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='austin';

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='Austin';

-- �˻������ �����ϱ� ���Ͽ� lower�Լ��� ���
-- Q) �ҹ��� �̸����� �˻����� �ʴ� ������ �˻��� �ǵ��� ���ڿ� �Լ� ����� ��
SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  LOWER(last_name)='austin';

-- Q] employees ���̺��� �̸�, �̸��� ����, 'a' ������ ��ġ ��ȯ
SELECT first_name, LENGTH(first_name), INSTR(first_name, 'a')
FROM   employees;

-- Q] employees ���̺��� �̸�, �̸��� �տ� 3����, first name�� last name�� ���޾� �ٿ��� ���
SELECT first_name, SUBSTR(first_name, 1, 3), CONCAT(first_name, last_name)
FROM   employees;

SELECT RPAD(first_name, 10, '-') AS name, LPAD(salary, 10, '*') AS sal 
FROM   employees;

--  Q] ���� ���̵� it_prog �� ����� �̸� �տ� 3�ڸ��� ����ϰ� ������ 7�ڸ��� * ����ϰ� SALARY�� ��ü 10�ڸ��� ���������� ����ϰ� 
--- �������� * ����Ѵ�.
SELECT 
  -- ��ü ������ �������� �ʰ� �ؽ�Ʈ�� �Ϻθ� �����ִ� ����
  RPAD(substr(first_name, 1, 3), LENGTH(first_name), '*') AS name,
  LPAD(salary, 10, '*') AS salary
FROM 
  employees
WHERE
  LOWER(job_id)='it_prog';


-- ����ǥ���� ����
DROP TABLE test_regexp;
CREATE TABLE test_regexp (col1  VARCHAR2(10));
INSERT INTO test_regexp VALUES('ABCDE01234');
INSERT INTO test_regexp VALUES('01234ABCDE');
INSERT INTO test_regexp VALUES('abcde01234');
INSERT INTO test_regexp VALUES('01234abcde');
INSERT INTO test_regexp VALUES('1-234-5678');
INSERT INTO test_regexp VALUES('234-567890');

SELECT * 
FROM   test_regexp
WHERE  REGEXP_LIKE(col1,'[0-9][a-z]');

SELECT * 
FROM   test_regexp
WHERE  REGEXP_LIKE(col1,'[0-9]{3}-[0-9]{4}$');

SELECT * 
FROM   test_regexp
WHERE  REGEXP_LIKE(col1,'[[:digit:]]{3}-[[:digit:]]{4}$');


SELECT * 
FROM   test_regexp
WHERE  REGEXP_LIKE(col1,'[[:digit:]]{3}-[[:digit:]]{4}');


INSERT INTO test_regexp VALUES('@!=)(9&%$#');
INSERT INTO test_regexp VALUES('�ڹ�3');

SELECT col1, 
  REGEXP_INSTR(col1,'[0-9]')  data1,
  REGEXP_INSTR(COL1,'%')      data2
FROM   test_regexp;

SELECT col1, REGEXP_SUBSTR(col1,'[C-Z]+')
FROM   test_regexp;

SELECT col1, REGEXP_REPLACE(col1,'[0-2]+','*') 
FROM   test_regexp;

SELECT first_name, phone_number
FROM employees
WHERE regexp_like (phone_number, '^[0-9]{3}.[0-9]{3}.[0-9]{4}$');

SELECT first_name, phone_number
FROM employees
WHERE regexp_like (phone_number, '^[[:digit:]]{3}.[[:digit:]]{3}.[[:digit:]]{4}$');

SELECT first_name, 
  regexp_replace(phone_number, '[[:digit:]]{4}$', '****') AS phone,
  regexp_substr(phone_number, '[[:digit:]]{4}$') AS phone2
FROM employees
WHERE regexp_like (phone_number, '^[0-9]{3}.[0-9]{3}.[0-9]{4}$');

-- ����ǥ�� ���� ��

----------------------------------------------------------------

-- �����Լ�
-- �ݿø�
SELECT ROUND(45.923,2), ROUND(45.923,0), ROUND(45.923,-1) 
FROM   DUAL;

-- �ø�
select ceil(7.3) from dual;

-- ����
select floor(7.3) from dual;

-- trunc([������], [�ڸ���]) �ڸ�����ŭ �������� ���� ����
SELECT TRUNC(45.923,2), TRUNC(45.923), TRUNC(45.923,-1) 
FROM   DUAL;

select TO_DATE('2022-12-20','YYYY-MM-DD') as dt from dual;
-- �������� ����
select trunc(TO_DATE('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;
-- ������� ����
select trunc(TO_DATE('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;

-- ���밪
select abs(-1000) from dual;

-- ������
select power(2,3) from dual;

-- ������
select sqrt(100) from dual;

-- ������
select mod(10,3) from dual;

--------------------------------------------------
-- ��¥�Լ�
-- SYSDATE ������ ��¥�� ��ȯ, (YY/MM/DD �Ǵ� DD-MON-YY ����)
SELECT SYSDATE 
FROM DUAL;

-- SYSTIMESTAMP ������ ��¥�� �ð��� ��ȯ
SELECT SYSTIMESTAMP 
FROM DUAL;

-- Q] �μ� ��ȣ�� 60�� ����� �̸��� ������� �ٹ��� �ָ� 'Weeks' ���̸����� ���
SELECT first_name, (SYSDATE - hire_date)/7 AS "Weeks"
FROM   employees
WHERE  department_id=60;

--MONTHS_BETWEEN : �� ��¥ ������ �� ���� ��ȯ
SELECT first_name, SYSDATE, hire_date, MONTHS_BETWEEN(SYSDATE, hire_date) AS workmonth
FROM employees
WHERE first_name='Diana'; --�ٹ� �� ���� ���� ���, 

--ADD_MONTHS : �����Ͽ� ���� ����
SELECT first_name, hire_date, ADD_MONTHS(hire_date, 1)
FROM employees
WHERE first_name='Diana';

SELECT first_name, hire_date, ADD_MONTHS(hire_date, 200)
FROM employees
WHERE first_name='Diana';

--NEXT_DAY, ���ƿ��� ���� �ֱ� ���� ��¥
SELECT SYSDATE, NEXT_DAY(SYSDATE, '��') 
FROM dual; 
SELECT SYSDATE, NEXT_DAY(SYSDATE, 'ȭ') 
FROM dual; 

--��¥�� ���Ե� ���� ������ ��¥
SELECT SYSDATE, LAST_DAY(SYSDATE) FROM dual;

SELECT 
  TO_CHAR(LAST_DAY(TO_DATE('01', 'MM')), 'dd') AS "1",
  TO_CHAR(LAST_DAY(TO_DATE('02', 'MM')), 'dd') AS "2",
  TO_CHAR(LAST_DAY(TO_DATE('03', 'MM')), 'dd') AS "3",
  TO_CHAR(LAST_DAY(TO_DATE('04', 'MM')), 'dd') AS "4",
  TO_CHAR(LAST_DAY(TO_DATE('05', 'MM')), 'dd') AS "5",
  TO_CHAR(LAST_DAY(TO_DATE('06', 'MM')), 'dd') AS "6",
  TO_CHAR(LAST_DAY(TO_DATE('07', 'MM')), 'dd') AS "7",
  TO_CHAR(LAST_DAY(TO_DATE('08', 'MM')), 'dd') AS "8",
  TO_CHAR(LAST_DAY(TO_DATE('09', 'MM')), 'dd') AS "9",
  TO_CHAR(LAST_DAY(TO_DATE('10', 'MM')), 'dd') AS "10",
  TO_CHAR(LAST_DAY(TO_DATE('11', 'MM')), 'dd') AS "11",
  TO_CHAR(LAST_DAY(TO_DATE('12', 'MM')), 'dd') AS "12"
FROM dual;

--round�� trunc �Լ��� �ݿø� �ϰų� ���� �� ������ ������ �� �ִ�.
SELECT TRUNC(SYSDATE, 'Month') FROM dual; --�� ���� ù ��° ��¥
SELECT TRUNC(SYSDATE, 'Year') FROM dual; --�� ���� ù ��° ��¥

SELECT ROUND(TO_DATE('22/12/13'), 'Month') FROM dual;
SELECT ROUND(TO_DATE('22/12/16'), 'Month') FROM dual;
SELECT TRUNC(TO_DATE('22/12/16'), 'Month') FROM dual;
-- Day�� trunc�ϸ� �� ���� �Ͽ��Ϸ� ������ ���� ��ȯ�Ѵ�.
SELECT TRUNC(TO_DATE('22/12/20'), 'Day') FROM dual;
SELECT TRUNC(TO_DATE('22/12/21'), 'Day') FROM dual;
SELECT TRUNC(TO_DATE('22/12/27'), 'Day') FROM dual;



----------------------------------------------------
-- ��ȯ�Լ�
-- �Ͻ��� �� ��ȯ
-- number <-> character <-> date
SELECT employee_id, first_name, department_id
FROM   employees
WHERE  department_id='40';

SELECT employee_id, first_name, hire_date
FROM   employees
WHERE  hire_date='03/06/17';

-- ������ ������ �� �����ʹ� �Ͻ��� �� ��ȯ�� ���� �ʴ´�.
SELECT '$5,500.00' - 4000 FROM dual;
-- ������ ������ �� �����ʹ� �Ͻ��� �� ��ȯ�� ���� �ʴ´�.
SELECT employee_id, first_name, hire_date
FROM   employees
WHERE  hire_date='03�� 06�� 17��';

-- ����� �� ��ȯ
-- TO_CHAR: ��¥�� ��¥������ �����Ͽ� ���ڷ� ��ȯ, TO_CHAR([��¥],[��¥����])
SELECT first_name, TO_CHAR(hire_date, 'MM/YY') AS HiredMonth
FROM   employees
WHERE  first_name='Steven';

SELECT first_name,
  TO_CHAR(hire_date, 'YYYY"��" MM"��" DD"��"') HIREDATE
FROM   employees;


SELECT first_name, last_name, TO_CHAR(salary, '$999,999') SALARY
FROM   employees
WHERE  first_name='David';

-- TO_CHAR: ���ڸ� ���������� �����Ͽ� ���ڷ� ��ȯ, TO_CHAR([����],[��������])
-- ���亸�� ū ���� '#'���� ǥ��
SELECT TO_CHAR(2000000, '$999,999') SALARY
FROM   dual;

SELECT TO_CHAR(2000000, '$9,999,999') SALARY
FROM   dual;

-- �տ� 0�� ��� (��ǥ �ݾ��� ���� ��� ���)
SELECT TO_CHAR(2000000, '$009,999,999') SALARY
FROM   dual;

-- �Ҽ��� ���� ó���� ���� ������ ��µ��� �ʴ´�.
SELECT TO_CHAR(2000000.45, '$009,999,999') SALARY
FROM   dual;

-- �Ҽ��� ó��
SELECT TO_CHAR(2000000.45, '$999,999,999.99') SALARY
FROM   dual;

-- ����ȭ�� ��ȣ���
SELECT TO_CHAR(2000000.45, 'L999,999,999.99') SALARY
FROM   dual;

-- Q] employees ���̺� �̸��� David�� �̸�(first_name), ��, �޿�, 15.23%�λ�� �λ�ݾ��� salary1����, ������ ���� $1,446.85 ������ ������ �λ�ݾ��� salary2���� ����ϼ���.
SELECT first_name, last_name, salary, 
       salary*0.15 SALARY1, 
       TO_CHAR(salary*0.1523, '$999,999.99') SALARY2
FROM   employees
WHERE  first_name='David';

-- ���ϴ� ��¥ �������� �˻��ϱ�
SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003/06/17', 'YYYY/MM/DD');


SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003��06��17��', 'YYYY"��"MM"��"DD"��"');

-- Q]������ ���� '2003/06/17' ��µǵ��� ��¥ Ÿ���� �����ϼ���.
SELECT first_name, to_char(hire_date,'YYYY/MM/DD') as hire_date
FROM   employees
WHERE  hire_date='03/06/17';

-- Q]������ ���� '2003-06-17' ��µǵ��� ��¥ Ÿ���� �����ϼ���.
SELECT first_name, to_char(hire_date,'YYYY-MM-DD') as hire_date
FROM   employees
WHERE  hire_date='03/06/17';

SELECT '$5,500.00' - 4000 FROM dual;

--������ ������..
-- to_number: ���� ��Ʈ���� ���� �������� ��ȯ
SELECT to_number('$5,500.00', '$99,999.99') FROM dual;
SELECT to_number('$5,500.00', '$99,999.99') - 4000 FROM dual;


-- NVL: Null ��ȯ
-- NVL ([������],[���̸� ��ȯ�Ǵ� ��])
select nvl(1000, 100) from dual;
select nvl(null, 100) from dual;



-- q] ��� ����� �޿��� ���ʽ��� �����Ͽ� ���÷��� �մϴ�.
-- null���� ��� ������ null�̴�.
-- �Ʒ� ���� ����� �����ְ� ���� Ǯ�� �Ѵ�.
select commission_pct from employees;
SELECT first_name, salary + salary*commission_pct AS ann_sal 
FROM employees;

SELECT first_name, salary + salary*nvl(commission_pct,0) AS ann_sal 
FROM employees;


-- NVL2 ([������],[���� �ƴϸ� ��ȯ�Ǵ� ��], [���̸� ��ȯ�Ǵ� ��])
select nvl2(1.2, 1000*1.2,1000) from dual;
select nvl2(null, 1000*1.2,1000) from dual;

-- q] �� ������ NVL2�Լ��� �����ϸ� Ǯ�����.
SELECT first_name, 
  nvl2(commission_pct, salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

-- COALESCE(expr1, expr2 ..) : ���� �ƴ� ù��° ������ ���� ����
-- �ٸ� Ȱ�뿹) �� �����ͺ��̽����� ���� ��ȭ��ȣ�� ����ϰ� ���� ���
-- �޴���, ����ȭ, ȸ����ȭ�� �켱������ ���� �ִ� ������ �˻��ϰ� ���� �� ������
SELECT first_name, 
  COALESCE(salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

--���ʽ��� 650�޷� ���� �۰ų� ���ʽ��� ���� ����鿡�� ��ǰ���� �����Ϸ� �մϴ�.
--�ش� ������� �̸��� ���ʽ��� ����ϼ���.
SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE salary*commission_pct < 650; --4�� �� (commision_pct �ִ�(NULL�� �ƴ�) ���� ���)

SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE COALESCE(salary*commission_pct, 0) < 650; --76�� �� (0���� ����)

-- LNNVL: LNNVL(expr1) expr1 ����� FALSE �Ǵ� UNKNOWN�̸� TRUE�� ��ȯ
-- ������ �ݴ� ���ǿ� ���Ͽ� �˻��ϰ� ���� �� Ȱ��
SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE LNNVL(salary*commission_pct >= 650); --76�� ��



-- DECODE: DECODE(Column or expression, search1, result
--                                      [, search2, result2, ...]
select decode('java','java','�鿣�� ���') as language from dual;
select decode('java','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���') as language
from dual;

select decode('html','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���') as language
from dual;

select decode('python','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���') as language
from dual;

select decode('css','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���') as language
from dual;

select decode('css','java','�鿣�� ���'
                    ,'html','����Ʈ ���'
                    ,'python','�����ͻ��̾� ���',
                    '��Ÿ���') as language
from dual;

-- Q] ���� ���̺��� ���� id, �޿� �׸��� ���� id�� IT_PROG, FI_MGR, FT_ACCOUNT�� ���� �޿��� 10,15,20% �λ��� �޿��� revised_salary ���� ����Ѵ�.
SELECT  job_id, salary,
        DECODE(job_id, 'IT_PROG',    salary*1.10,
                       'FI_MGR',     salary*1.15,
                       'FI_ACCOUNT', salary*1.20, 
                                     salary)
        AS REVISED_SALARY
FROM    employees;

-- CASE ~ WHEN ~ THEN
SELECT job_id, salary,
  CASE job_id WHEN 'IT_PROG'    THEN salary*1.10
              WHEN 'FI_MGE'     THEN salary*1.15
              WHEN 'FI_ACCOUNT' THEN salary*1.20
       ELSE salary
  END AS REVISED_SALARY
FROM   employees;

SELECT job_id, salary,
  CASE WHEN job_id='IT_PROG'    THEN salary*1.10
       WHEN job_id='FI_MGE'     THEN salary*1.15
       WHEN job_id='FI_ACCOUNT' THEN salary*1.20
       ELSE salary
  END AS REVISED_SALARY
FROM   employees;


-- ��ø�Լ�
SELECT   ADD_MONTHS(hire_date, 6) -- �Ի��� 3����
FROM     employees
ORDER BY hire_date;

SELECT   NEXT_DAY(ADD_MONTHS(hire_date, 6), '��') -- ���� �ݿ���
FROM     employees
ORDER BY hire_date;

SELECT   TO_CHAR(NEXT_DAY(ADD_MONTHS(hire_date, 6), '��'), 'YYYY-MM-DD') AS "������ ���� �����" --�� ��¥
FROM     employees
ORDER BY hire_date;

--���տ�����
--UNION
SELECT employee_id, first_name
FROM   employees
WHERE  hire_date LIKE '04%'
UNION
SELECT employee_id, first_name
FROM   employees
WHERE  department_id=20;

--UNION ALL
SELECT employee_id, first_name
FROM   employees
WHERE  hire_date LIKE '04%'
UNION  ALL
SELECT employee_id, first_name
FROM   employees
WHERE  department_id=20;

--INTERSECT
SELECT employee_id, first_name
FROM   employees
WHERE  hire_date LIKE '04%'
INTERSECT
SELECT employee_id, first_name
FROM   employees
WHERE  department_id=20;

--MINUS
SELECT employee_id, first_name
FROM   employees
WHERE  hire_date LIKE '04%'
MINUS
SELECT employee_id, first_name
FROM   employees
WHERE  department_id=20;


--10
SELECT first_name, salary, 
  TO_CHAR(hire_date, 'RRRR"�� �Ի�"') AS year,
  TO_CHAR(hire_date, 'day') AS day,
  CASE WHEN TO_NUMBER(TO_CHAR(hire_date, 'YY')) >= 10
            THEN TO_CHAR(salary*1.10, '$999,999')
       WHEN TO_NUMBER(TO_CHAR(hire_date, 'YY')) >= 5
            THEN TO_CHAR(salary*1.05, '$999,999')
       ELSE TO_CHAR(salary,'$999,999')
  END AS "INCREASING_SALARY"
FROM employees;

SELECT first_name, salary, 
  TO_CHAR(hire_date, 'RRRR"�� �Ի�"') AS year,
  TO_CHAR(hire_date, 'day') AS day,
  CASE WHEN TO_NUMBER(REGEXP_SUBSTR(hire_date, '[0-9]{2}')) >= 10
            THEN TO_CHAR(salary*1.10, '$999,999')
       WHEN TO_DATE(REGEXP_SUBSTR(hire_date, '[0-9]{2}'), 'RR') >= TO_DATE('05', 'RR')    
            THEN TO_CHAR(salary*1.05, '$999,999')
       ELSE TO_CHAR(salary,'$999,999')
  END AS "INCREASING_SALARY"
FROM employees;