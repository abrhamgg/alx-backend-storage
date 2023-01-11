-- script that creates a table
-- if table already exists the script shouldn't fail
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY  AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country ENUM('US','CO','TN') DEFAULT 'US'
);
