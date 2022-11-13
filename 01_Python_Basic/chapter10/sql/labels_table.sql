/*
"id": 76811,
"url": "https://api.github.com/repos/pandas-dev/pandas/labels/Bug",
"name": "Bug",
"color": "e10c02",
"default": false
*/

create or replace table labels(
id int not null,
url varchar(200) not null,
name varchar(50) not null,
color varchar(50) not null,
def char(5)
); 

commit; -- db 반영



