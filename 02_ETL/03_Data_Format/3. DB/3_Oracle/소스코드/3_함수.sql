-- * 함수의 종류
--  - 단일 행 함수: 문자, 숫자, 날짜, 변환, 일반함수
--  - 다중 행 함수

-- * 단일 행 함수
-- - 문자열 함수
SELECT * FROM dual; -- dual: 오라클 자체에서 제공되는 테이블
SELECT sysdate FROM dual; 
SELECT initcap('javaspecialist') FROM dual; -- 첫 문자만 대문자로, 나머지는 소문자로
SELECT lower('JavaSpecialist') FROM dual;
SELECT upper('JavaSpecialist') FROM dual;
SELECT length('JavaSpecialist') FROM dual; -- 문자열 길이수
SELECT length('자바전문가그룹') FROM dual;

-- 현재 인코딩은 utf-8이기 때문에, EUC-KR 인코딩을 사용하면 10이 출력
SELECT concat('Java', 'Specialist') FROM dual;
SELECT substr('JavaSpecialist', 5, 7) FROM dual; -- 5번째 문자 부터 7문자 (인덱스 1부터 시작)
SELECT substr('자바전문가그룹', 3, 3) FROM dual;
SELECT instr('JavaSpecialist',  'S') FROM dual; -- 찾는 문자의 위치 반환
SELECT instr('JavaSpecialist',  'b') FROM dual; -- 못찾으면 0을 반환
SELECT instr('자바전문가그룹',  '전') FROM dual;
-- 주어진 자릿수 만큼 오른쪽(rpad) 또는 왼쪽(lpad)에 채운다.
SELECT rpad(first_name, 10, '-') AS name, lpad(salary, 10, '*') AS sal FROM employees;

SELECT ltrim('   JavaSpecialist   ') FROM dual; -- 지정한 문자를 왼쪽 기준으로 제거(default: 공백문자)
SELECT rtrim('   JavaSpecialist   ') FROM dual; -- 지정한 문자를 오른쪽 기준으로 제거(default: 공백문자)
SELECT trim('   JavaSpecialist   ') FROM dual; -- 지정한 문자를 양쪽 기준으로 제거(default: 공백문자)
SELECT ltrim('JavaSpecialist', 'Java') FROM dual; -- 지정한 문자는 순서를 고려하지 않는다.
-- Q] 아래 쿼리의 예상 결과는?
SELECT ltrim('JavaSpecialist', 'Jav') FROM dual; 
SELECT ltrim('JavaSpecialist', 'avJ') FROM dual; 
SELECT ltrim('JavaSpecialist', 'vJa') FROM dual; 

SELECT replace('JavaSpecialist', 'Java', 'BigData') FROM dual;
SELECT replace('Java Specialist', ' ', '') FROM dual;
-- translate([원본 문자열],[매칭문자열],[변환문자열]) 
SELECT translate('1234abcd', 'abcd', 'ABC') FROM dual;
SELECT TRANSLATE('hello world!!!', 'hw', 'HW') from dual;
SELECT TRANSLATE('hello world!!!', '!', '?') from dual;
SELECT TRANSLATE('010 1234 5678', ' ', '-') from dual;

SELECT TRANSLATE('$100', '$', '') as m from dual; -- 변환문자가 없다면 null로 매칭
-- Q] $100 에서 '$' 제거 열이름은 m으로 (TRIM 함수 사용)
SELECT TRIM(TRANSLATE('$100', '$', ' ')) as m from dual;
-- Q] $1,000,000 에서 '$',',' 제거 열이름은 m으로 (TRIM 함수 사용)
SELECT TRIM(TRANSLATE('$1,000,000', '$,', ' ')) as m from dual;

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees;

-- 소문자로 이름이 검색이 되지 않는다.
SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='austin';

SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  last_name='Austin';

-- 검색방식을 통일하기 위하여 lower함수를 사용
-- Q) 소문자 이름으로 검색되지 않는 예제를 검색이 되도록 문자열 함수 사용할 것
SELECT last_name, LOWER(last_name), INITCAP(last_name), UPPER(last_name)
FROM   employees
WHERE  LOWER(last_name)='austin';

