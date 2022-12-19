
SELECT * FROM dual;
SELECT sysdate FROM dual;
SELECT initcap('javaspecialist') FROM dual;
SELECT lower('JavaSpecialist') FROM dual;
SELECT upper('JavaSpecialist') FROM dual;
SELECT length('JavaSpecialist') FROM dual;
SELECT length('자바전문가그룹') FROM dual;
SELECT lengthb('자바전문가그룹') FROM dual;
-- 현재 인코딩은 utf-8이기 때문에, EUC-KR 인코딩을 사용하면 10이 출력
SELECT * FROM NLS_DATABASE_PARAMETERS; --현재 인코딩 확인
SELECT concat('Java', 'Specialist') FROM dual;
SELECT substr('JavaSpecialist', 5, 7) FROM dual;
SELECT substr('자바전문가그룹', 3, 3) FROM dual;
SELECT substrb('자바전문가그룹', 7, 9) FROM dual;
SELECT instr('JavaSpecialist',  'S') FROM dual;
SELECT instr('JavaSpecialist',  'b') FROM dual;
SELECT instr('자바전문가그룹',  '전') FROM dual;
SELECT instrb('자바전문가그룹',  '전') FROM dual;
SELECT rpad(first_name, 10, '-') AS name, lpad(salary, 10, '*') AS sal FROM employees;
-- 주어진 자릿수 만큼 오른쪽(rpad) 또는 왼쪽(lpad)에 채운다.
SELECT ltrim('JavaSpecialist', 'Java') FROM dual;
SELECT ltrim(' JavaSpecialist') FROM dual;
SELECT trim(' JavaSpecialist ') FROM dual;
SELECT replace('JavaSpecialist', 'Java', 'BigData') FROM dual;
SELECT replace('Java Specialist', ' ', '') FROM dual;
SELECT translate('javaspecialist', 'abcdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyzabc') FROM dual;

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees;

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='austin';

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='Austin';

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  LOWER(last_name)='austin';

SELECT first_name, LENGTH(first_name), INSTR(first_name, 'a')
FROM   employees;

SELECT first_name, SUBSTR(first_name, 1, 3), CONCAT(first_name, last_name)
FROM   employees;

SELECT RPAD(first_name, 10, '-') AS name, LPAD(salary, 10, '*') AS sal 
FROM   employees;


SELECT 
  RPAD(substr(first_name, 1, 3), LENGTH(first_name), '*') AS name,
  LPAD(salary, 10, '*') AS salary
FROM 
  employees
WHERE
  LOWER(job_id)='it_prog';

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
INSERT INTO test_regexp VALUES('자바3');

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


SELECT ROUND(45.923,2), ROUND(45.923,0), ROUND(45.923,-1) 
FROM   DUAL;

SELECT TRUNC(45.923,2), TRUNC(45.923), TRUNC(45.923,-1) 
FROM   DUAL;


SELECT first_name, salary, commission_pct
FROM   employees
WHERE  job_id='IT_PROG';

SELECT SYSDATE 
FROM DUAL;

SELECT SYSTIMESTAMP 
FROM DUAL;

SELECT first_name, (SYSDATE - hire_date)/7 AS "Weeks"
FROM   employees
WHERE  department_id=60;

--MONTHS_BETWEEN
SELECT first_name, SYSDATE, hire_date, MONTHS_BETWEEN(SYSDATE, hire_date) AS workmonth
FROM employees
WHERE first_name='Diana'; --근무 한 개월 수를 출력, 

--ADD_MONTHS
SELECT first_name, hire_date, ADD_MONTHS(hire_date, 100)
FROM employees
WHERE first_name='Diana';

--NEXT_DAY, 돌아오는 가장 최근 요일 날짜
SELECT SYSDATE, NEXT_DAY(SYSDATE, '월') 
FROM dual; 

--날짜가 포함된 월의 마지막 날짜
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

--시간에 상관 없이 처리하고 싶을 때 사용
SELECT SYSDATE, ROUND(SYSDATE), TRUNC(SYSDATE) FROM dual;

--round와 trunc 함수에 반올림 하거나 절삭 할 단위를 지정할 수 있다.
SELECT TRUNC(SYSDATE, 'Month') FROM dual; --그 달의 첫 번째 날짜
SELECT TRUNC(SYSDATE, 'Year') FROM dual; --그 해의 첫 번째 날짜

