<?php
    define("LOADFLAG", true);
    error_reporting(0);
    function get_debug_info($filters) {
        ob_start(); phpinfo(); $pi = ob_get_contents(); ob_end_clean() ;
        $debug = array();
        foreach(explode(PHP_EOL, $pi) as $line) {
            if(strstr($line, $filters)) {
                array_push($debug, $line);
            }
        }
        return $debug;
    }
    if(isset($_GET['action']) && $_GET['action']=="debug") {
        $is_admin = $_SERVER['REMOTE_ADDR'] == "127.0.0.0" ? 1 : 0;
        $debug_info = get_debug_info(extract($_GET['filters']));
        if($is_admin) {
            echo implode($debug_info, '\n');
        } else {
            echo("Only local admins are allowed to debug!");
        }
        include_once "flag.php";
    }
    if(isset($_GET['action']) && $_GET['action']=="src") {
        highlight_file(__FILE__);
    }
    // With <3 from @gehaxelt.
?>