-- Q] employees 테이블에서 이름, 이름별 길이, 'a' 문자의 위치 반환
SELECT first_name, LENGTH(first_name), INSTR(first_name, 'a')
FROM   employees;

-- Q] employees 테이블에서 이름, 이름중 앞에 3글자, first name과 last name을 연달아 붙여서 출력
SELECT first_name, SUBSTR(first_name, 1, 3), CONCAT(first_name, last_name)
FROM   employees;

SELECT RPAD(first_name, 10, '-') AS name, LPAD(salary, 10, '*') AS sal 
FROM   employees;

--  Q] 직무 아이디가 it_prog 인 사원의 이름 앞에 3자리만 출력하고 나머지 7자리는 * 출력하고 SALARY는 전체 10자리중 오른쪽으로 출력하고 
--- 나머지는 * 출력한다.
SELECT 
  -- 전체 내용을 보여주지 않고 텍스트의 일부만 보여주는 응용
  RPAD(substr(first_name, 1, 3), LENGTH(first_name), '*') AS name,
  LPAD(salary, 10, '*') AS salary
FROM 
  employees
WHERE
  LOWER(job_id)='it_prog';


-- 정규표현식 시작
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

-- 정규표현 응용 끝

----------------------------------------------------------------

-- 숫자함수
-- 반올림
SELECT ROUND(45.923,2), ROUND(45.923,0), ROUND(45.923,-1) 
FROM   DUAL;

-- 올림
select ceil(7.3) from dual;

-- 버림
select floor(7.3) from dual;

-- trunc([데이터], [자리수]) 자리수만큼 데이터의 값을 절삭
SELECT TRUNC(45.923,2), TRUNC(45.923), TRUNC(45.923,-1) 
FROM   DUAL;

select TO_DATE('2022-12-20','YYYY-MM-DD') as dt from dual;
-- 월단위로 절사
select trunc(TO_DATE('2022-12-20','YYYY-MM-DD'),'MM') as dt from dual;
-- 년단위로 절사
select trunc(TO_DATE('2022-12-20','YYYY-MM-DD'),'YYYY') as dt from dual;

-- 절대값
select abs(-1000) from dual;

-- 제곱값
select power(2,3) from dual;

-- 제곱근
select sqrt(100) from dual;

-- 나머지
select mod(10,3) from dual;

--------------------------------------------------
-- 날짜함수
-- SYSDATE 현재의 날짜를 반환, (YY/MM/DD 또는 DD-MON-YY 형식)
SELECT SYSDATE 
FROM DUAL;

-- SYSTIMESTAMP 현재의 날짜와 시간을 반환
SELECT SYSTIMESTAMP 
FROM DUAL;

-- Q] 부서 번호가 60인 사원의 이름과 현재까지 근무한 주를 'Weeks' 열이름으로 출력
SELECT first_name, (SYSDATE - hire_date)/7 AS "Weeks"
FROM   employees
WHERE  department_id=60;

--MONTHS_BETWEEN : 두 날짜 사이의 월 수를 반환
SELECT first_name, SYSDATE, hire_date, MONTHS_BETWEEN(SYSDATE, hire_date) AS workmonth
FROM employees
WHERE first_name='Diana'; --근무 한 개월 수를 출력, 

--ADD_MONTHS : 기준일에 월을 더함
SELECT first_name, hire_date, ADD_MONTHS(hire_date, 1)
FROM employees
WHERE first_name='Diana';

SELECT first_name, hire_date, ADD_MONTHS(hire_date, 200)
FROM employees
WHERE first_name='Diana';

--NEXT_DAY, 돌아오는 가장 최근 요일 날짜
SELECT SYSDATE, NEXT_DAY(SYSDATE, '월') 
FROM dual; 
SELECT SYSDATE, NEXT_DAY(SYSDATE, '화') 
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

