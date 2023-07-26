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
        'helper'=>'/model/model.php',

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
        require_once__DIR__.self :: $CLASS
    }
 

}

?>