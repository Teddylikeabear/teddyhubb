
<?php
/*
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dbteddy";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
} 

// sql to create table
$sql = "CREATE TABLE employees (
empid INT(6)  PRIMARY KEY, 
initials VARCHAR(30) NOT NULL,
lastname VARCHAR(30) NOT NULL,
age INT(2) NOT NULL,
email VARCHAR(50)
)";

if ($conn->query($sql) === TRUE) {
  echo "Table Employees created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}


$conn->close();
?>
*/