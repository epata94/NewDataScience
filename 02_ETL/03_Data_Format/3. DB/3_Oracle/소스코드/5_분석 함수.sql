------------------------
--5�� �м��Լ�
------------------------
-- ����
--Analytic_Function 
--    OVER (PARTITION BY column_list
--        ORDER BY column_list [ASC|DESC] 
--        Windowing)

SELECT 
  first_name, salary, 
  -- RANK: �ش� ���� ���� �켱������ ����(�ߺ����� �����)
  RANK() OVER (ORDER BY salary DESC) AS rank,
  -- DENSE_RANK: �ش� ���� ���� �켱������ ����(�ߺ����� �����)
  DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank,
  -- CUME_DIST: �ִ밪 1�� �������� �л�� ���� ����
  ROUND(CUME_DIST() OVER (ORDER BY salary DESC), 5) AS cume_dist,
  -- �ִ밪 1�� �������� �����(Percent)���� ����
  -- ù ��° ��ġ�� 0���� �����ϰ� �� ��° row������ ��ġ�� (row�� rank-1) / (��ü row ���� -1)�� �˴ϴ�.
  -- rank�� �������� ������ rank�� ������ ��ü ��� �� %���� ǥ��
  ROUND(PERCENT_RANK() OVER (ORDER BY salary DESC), 5) AS percent,
  -- ��ü ������ ������ �տ��� ���� N�� �������� ������ ǥ��
  NTILE(4) OVER (ORDER BY salary DESC) AS ntile ,
  -- ROW_NUMBER: �˻������ ���� ���������� �ο��Ǵ� ���ȣ�� ��ȯ
  ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_number,
  -- ���� ���ڵ��� ���ȣ(�ǻ翭)
  ROWNUM
FROM employees;

-- skip (�ߺ�)
--RANK, DENSE_RANK, ROW_NUMBER
SELECT employee_id, department_id, salary,
    RANK()       OVER (ORDER BY salary DESC) sal_rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) sal_dense_rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC) sal_number
FROM   employees;

-- skip (�ߺ�)
--CUME_DIST, PERCENT_RANK
SELECT employee_id, department_id, salary,
    CUME_DIST()    OVER (ORDER BY salary DESC) sal_cume_dist,
    PERCENT_RANK() OVER (ORDER BY commission_pct DESC) sal_pct_rank
FROM   employees;

-- skip (�ߺ�)
--CUME_DIST, PERCENT_RANK
SELECT employee_id, department_id, salary,
    CUME_DIST()    OVER (ORDER BY salary DESC) sal_cume_dist,
    CUME_DIST()    OVER (ORDER BY commission_pct DESC) comml_cume_dist,
    PERCENT_RANK() OVER (ORDER BY salary DESC) sal_pct_rank,
    PERCENT_RANK() OVER (ORDER BY commission_pct DESC) comm_pct_rank
FROM   employees;

-- RATIO_TO_REPORT
-- �ش� �÷� ���� ������� �Ҽ������� ����
-- ��) ����
--      30 <- 0.3
--      50 <- 0.5
--      20 <- 0.2
SELECT first_name, salary, ROUND(RATIO_TO_REPORT(salary) OVER (), 4) AS salary_ratio
FROM employees
WHERE job_id='IT_PROG';

-- skip �ߺ�
SELECT employee_id, department_id, salary,
       NTILE(10)  OVER (ORDER BY salary DESC) sal_quart_tile
FROM   employees
WHERE  department_id=50;

-- LAG, LEAD
-- LAG([���̸�], [�������� �̵���],[���� ���� ��� ��ȯ��])
-- LEAD([���̸�], [���ķ� �̵���],[���� ���� ��� ��ȯ��])
SELECT employee_id, 
  LAG(salary, 1, 0) OVER (ORDER BY salary) AS lower_sal, 
  salary,
  LEAD(salary, 1, 0) OVER (ORDER BY salary) AS higher_sal 
FROM employees
ORDER BY salary;

-- LISTAGG
-- LISTAGG([��, ����], [������]) 
--    WITHIN GROUP(ORDER BY [���̸�])
-- �����Ǵ� ���� �����ڷ� join

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

-- PIVOT: ������ ������ ���� ���� �����͸� ������ �Ӽ����� ���� ����(���, �հ��)�ϰ� ���� ��Ÿ����.
-- �α׼� �����͸� �м��� �����ͷ� ��ȯ�ϴ� ����
-- SELECT
-- FROM
-- PIVOT(
--    �׷��Լ�(�������÷�)
--    for �ǹ������÷�
--    in (�ǹ��÷� ����);
--)
-- WHERE
-- ORDER BY
-- �ݵ�� �����Լ��� �־�� �Ѵ�. �����Լ��� ���� �������� wide ������ pivot ���̺��� ������� pivot �Լ� ���� 
-- case when then�� ����ؾ� �Ѵ�.
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

-- UNPIVOT: �������� ������ ������ ���� ���� �����͸� ������ ���� ����(Stack) ����
-- ���ռӼ��� ���� �Ӽ����� ��ȯ�ϴ� ����
-- ����
-- SELECT 
-- FROM
-- UNPIVOT
--(
--    [������ ���� �̸�: ���� �������� ���� ��Ÿ���� �̸�]
--    for [������ ���� �̸�: ���� �����Ϳ��� ������ ���� ���� Ư���� ��Ÿ���� �̸�]
--    in ([���ص������� ���մ��1],[���ص������� ���մ��2]..)
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