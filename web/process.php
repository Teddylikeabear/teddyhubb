<!--<!DOCTYPE html>
<html>
<head>
    <title> Result</title>
</head>
<body>
    <h2> Form Output</h2>
    <?php
    
   /* if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $name = $_POST['name'];
        $surname = $_POST['surname'];
        $email = $_POST['email'];
        $placement = $_POST['placement'];
        $institution = $_POST['institution'];

        echo "<p>Name: $name</p>";
        echo "<p>Surname: $surname</p>";
        echo "<p>Email: $email</p>";
        echo "<p>Placement: $placement</p>";
        echo "<p>Institution: $institution</p>";
    
    } else {
        echo "<p>No data submitted.</p>";
    }
    */

      // formfile template setup
      $view = [
        'submit'
    ];

    $action = Helper::getUrlParam('view');

    if(! (array_key_exists('view',$_GET) && in_array($action, $view))){
        throw  new NotFoundException("View not found");  
    }
 // redirect loged in users
 if( isset($_SESSION['_userId'])){ 
    // can have a nav class that handles such requests

}
// user POST request 
$errors = [];
if( array_key_exists('submit', $_POST)){
    $data = [
        'name' => isset($_POST['user']['name'])?$_POST['user']['name'] :'',
        'surname' => isset($_POST['user']['surname'])?$_POST['user']['surname'] :'',
        'email' => isset($_POST['user']['email'])?$_POST['user']['email'] :'',
        'placement' => isset($_POST['user']['placement'])?$_POST['user']['placement'] :'',
        'institution' => isset($_POST['user']['institution'])?$_POST['user']['institution'] :''
    ];

    $errors = $obj->submit($data);
    if(empty($errors)){
        
    
        $obj = $user->selectProperties('email', $obj);

        if($obj->getName() != $data['name']){
            $errors[] = new ValidatorError('error', 'Incorrect Name / Email');
        }
        else{
            echo 'welcome';
            echo "<p>Name: $name</p>";
            echo "<p>Surname: $surname</p>";
            echo "<p>Email: $email</p>";
            echo "<p>Placement: $placement</p>";
            echo "<p>Institution: $institution</p>";
        
        }
    }
    else if( array_key_exists('cancel', $_POST)){
        Helper::redirect('.');
}

}
    ?>
</body>
</html>
-->