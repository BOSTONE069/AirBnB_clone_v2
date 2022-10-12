-- Create database and user, grant user permissions without failing if either exists 
CREATE IF NOT EXISTS DATABASE hbnb_dev_db;
CREATE IF NOT EXISTS USER 'hbnb_dev'@'localhost' IDENTIFIED 
WITH authentication_plugin 
BY 'hbnb_dev_pwd';

GRANT PRIVILEGE ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGE ON performance_schema TO 'hbnb_dev'@'localhost';
