<?php

$user = new infinitt;

$name = $email = $hear_from =$checkbox= "";

if ($_SERVER["REQUEST_METHOD"] == "POST")
 {
  $name = test_input($_POST["name"]);
  $email = test_input($_POST["surname"]);
  $hear_from = test_input($_POST["hear_from"]);
  $checkbox = test_input($_POST["checkbox"]);
 
  $user -> set_name ("$user_name");
  $user -> set_surname ("$user_surname");
  $user -> set_hear_from ("$user_hear_from");
$user -> set_checkbox ("$user_checkbox");


  echo "Name :".$user -> get_name() ."<br>"; 
  echo "Surname :".$user -> get_surname() ."<br>"; 
  echo "Hear us from:".$user -> get_hear_from() ."<br>"; 
  echo "Like:".$user -> get_checkbox() ."<br>"; 


 }
/*
function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

   */       


  ?>

?>