
use flask_web_database;

show tables;

create table users(id int primary key auto_increment, 
					name varchar(50) not null, 
                    email varchar(50) not null unique, 
                    password varchar(300) not null,
                    details timestamp default now());


describe users;

select 
	*
from users;


drop table users;

