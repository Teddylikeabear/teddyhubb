<!DOCTYPE html>
<html>
<head>
<script>

    fuction showUser(str){
        if (str==""){

            document.getElementById("txtHint").innerHTML="";
            return;
        }
        var xmlhttp=new
        XMLHttpRequest();

        xmlhttp.onreadystatechange=function(){
            if(this.readyState==4&&this.status==200){

                document.getElementById("txtHint").innerHTML=this.responseText;
            }
        }

        xmlhttp.open("GET","getuser.php?q="+str,true);
        xmlhttp.send();
    }
    </script>
    </head>
    <body>
        <form>
            <select name="user" onchange="showUser(this.value)">
            <option value ="">Select a person :</option>
            <option value ="1">Thendo Marageni</option>
            <option value ="2">Mavhungu Marageni</option>
            <option value ="3">Muelelwa Marageni</option>
            <option value ="4">Teddy Marageni</option>
            <option value ="5">Charmaine Marageni</option>

</select>
</form>
<br>
<div id="txtHint"><b>Person info will be listed here.</br></div>
</body>
</html>
     


