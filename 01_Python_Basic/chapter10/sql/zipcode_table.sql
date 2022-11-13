-- code     city      gu         dong            detail
-- 135-806	서울		강남구	개포1동 경남아파트		1

create or replace table zipcode_tab(
code char(14) not null,
city varchar(15) not null,
gu varchar(20) not null,
dong varchar(60) not null,
detail varchar(60) 
);

select * from zipcode_tab;
select * from zipcode_tab where gu ='강남구';
commit work;