-- create a database and table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; 
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(256) NOT NULL,
);
