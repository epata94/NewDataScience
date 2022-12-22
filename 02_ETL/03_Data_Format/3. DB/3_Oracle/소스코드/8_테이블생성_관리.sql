-- ���̺� ����
CREATE TABLE test_table (
   deptno  NUMBER(2),
   dname   VARCHAR2(14),
   loc     VARCHAR2(13) );
   
-- ���ʿ��� ���� ��ħ
   
-- ���̺� ��Ű�� ��ȸ
describe test_table;

insert into test_table
values(
    11,
    'IT����',
    '����'
);

select * from test_table;

-- �� �߰�
alter table test_table
add (job varchar2(10));

describe test_table;
select * from test_table;

-- �� �̸� ����
alter table test_table
rename column deptno to department_no;
alter table test_table
rename column dname to department_name;

describe test_table;

-- �� �Ӽ� ����
-- ũ�� �����ϴ� ���� ���� ������ �۰Դ� �ȵ�
alter table test_table
modify (department_name varchar2(20));
describe test_table;

-- �� ����
alter table test_table
drop column job;
describe test_table;
select * from test_table;

drop table test_table;