--round와 trunc 함수에 반올림 하거나 절삭 할 단위를 지정할 수 있다.
SELECT TRUNC(SYSDATE, 'Month') FROM dual; --그 달의 첫 번째 날짜
SELECT TRUNC(SYSDATE, 'Year') FROM dual; --그 해의 첫 번째 날짜

SELECT ROUND(TO_DATE('22/12/13'), 'Month') FROM dual;
SELECT ROUND(TO_DATE('22/12/16'), 'Month') FROM dual;
SELECT TRUNC(TO_DATE('22/12/16'), 'Month') FROM dual;
-- Day로 trunc하면 그 주의 일요일로 절삭한 값을 반환한다.
SELECT TRUNC(TO_DATE('22/12/20'), 'Day') FROM dual;
SELECT TRUNC(TO_DATE('22/12/21'), 'Day') FROM dual;
SELECT TRUNC(TO_DATE('22/12/27'), 'Day') FROM dual;



----------------------------------------------------
-- 변환함수
-- 암시적 형 변환
-- number <-> character <-> date
SELECT employee_id, first_name, department_id
FROM   employees
WHERE  department_id='40';

SELECT employee_id, first_name, hire_date
FROM   employees
WHERE  hire_date='03/06/17';

-- 하지만 서식이 들어간 데이터는 암시적 형 변환이 되지 않는다.
SELECT '$5,500.00' - 4000 FROM dual;
-- 하지만 서식이 들어간 데이터는 암시적 형 변환이 되지 않는다.
SELECT employee_id, first_name, hire_date
FROM   employees
WHERE  hire_date='03년 06월 17일';

-- 명시적 형 변환
-- TO_CHAR: 날짜를 날짜포멧을 적용하여 문자로 변환, TO_CHAR([날짜],[날짜포멧])
SELECT first_name, TO_CHAR(hire_date, 'MM/YY') AS HiredMonth
FROM   employees
WHERE  first_name='Steven';

SELECT first_name,
  TO_CHAR(hire_date, 'YYYY"년" MM"월" DD"일"') HIREDATE
FROM   employees;


SELECT first_name, last_name, TO_CHAR(salary, '$999,999') SALARY
FROM   employees
WHERE  first_name='David';

-- TO_CHAR: 숫자를 숫자포멧을 적용하여 문자로 변환, TO_CHAR([숫자],[숫자포멧])
-- 포멧보다 큰 경우는 '#'으로 표기
SELECT TO_CHAR(2000000, '$999,999') SALARY
FROM   dual;

SELECT TO_CHAR(2000000, '$9,999,999') SALARY
FROM   dual;

-- 앞에 0을 출력 (목표 금액이 있을 경우 고려)
SELECT TO_CHAR(2000000, '$009,999,999') SALARY
FROM   dual;

-- 소수점 이하 처리를 하지 않으면 출력되지 않는다.
SELECT TO_CHAR(2000000.45, '$009,999,999') SALARY
FROM   dual;

-- 소수점 처리
SELECT TO_CHAR(2000000.45, '$999,999,999.99') SALARY
FROM   dual;

-- 지역화폐 기호사용
SELECT TO_CHAR(2000000.45, 'L999,999,999.99') SALARY
FROM   dual;

-- Q] employees 테이블에 이름이 David인 이름(first_name), 성, 급여, 15.23%인상된 인상금액을 salary1열에, 다음과 같은 $1,446.85 형식을 적용한 인상금액을 salary2열에 출력하세요.
SELECT first_name, last_name, salary, 
       salary*0.15 SALARY1, 
       TO_CHAR(salary*0.1523, '$999,999.99') SALARY2
FROM   employees
WHERE  first_name='David';

-- 원하는 날짜 포멧으로 검색하기
SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003/06/17', 'YYYY/MM/DD');


SELECT first_name, hire_date
FROM   employees
WHERE  hire_date=TO_DATE('2003년06월17일', 'YYYY"년"MM"월"DD"일"');

-- Q]다음과 같이 '2003/06/17' 출력되도록 날짜 타입을 변경하세요.
SELECT first_name, to_char(hire_date,'YYYY/MM/DD') as hire_date
FROM   employees
WHERE  hire_date='03/06/17';

