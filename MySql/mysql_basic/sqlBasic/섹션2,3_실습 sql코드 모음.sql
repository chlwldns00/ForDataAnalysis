CREATE DATABASE jiun;
USE jiun;
CREATE TABLE mytable (PRIMARY
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    modelnumber VARCHAR(15) NOT NULL,
    series VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
    );
SHOW TABLES;
desc mytable;

ALTER TABLE mytable MODIFY COLUMN name varchar(20) NOT NULL;
ALTER TABLE mytable CHANGE COLUMN modelnumber model_num varchar(15) NOT NULL;
ALTER TABLE mytable CHANGE COLUMN series model_type varchar(10) NOT NULL AUTO_INCREMENT;

desc mytable;

DROP TABLE mytable;
SHOW TABLES;
SHOW DATABASES;

USE mydb;
SHOW TABLES;
desc department;

ALTER TABLE mytable ADD COLUMN lowest_price INT UNSIGNED;

UPDATE mytable SET lowest_price = 347100 WHERE id = 1;

SELECT name, model_num FROM mytable WHERE lowest_price < 300000;



