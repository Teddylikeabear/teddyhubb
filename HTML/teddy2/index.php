 <?php

require_once

//entry script that handles everthing
/*
echo "hello world";
*/
//create variable
$app= new Application(); 
/*
$router = new Router();
//comfig , when get is called it will execute the function
$router->get('/',function(){
    return 'Hellow world';
});

//tell app to use router
$app->userRouter($router);
*/
//or 
$app->router->get('/',function(){
    return 'Hellow world';
});

$app->router->get('/contact',function(){
    return 'contact';
});



//call run method to handle

$app->run();


 ?>
