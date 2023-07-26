<?php

class NotFoundException extends Exception {}

final class Index{

    const LAYOUT_DIR = '/layout';
    const PAGE_DIR = '/web';
    const LAYOUT_PAGE = 'index.phtml';
    const DEFAULT_PAGE = 'formfile';

    private static $CLASS = [
        'Processor'=> '/model/model.php',
        'NotFoundException' => 'index.php',
        'Helper'=>'/model/model.php'];

    //system config

    function __constuct(){
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
    public function loadclass($name)
    {
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
    return $this -> checkPage($page);
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

   private function hasScript($page){
    return file_exists($this -> getScript($page));
   }

   private function getScript($page){
    return__DIR__.self :: PAGE_DIR.$page.'';
   }

   private function hasTemplate($page){
    return file_exists($this->getTemplate($page));
   }

   private function getTemplate($page){
    return__DIR__.self ::PAGE_DIR.$page.'';
   }

   //RUN APPLICATION

   public function run(){
    $this -> runPage($this -> getPage());
   }
}

$index = new Index();
$index ->run();

?>