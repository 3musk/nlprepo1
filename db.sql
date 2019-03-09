drop database University;
create database university;
use university;

create table student
(rollno int(10),
name varchar(20),
phone varchar(10),
section char(1));

insert into student(rollno,name,phone,section) values("1000","Akrati","9876543210","A");
insert into student(rollno,name,phone,section) values("1001","Ankita","9876543211","D");
insert into student(rollno,name,phone,section) values("1002","Manika","9876543212","A");
insert into student(rollno,name,phone,section) values("1003","Sajal","9876543213","A");
insert into student(rollno,name,phone,section) values("1004","Akarsh","9876543214","B");
insert into student(rollno,name,phone,section) values("1005","Muskan","9876543215","B");
insert into student(rollno,name,phone,section) values("1006","Aditya","9876543216","B");
insert into student(rollno,name,phone,section) values("1007","Kajal","9876543217","D");
insert into student(rollno,name,phone,section) values("1008","Nikhil","9876543218","C");
insert into student(rollno,name,phone,section) values("1009","Nainka","9876543219","C");