create user pass_gen_admin password 'simplepass';

create database pass_gen_db encoding 'utf-8';
grant all privileges on database pass_gen_db to pass_gen_admin;
alter database pass_gen_db owner to pass_gen_admin;

create database pass_gen_test_db encoding 'utf-8';
grant all privileges on database pass_gen_test_db to pass_gen_admin;
alter database pass_gen_test_db owner to pass_gen_admin;