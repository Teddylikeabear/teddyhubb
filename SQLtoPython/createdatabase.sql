--database name 
CREATE DATABASE teddyhubb; 

--database username and database password 
CREATE USER 'teddy'@'localhost' IDENTIFIED BY 'TeddyLikeabear2703@';

--grant previleges to users to use the databse
GRANT ALL PRIVILEGES ON teddyhubb.* TO 'teddy'@'localhost';

--run to applu changes 
FLUSH PRIVILEGES;
