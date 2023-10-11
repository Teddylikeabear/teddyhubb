<?php

$user = new Processor;

if ($_SERVER[ 'REQUEST_METHOD'] === 'POST')
{
    $user_name = $_POST["name"];
    $user_surname = $_POST["surname"];
    $user_email = $_POST["email"];
    $user_placement = $_POST["placement"];
    $user_institution = $_POST["institution"];

$user -> set_name ("$user_name");
$user -> set_surname ("$user_surname");
$user -> set_email ("$user_email");
$user -> set_placement ("$user_placement");
$user -> set_institution ("$user_institution");
    
}


?>