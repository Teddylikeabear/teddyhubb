<?php

$user = new Processor;

if ($_SERVER[ 'REQUEST_METHOD'] === 'GET')
{
    $user_name = $_GET["name"];
    $user_surname = $_GET["surname"];
    $user_email = $_GET["email"];
    $user_placement = $_GET["placement"];
    $user_institution = $_GET["institution"];

$user -> set_name ("$user_name");
$user -> set_surname ("$user_surname");
$user -> set_email ("$user_email");
$user -> set_placement ("$user_placement");
$user -> set_institution ("$user_institution");
    
}


?>