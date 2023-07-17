
<!DOCTYPE html>
<html>
<body>

<?php
/*
$myXMLData =
"<?xml version='1.0' encoding='UTF-8'?>
<note>
<to>Bongisiwe</to>
<from>Teddy</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>";

$xml=simplexml_load_string($myXMLData) or die("Error: Cannot create object");
print_r($xml);
*/

//error handling 
/*libxml_use_internal_errors(true);
$myXMLData =
"<?xml version='1.0' encoding='UTF-8'?>
<document>
<user>Thendo Marageni</wronguser>
<email>teddy@example.com</wrongemail>
</document>";

$xml = simplexml_load_string($myXMLData);
if ($xml === false) {
  echo "Failed loading XML: ";
  foreach(libxml_get_errors() as $error) {
    echo "<br>", $error->message;
  }
} else {
  print_r($xml);
}*/

//Initialize the XML parser
$parser=xml_parser_create();

//Function to use at the start of an element
function start($parser,$element_name,$element_attrs) {
    switch($element_name) {
        case "NOTE":
        echo "-- Note --<br>";
    break;
        case "TO":
        echo "To: ";
    break;
        case "FROM":
        echo "From: ";
    break;
        case "HEADING":
        echo "Heading: ";
    break;
        case "BODY":
        echo "Message: ";
    }
}


//Function to use at the end of an element
function stop($parser,$element_name) {
    echo "<br>";
}

//Function to use when finding character data
function char($parser,$data) {
    echo $data;
}
?>

</body>
</html>
