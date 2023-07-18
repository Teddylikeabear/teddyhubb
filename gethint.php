<?php
//array with names 
$a[] = "Thendo";
$a[] = "Mavhungu";
$a[] = "Collet";
$a[] = "Muelelwa";

//get the q parameter from URL
$b = $_REQUEST["b"];

$hint = "";

//look up all hints from array if $q is different from ""

if($b !== ""){
    $b = strtolower($b);
    $len = strlen($b);
    foreach($a as $name){
        if (stristr($b,substr($name,0,$len))){
            if ($hint === "") {
                $hint = $name;
            } else {
                $hint .= " , $name";
            }
        }
    }
}

//output 
echo $hint === "" ? "no suggestion" : $hint;
?>