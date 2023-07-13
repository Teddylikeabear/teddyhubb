
<!DOCTYPE html>
<html>
<body>

<?php
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

//select data from table
/*$sql = "SELECT empid, initials, lastname FROM employees ";
$result = $conn->query($sql);

//select WHERE clause
$sql = "SELECT empid, initials, lastname FROM employees WHERE lastname='Morakabi'";
$result = $conn->query($sql);*/

//select ORDER BY clause
/*$sql = "SELECT empid, initials, lastname FROM employees ORDER BY lastname";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> Employee id: ". $row["empid"]. " - Name: ". $row["initials"]. " " . $row["lastname"] . "<br>";
        
    }
  
} else {
    echo "0 results";
}*/

//delete record

$sql = "DELETE FROM employees WHERE empid=994";
if (mysqli_query($conn, $sql)) {
    echo "Record deleted successfully";
  } else {
    echo "Error deleting record: " . mysqli_error($conn);
  }


$conn->close();
?>

</body>
</html>