-- Q]다음과 같이 '2003-06-17' 출력되도록 날짜 타입을 변경하세요.
SELECT first_name, to_char(hire_date,'YYYY-MM-DD') as hire_date
FROM   employees
WHERE  hire_date='03/06/17';

SELECT '$5,500.00' - 4000 FROM dual;

--수정된 문장은..
-- to_number: 문자 스트링을 숫자 형식으로 변환
SELECT to_number('$5,500.00', '$99,999.99') FROM dual;
SELECT to_number('$5,500.00', '$99,999.99') - 4000 FROM dual;


-- NVL: Null 변환
-- NVL ([원본값],[널이면 변환되는 값])
select nvl(1000, 100) from dual;
select nvl(null, 100) from dual;



-- q] 모든 사원의 급여를 보너스를 포함하여 디스플레이 합니다.
-- null과의 모든 연산은 null이다.
-- 아래 연산 결과를 보여주고 문제 풀게 한다.
select commission_pct from employees;
SELECT first_name, salary + salary*commission_pct AS ann_sal 
FROM employees;

SELECT first_name, salary + salary*nvl(commission_pct,0) AS ann_sal 
FROM employees;


-- NVL2 ([원본값],[널이 아니면 반환되는 값], [널이면 변환되는 값])
select nvl2(1.2, 1000*1.2,1000) from dual;
select nvl2(null, 1000*1.2,1000) from dual;

-- q] 위 예제를 NVL2함수를 적용하며 풀어보세요.
SELECT first_name, 
  nvl2(commission_pct, salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

-- COALESCE(expr1, expr2 ..) : 널이 아닌 첫번째 인자의 값을 선택
-- 다른 활용예) 고객 데이터베이스에서 고객의 전화번호를 출력하고 싶은 경우
-- 휴대폰, 집전화, 회사전화중 우선순위별 값이 있는 순위로 검색하고 싶을 때 유용함
SELECT first_name, 
  COALESCE(salary + (salary*commission_pct), salary) AS ann_sal 
FROM employees;

--보너스가 650달러 보다 작거나 보너스가 없는 사원들에게 상품권을 지급하려 합니다.
--해당 사원들의 이름과 보너스를 출력하세요.
SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE salary*commission_pct < 650; --4개 행 (commision_pct 있는(NULL이 아닌) 행을 대상)

SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE COALESCE(salary*commission_pct, 0) < 650; --76개 행 (0까지 포함)

-- LNNVL: LNNVL(expr1) expr1 결과가 FALSE 또는 UNKNOWN이면 TRUE를 반환
-- 조건의 반대 조건에 대하여 검색하고 싶을 때 활용
SELECT first_name, COALESCE(salary*commission_pct, 0) AS bonus
FROM employees
WHERE LNNVL(salary*commission_pct >= 650); --76개 행



-- DECODE: DECODE(Column or expression, search1, result
--                                      [, search2, result2, ...]
select decode('java','java','백엔드 언어') as language from dual;
select decode('java','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어') as language
from dual;

select decode('html','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어') as language
from dual;

select decode('python','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어') as language
from dual;

select decode('css','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어') as language
from dual;

select decode('css','java','백엔드 언어'
                    ,'html','프론트 언어'
                    ,'python','데이터사이언스 언어',
                    '기타언어') as language
from dual;

-- Q] 직원 테이블에서 직무 id, 급여 그리고 직무 id가 IT_PROG, FI_MGR, FT_ACCOUNT는 각각 급여를 10,15,20% 인상한 급여를 revised_salary 열에 출력한다.
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


-- 중첩함수
SELECT   ADD_MONTHS(hire_date, 6) -- 입사후 3개월
FROM     employees
ORDER BY hire_date;

SELECT   NEXT_DAY(ADD_MONTHS(hire_date, 6), '금') -- 다음 금요일
FROM     employees
ORDER BY hire_date;

SELECT   TO_CHAR(NEXT_DAY(ADD_MONTHS(hire_date, 6), '금'), 'YYYY-MM-DD') AS "정규직 논의 대상일" --의 날짜
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