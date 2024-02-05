<?php

echo "Hellow world";

// declaire variables and data types 
$name = "Teddy ";
$age = 50;
$isintern = true;

//operations 
$sum= $age + 5;
echo " After 5 years , $name wii be $sum years old.";

// if statements 
$mark = 45;
if ($grade >=70)
{
    echo "Pass";
}
else 
{
    echo "fail";
}

// for loop 
for($i = 1 ; $i <= 5 ; $i++)
{
    echo " Iteration $i <br>";
}

// define functions 
function greet($name)
{
    return "Hello, $name!";
}

//call function 
$message = greet ( "Teddy");
echo $message;

//indexted array
$colors = array ( "Purple" , "Black ", " Pink ");

//Associative array 
$person = array ("name "=> "Teddy" , "age" => 50 , "city"=> "Makhado " );

//Multidimentional array 
$matrix = array ( array(1,2,3), array(4,5,6));

//connecting to your database 

$servername = "localhost";
$username = "root"
$password = "";
$database = "teddyhubb";

$conn = new mysqli($servername, $username , $password ,$database );

if ($conn->connect_error)
{
die("connection failed : " . $conn->connect_error);
}
echo "Connected to the database successfully ";

//handling forms 

<form action="process_form.php" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username">
    
    <label for="password">Password:</label>
    <input type="password" id="password" name="password">
    
    <input type="submit" value="Submit">
</form>

//process_form 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
}

//database interaction 
//database query 

$query = "SELECT * FROM users ";
$result = $conn -> query($query);

if( $result -> num_rows > 0 )
{
    //output data of each row 
    while ($row = $reslt -> fetch_assoc())
    {
        echo "Name". $row {"name" }. ",Age : ". $row{"age"}. "<br>";
    }

}
else 
{
    echo"No results found";
}

//close the database connection 
$conn->close();

?>

