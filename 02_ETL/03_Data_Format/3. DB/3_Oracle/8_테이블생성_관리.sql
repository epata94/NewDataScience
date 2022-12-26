-- �׽�Ʈ�� ���̺� ����
create table test_table(
    deptno  number(2),
    dname   varchar2(14),
    loc     varchar2(13)
);


create table test_table(
    timestamp_min  timestamp,
    speed number(4)
);

insert into test_table
values(
    '202212231246',
    11
);
select * from test_table;
commit;
-- ���̺� ��Ű�� ��ȸ
DESCRIBE test_table;

-- ���� ������ �Է� �׽�Ʈ
insert into test_table
values(
    11,
    'IT����',
    '����'
);

select * from test_table;

-- ���̺��� �� �߰�
alter table test_table
add (job varchar2(10));

DESCRIBE test_table;

-- �� �̸� ����
alter table test_table
rename column deptno to department_no;
DESCRIBE test_table;

alter table test_table
rename column dname to department_name;
DESCRIBE test_table;

-- �� �Ӽ� ����
-- �������: ����� ũ�� �����ϴ� ���� ���� ������ �۰Դ� ����� �ȵ�.
alter table test_table
modify (department_name varchar2(20));
describe test_table;

-- �� ����
alter table test_table
drop column job;
describe test_table;

-- ���̺� ����
drop table test_table;
-- ��������� ���ΰ�ħ �Ǵ� Ctrl+R
describe test_table;