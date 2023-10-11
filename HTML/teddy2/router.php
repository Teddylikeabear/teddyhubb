 <?php

namespace app\core; 

class Router
{
    public Request $request;
protected array $routes =[];

public function __construct(Request $request) 
    {
        $this ->request = $request;
    }

//handle submitted data
    public function get($path,$callback)
    {

        //callback as the associate array
$this ->routes['get'][$path]=$callback;
    }
public function resolve()
{
$this ->request ->getPath();
}

}

?>