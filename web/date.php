<!DOCTYPE html>
<html>
<body>

© 2023-
<?php

//copyright date
echo date("Y") ."<br>";

//create date and time
$d=strtotime("09:00am July 17 2023");
echo "Created date is " . date("Y-m-d h:i:sa", $d). "<br>";

//outputs date and time 
$d=strtotime("tomorrow");
echo date("Y-m-d h:i:sa", $d) . "<br>";

$d=strtotime("next Saturday");
echo date("Y-m-d h:i:sa", $d) . "<br>";

$d=strtotime("+3 Months");
echo date("Y-m-d h:i:sa", $d) . "<br>"; 

//outputs the next six Sundays
$startdate=strtotime("Saturday");
$enddate=strtotime("+6 weeks", $startdate);

while ($startdate < $enddate) {
  echo date("M d", $startdate) . "<br>";
  $startdate = strtotime("+1 week", $startdate);
}


//output number of days
$d1=strtotime("August 26");
$d2=ceil(($d1-time())/60/60/24);
echo "There are " . $d2 ." days until 26th of August.";


?>

</body>
</html>