SELECT ROUND(TO_DATE('17/03/16'), 'Month') FROM dual;
SELECT TRUNC(TO_DATE('17/03/16'), 'Month') FROM dual;
SELECT TRUNC(TO_DATE('17/03/16'), 'Day') FROM dual;

--암시적 형 변환
SELECT employee_id, first_name, department_id
FROM   employees
WHERE  department_id='40';

SELECT employee_id, first_name, hire_date
FROM   employees
WHERE  hire_date='03/06/17';

SELECT first_name, TO_CHAR(hire_date, 'MM/YY') AS HiredMonth
FROM   employees
WHERE  first_name='Steven';

SELECT first_name,
  TO_CHAR(hire_date, 'YYYY"년" MM"월" DD"일"') HIREDATE
FROM   employees;

SELECT first_name, 
  TO_CHAR(hire_date, 
          'fmDdspth "of" Month YYYY fmHH:MI:SS AM', 
          'NLS_DATE_LANGUAGE=english') AS HIREDATE
FROM   employees;


SELECT first_name, last_name, TO_CHAR(salary, '$999,999') SALARY
FROM   employees
WHERE  first_name='David';

SELECT TO_CHAR(2000000, '$999,999') SALARY
FROM   dual;

SELECT first_name, last_name, 
       salary*0.123456 SALARY1, 
       TO_CHAR(salary*0.123456, '$999,999.99') SALARY2
FROM   employees
WHERE  first_name='David';


SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003/06/17', 'YYYY/MM/DD');


SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003년06월17일', 'YYYY"년"MM"월"DD"일"');

SELECT '$5,500.00' - 4000 FROM dual;

--수정된 문장은...
SELECT to_number('$5,500.00', '$99,999.99') - 4000 FROM dual;

--모든 사원의 급여를 보너스를 포함하여 디스플레이 합니다.
SELECT first_name, salary + salary*nvl(commission_pct,0) AS ann_sal 
FROM employees;

SELECT first_name, 
  nvl2(commission_pct, salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

SELECT first_name, 
  COALESCE(salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

--보너스가 650달러 보다 작거나 보너스가 없는 사원들에게 상품권을 지급하려 합니다.
--해당 사원들의 이름과 보너스를 출력하세요.
SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE salary*commission_pct < 650; --4개 행

SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE COALESCE(salary*commission_pct, 0) < 650; --76개 행

SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE LNNVL(salary*commission_pct >= 650); --76개 행

SELECT  job_id, salary,
        DECODE(job_id, 'IT_PROG',    salary*1.10,
                       'FI_MGR',     salary*1.15,
                       'FI_ACCOUNT', salary*1.20, 
                                     salary)
        AS REVISED_SALARY
FROM    employees;


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

SELECT   TO_CHAR(NEXT_DAY(ADD_MONTHS(hire_date, 6), 'FRIDAY'), 'fmDay, Month ddth, YYYY') AS "Next 6 Month Review"
FROM     employees
ORDER BY hire_date;

--집합연산자
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
  TO_CHAR(hire_date, 'RRRR"년 입사"') AS year,
  TO_CHAR(hire_date, 'day') AS day,
  CASE WHEN TO_NUMBER(TO_CHAR(hire_date, 'YY')) >= 10
            THEN TO_CHAR(salary*1.10, '$999,999')
       WHEN TO_NUMBER(TO_CHAR(hire_date, 'YY')) >= 5
            THEN TO_CHAR(salary*1.05, '$999,999')
       ELSE TO_CHAR(salary,'$999,999')
  END AS "INCREASING_SALARY"
FROM employees;

SELECT first_name, salary, 
  TO_CHAR(hire_date, 'RRRR"년 입사"') AS year,
  TO_CHAR(hire_date, 'day') AS day,
  CASE WHEN TO_NUMBER(REGEXP_SUBSTR(hire_date, '[0-9]{2}')) >= 10
            THEN TO_CHAR(salary*1.10, '$999,999')
       WHEN TO_DATE(REGEXP_SUBSTR(hire_date, '[0-9]{2}'), 'RR') >= TO_DATE('05', 'RR')    
            THEN TO_CHAR(salary*1.05, '$999,999')
       ELSE TO_CHAR(salary,'$999,999')
  END AS "INCREASING_SALARY"
FROM employees;