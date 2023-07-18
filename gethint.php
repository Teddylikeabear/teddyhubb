<?php
//array with names 
$a[]="Thendo";
$a[]="Mavhungu";
$a[]="Collet";

//get the q parameter from URL
$q=$_REQUEST["q"];

$hint="";

//look up all hints from array if $q is different from ""

if($q!==""){
    $q=strtolower($q);
    $len=strlen($q);
    
}
