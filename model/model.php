<?php

final class Processor{
private $name;
private $surname;
private $email;
private $placement;
private $institution;

function __construct(){} 

public function setParam(stdClass $processor){

    if(array_key_exists('name', $processsor)){
        $this->name = $processsor->name;
    }

    if(array_key_exists('surname', $processsor)){
        $this->surname = $processsor->surname;
    }

    if(array_key_exists('email', $processsor)){
        $this->email = $processsor->email;
    }

    if(array_key_exist('placement', $processsor)){
        $this->placement = $processsor->placement;
    }

    if(array_key_exist('institution', $processsor)){
        $this->institution = $processsor->institution;
    }
}

public function register( array $processsor)
{
    $errors = [];

    if(trim($processsor['name'])){
        $this->name = $processsor['name'];
    }
    else{
        $errors[] = new ValidatorError('name','name cannot be empty');
    }

    if(trim($processsor['surname'])){
        $this->surname = $processsor['surname'];
    }
    else{
        $errors[] = new ValidatorError('surname','surname cannot be empty');
    }

    if(trim($processsor['email'])){
        $this->email = $processsor['email'];
    }
    else{
        $errors[] = new ValidatorError('email','email cannot be empty');
    }

    if(trim($processsor['placement'])){
        $this->placement = $processsor['placement'];
    }
    else{
        $errors[] = new ValidatorError('placement','placement cannot be empty');
    }
    
    if(trim($processsor['institution'])){
        $this->institution = $processsor['institution'];
    }
    else{
        $errors[] = new ValidatorError('institution','institution cannot be empty');
    } 

    return $errors;

}}
    final class Helper{ 	

        /**
         * Get value of the URL param.
         * @return string parameter value
         * @throws NotFoundException if the param is not found in the URL
         */
        public static function getUrlParam($name) {
            if (!array_key_exists($name, $_GET)) {
                throw new NotFoundException('URL parameter "' . $name . '" not found.');
            }
            return $_GET[$name];
        }
    
        /**
         * Redirect to the given page.
         * @param type $page target page
         * @param array $params page parameters
         */
        public static function redirect($page, array $params = []) {
            header('Location: ' . self::createLink($page, $params));
            die();
        }
    
        /**
         * Generate link.
         * @param string $page target page
         * @param array $params page parameters
         * @return 
         */
        public static function createLink($page, array $params = []) {
            unset($params['page']);
            return (empty($params))?$page :$page.'&'.http_build_query($params);
        }
    
        /**
         * Capitalize the first letter of the given string
         * @param string $string string to be capitalized
         * @return string capitalized string
         */
        public static function capitalize($string) {
            return ucfirst(mb_strtolower($string));
        }
    
        /**
         * Escape the given string
         * @param string $string string to be escaped
         * @return string escaped string
         */
        public static function escape($string) {
            return htmlspecialchars($string, ENT_QUOTES);
        }
    };
    
    final class User{

        private $name;
        private $surname;
        private $email;
        private $placement;
        private $institution;
    
        function __construct(){
    
        }
    
        public function setParam(stdClass $user){
    
    
            if(array_key_exists('name', $user)){
                $this->name = $user->name;
            }
    
            if(array_key_exists('surname', $user)){
                $this->surname = $user->surname;
            }
    
            if(array_key_exists('email', $user)){
                $this->email = $user->email;
            }

            if(array_key_exists('placement', $user)){
                $this->placement = $user->placement;
            }

            if(array_key_exists('institution', $user)){
                $this->institution = $user->institution;
            }
        }
    
    
    };

    final class ValidatorError {

        private $source;
        private $message;
    
        /**
         * Create new validation error.
         * @param mixed $source source of the error
         * @param string $message error message
         */
        function __construct($source, $message) {
            $this->source = $source;
            $this->message = $message;
        }
    
        /**
         * Get source of the error.
         * @return mixed source of the error
         */
        public function getSource() {
            return $this->source;
        }
    
        /**
         * Get error message.
         * @return string error message
         */
        public function getMessage() {
            return $this->message;
        }
    };


    
?>