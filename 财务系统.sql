create table employees(
eno number(7) not null PRIMARY KEY,
eaccount VARCHAR2(19) not null,
ename VARCHAR2(12) not null,
cnaps_code VARCHAR2(12) not null references bank(cnaps_code),
id number(10) not null references fdl_city(id),
email VARCHAR2(20),
phone VARCHAR2(17));

create table bank(
cnaps_code VARCHAR2(12) primary key,
bname VARCHAR2(20) not null,
branch VARCHAR2(80)not null);


CREATE TABLE fdl_city(
id number(10) not null PRIMARY KEY,
serial_no varchar2(25)  NOT NULL ,
l_name varchar2(50)  NOT NULL,
parent_id varchar2(25) NOT NULL ,
l_level number(4) NOT NULL
);

create table salary(
eno number(7) not null references employees(eno),
year_month date not null,
amount number(6),
primary key(eno,year_month));

create table payment(
Account VARCHAR2(19) not null primary key,
purposes VARCHAR2(10) not null,
Currency VARCHAR2(10),
branch VARCHAR2(50),
settlement_method VARCHAR2(4),
business_types varchar2(10)
);

insert into bank values(402191030498,'农村信用合作社','内蒙古呼和浩特金谷农村商业银行股份有限公司创业路分理处');
insert into payment values(471901379510902,'劳务收入','人民币','呼和浩特分行','普通');