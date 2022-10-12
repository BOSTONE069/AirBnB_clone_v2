-- Create database and user, grant user permissions without failing if either exists 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED 
WITH authentication_plugin 
BY 'hbnb_test_pwd';

GRANT PRIVILEGE ON hbnb_test_db TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGE ON performance_schema TO 'hbnb_test'@'localhost';
