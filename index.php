<?php

class NotFoundException extends Exception {

}

final class Index{

    const LAYOUY_DIR = '/layout';
    const PAGE_DIR = '/web';
    const LAYOUT_PAGE = 'index.php';
    const DEFAULT_PAGE = 'formfile';

    private static $CLASS = [
        'processor'=> '/model/model.php',
        'NotFoundException' => 'index.php',
        'helper'=>'/model/model.php'

    ];

    function__constuct(){
        //ERROR REPORTING DEVELOPMENT
        error_reporting(E_ALL | E_STRICT);
        mb_internal_encoding('UTF-8');
        //SET EXCEPTION HANDLER
spl_autoload_register([$this,'loadClass']);
//session handler setup
try{
    //$handler = new mysqlsessionHandler();
    //session_set_save_handler($handler)
    //session_start();

}catch(Exception $e){
    throw $e;
}

    }

    //CLASS LOADER
    public fuction loadclass($name){
        if (!array_key_exists($name, self ::$CLASS)){
            die('Class"'. $name .'" not found .');

        }
        require_once__DIR__.self :: $CLASS[$name];
    }

   private function runPage($page, array $extra = []){

    $run = false;
    if ($this -> hasScript($page)){
        $run = true;
        require $this->getScript($page);
    }
    if ($this-> hasTemplate($page)){
        $run = true;
        //data from main template 
        $template = $this -> getTemplate ($page);
        //main template (layout)
        require__DIR__.self::LAYOUT_DIR.self::LAYOUT_PAGE;
    }
    if (!$run){
        die('Page "'.$page . '"has neither script nor template ! ');

    }

   }
 
   private function getPage(){
    $page = self :: DEFAULT_PAGE;
    if (array_key_exists('page',$_GET)){
        $page = $_GET['page'];
    }
    return $this -> checkPage($page)
   }

   private function chechPage($page){
    if (!preg_match('/^[a-z0-9-]+$/i',$page)){
        //TODO LOG ATTEMPT , REDIRECT ATTACHER
        die('Unsafe page "'.$page . '" requested');
    }
    if (!$this -> hasScript($page)&& !$this -> hasTemplate($page)){
        //TODO LOG ATTEMPTT , REDIRECT ATTACKER
        die('Page "' .$page . '" not found ');
    }
    return $page;
   }

}

?>