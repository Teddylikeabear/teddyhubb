
<!DOCTYPE html>
<html>
<head>
<script>
function showHint(str) {
  if (str.length == 0) {
    document.getElementById("txtHint").innerHTML = "";
    return;
  } else {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("txtHint").innerHTML = this.responseText;
      }
    }
    xmlhttp.open("GET", "gethint.php?q="+str, true);
    xmlhttp.send();
  }
}
</script>
</head>
<body>

<p><b>Start typing your details in the fields below:</b></p>
<form action="">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname" onkeyup="showHint(this.value)">
  <br><label for="surname">Surname:</label> 
  <input type="text" id="surname" name="surname" onkeyup="showHint(this.value)">
  <br><label for="email">Email:</label> 
  <input type="text" id="email" name="email" onkeyup="showHint(this.value)">
  <br><label for="intplc">Intern placement:</label> 
  <input type="text" id="intplc" name="intplc" onkeyup="showHint(this.value)">
  
</form>
<p>Suggestions: <span id="txtHint"></span></p>
<input type="text" id="suggestion" name="suggestion" onkeyup="showHint(this.value)">


</body>
</html>
