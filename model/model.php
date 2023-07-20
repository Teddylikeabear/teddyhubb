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
?>