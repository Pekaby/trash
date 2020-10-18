<?php
function debug($var = '')
{
    global $_SESSION;
    global $requests;
    global $_COOKIE;
    
    if ($var == '') {
        echo "<pre>";
        print_r($requests);
        echo "Path __DIR__: " . __DIR__ . "\n";
        echo "SESSION: ";
        var_dump($_SESSION);
        echo "COOKIE: ";
        print_r($_COOKIE);
        echo "</pre>";
    }else{
        echo "<pre>";
        print_r($var);
        echo "</pre>";
    }
}
