
<!DOCTYPE html>
<html>
<body>

<?php
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
?>

</body>
</html>
