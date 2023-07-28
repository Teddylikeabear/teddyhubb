<?php

$user = new Processor;

if ($_SERVER[ 'REQUEST_METHOD'] === 'GET')
{
    $user_name = $_GET["name"];
    $user_surname = $_GET["surname"];
    $user_email = $_GET["email"];
    $user_placement = $_GET["placement"];
    $user_institution = $_GET["institution"];


    
}


?>