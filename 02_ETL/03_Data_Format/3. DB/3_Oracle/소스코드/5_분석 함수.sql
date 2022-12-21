------------------------
--5장 분석함수
------------------------
-- 문법
--Analytic_Function 
--    OVER (PARTITION BY column_list
--        ORDER BY column_list [ASC|DESC] 
--        Windowing)

SELECT 
  first_name, salary, 
  -- RANK: 해당 값에 대한 우선순위를 결정(중복순위 계산함)
  RANK() OVER (ORDER BY salary DESC) AS rank,
  -- DENSE_RANK: 해당 값에 대한 우선순위를 결정(중복순위 계산함)
  DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank,
  -- CUME_DIST: 최대값 1을 기준으로 분산된 값을 제공
  ROUND(CUME_DIST() OVER (ORDER BY salary DESC), 5) AS cume_dist,
  -- 최대값 1을 기준으로 백분율(Percent)값을 제공
  -- 첫 번째 위치가 0부터 시작하고 두 번째 row부터의 위치는 (row의 rank-1) / (전체 row 개수 -1)이 됩니다.
  -- rank를 기준으로 동일한 rank의 개수가 전체 대비 몇 %인지 표시
  ROUND(PERCENT_RANK() OVER (ORDER BY salary DESC), 5) AS percent,
  -- 전체 데이터 분포를 앞에서 부터 N개 구간으로 나누어 표시
  NTILE(4) OVER (ORDER BY salary DESC) AS ntile ,
  -- ROW_NUMBER: 검색결과에 따라 순차적으로 부여되는 행번호를 반환
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_number,
  -- 원래 레코드의 행번호(의사열)
  ROWNUM
FROM employees;

-- skip (중복)
--RANK, DENSE_RANK, ROW_NUMBER
SELECT employee_id, department_id, salary,
    RANK()       OVER (ORDER BY salary DESC) sal_rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) sal_dense_rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC) sal_number
FROM   employees;

-- skip (중복)
--CUME_DIST, PERCENT_RANK
SELECT employee_id, department_id, salary,
    CUME_DIST()    OVER (ORDER BY salary DESC) sal_cume_dist,
    PERCENT_RANK() OVER (ORDER BY commission_pct DESC) sal_pct_rank
FROM   employees;

-- skip (중복)
--CUME_DIST, PERCENT_RANK
SELECT employee_id, department_id, salary,
    CUME_DIST()    OVER (ORDER BY salary DESC) sal_cume_dist,
    CUME_DIST()    OVER (ORDER BY commission_pct DESC) comml_cume_dist,
    PERCENT_RANK() OVER (ORDER BY salary DESC) sal_pct_rank,
    PERCENT_RANK() OVER (ORDER BY commission_pct DESC) comm_pct_rank
FROM   employees;

-- RATIO_TO_REPORT
-- 해당 컬럼 값의 백분율을 소수점으로 제공
-- 예) 매출
--      30 <- 0.3
--      50 <- 0.5
--      20 <- 0.2
SELECT first_name, salary, ROUND(RATIO_TO_REPORT(salary) OVER (), 4) AS salary_ratio
FROM employees
WHERE job_id='IT_PROG';

-- skip 중복
SELECT employee_id, department_id, salary,
       NTILE(10)  OVER (ORDER BY salary DESC) sal_quart_tile
FROM   employees
WHERE  department_id=50;

-- LAG, LEAD
-- LAG([열이름], [이전으로 이동수],[값이 없을 경우 반환값])
-- LEAD([열이름], [이후로 이동수],[값이 없을 경우 반환값])
SELECT employee_id, 
  LAG(salary, 1, 0) OVER (ORDER BY salary) AS lower_sal, 
  salary,
  LEAD(salary, 1, 0) OVER (ORDER BY salary) AS higher_sal 
FROM employees
ORDER BY salary;

-- LISTAGG
-- LISTAGG([값, 구문], [구분자]) 
--    WITHIN GROUP(ORDER BY [열이름])
-- 수집되는 값을 구분자로 join

SELECT department_id, 
  LISTAGG(first_name, ',') WITHIN GROUP(ORDER BY hire_date) AS names
FROM employees
GROUP BY department_id;

--PIVOT, UNPIVOT
CREATE TABLE   sales_log(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  week_day     VARCHAR2(10),
  quantity     NUMBER(8,2)
); 

INSERT INTO sales_log values(1101, 4, 'SALES_MON', 100);
INSERT INTO sales_log values(1101, 4, 'SALES_TUE', 150);
INSERT INTO sales_log values(1101, 4, 'SALES_WED', 80);
INSERT INTO sales_log values(1101, 4, 'SALES_THU', 60);
INSERT INTO sales_log values(1101, 4, 'SALES_FRI', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_MON', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_TUE', 300);
INSERT INTO sales_log values(1102, 5, 'SALES_WED', 230);
INSERT INTO sales_log values(1102, 5, 'SALES_THU', 120);
INSERT INTO sales_log values(1102, 5, 'SALES_FRI', 150);
COMMIT;
SELECT * FROM sales_log;

SELECT SUM(quantity)
FROM   sales_log
WHERE  week_day='SALES_MON';

-- PIVOT: 행으로 나열된 여러 개의 데이터를 공통의 속성으로 묶어 집계(평균, 합계등)하고 열로 나타낸다.
-- 로그성 데이터를 분석용 데이터로 전환하는 과정
-- SELECT
-- FROM
-- PIVOT(
--    그룹함수(집계대상컬럼)
--    for 피벗기준컬럼
--    in (피벗컬럼 나열);
--)
-- WHERE
-- ORDER BY
-- 반드시 집계함수가 있어야 한다. 집계함수가 없는 형식으로 wide 형식의 pivot 테이블을 만들려면 pivot 함수 없이 
-- case when then을 사용해야 한다.
SELECT * 
FROM   sales_log
PIVOT
(
  sum(quantity)
  FOR week_day IN('SALES_MON' AS sales_mon, 
                  'SALES_TUE' AS sales_tue, 
                  'SALES_WED' AS sales_wed, 
                  'SALES_THU' AS sales_thu, 
                  'SALES_FRI' AS sales_fri)
)
ORDER BY employee_id, week_id;

-- unpivot
CREATE TABLE sales(
  employee_id  NUMBER(6),
  week_id      NUMBER(2),
  sales_mon    NUMBER(8,2),
  sales_tue    NUMBER(8,2),
  sales_wed    NUMBER(8,2),
  sales_thu    NUMBER(8,2),
  sales_fri    NUMBER(8,2)
);
INSERT INTO sales VALUES(1101, 4, 100, 150, 80,  60,  120);
INSERT INTO sales VALUES(1102, 5, 300, 300, 230, 120, 150);
COMMIT;
SELECT * FROM sales;

-- UNPIVOT: 여러개의 열으로 나열된 여러 개의 데이터를 공통의 열로 묶어(Stack) 나열
-- 복합속성을 단일 속성으로 전환하는 과정
-- 포멧
-- SELECT 
-- FROM
-- UNPIVOT
--(
--    [통합할 열의 이름: 기준 데이터의 값을 나타내는 이름]
--    for [통합할 열의 이름: 기준 데이터에서 나열된 열의 공통 특성을 나타내는 이름]
--    in ([기준데이터의 통합대상열1],[기준데이터의 통합대상열2]..)
--)
--where
--order by
SELECT employee_id, week_id, week_day, quantity
FROM   sales
UNPIVOT 
(
  quantity 
  FOR week_day 
  IN(sales_mon, sales_tue, sales_wed, sales_thu, sales_fri)
);