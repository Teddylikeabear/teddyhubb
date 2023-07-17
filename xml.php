
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
libxml_use_internal_errors(true);
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
}

?>

</body>
</html>
