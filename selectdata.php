
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

/*$sql = "SELECT empid, initials, lastname FROM employees ";
$result = $conn->query($sql);

$sql = "SELECT empid, initials, lastname FROM employees WHERE lastname='Morakabi'";
$result = $conn->query($sql);*/

$sql = "SELECT empid, initials, lastname FROM employees ORDER BY lastname";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> Employee id: ". $row["empid"]. " - Name: ". $row["initials"]. " " . $row["lastname"] . "<br>";
        
    }
  
} else {
    echo "0 results";
}

$conn->close();
?>

</body>
</html>
