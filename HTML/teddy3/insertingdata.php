<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "dbteddy";

//creating a connection to database
$conn = new mysqli ($servername, $username, $password, $dbname);

//checking connection to database
if ($conn->connect_error){
    die("Connection failed : " . $conn->connect_error);
}


//inserting data in the employees table 

/*$sql = "INSERT INTO employees (empid , initials ,lastname ,age, email )
VALUES('999' , 'TC' ,' Marageni' , '22' , 'tcmarageni@gmail.com');";

$sql .= "INSERT INTO employees (empid , initials ,lastname ,age, email )
VALUES('998' , 'BS' , 'Shabalala' ,' 22' , 'bsshabalala@gmail.com');";

$sql .= "INSERT INTO employees (empid , initials ,lastname ,age, email )
VALUES('997' , 'BI' , 'Morakabi' ,' 23' , 'bcmorakabi@gmail.com');";

$sql .= "INSERT INTO employees (empid , initials ,lastname ,age, email )
VALUES('996' , 'TM' , 'Mudau' , '23' , 'tmmudau@gmail.com');";

$sql .="INSERT INTO employees (empid , initials , lastname , age , email)
VALUES('995', 'KM', 'Mofokeng', '24', 'kmmofokeng@gmail.com');";

$sql .="INSERT INTO employees(empid , initials , lastname , age , email)
VALUES('994', 'MM', 'Marageni', '13', 'mmmarageni@gmail.com');";

$sql .="INSERT INTO employees(empid , initials , lastname , age , email)
VALUES('993','TD','Madzaga','21','tdmadzaga@gmail.com');";


if ($conn->multi_query($sql)=== TRUE){
    echo "New records are created successfullly";
} else {
    echo "Error : " .$sql . "<br>" . $conn->error;
}


$conn->close();

?>
*/