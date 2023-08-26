<?php
    error_reporting(0);
    function fetch_backend($ip) {
        if(is_bad_ip($ip)) {
            return "This IP is not allowed!";
        }
        return file_get_contents("http://". $ip . "/");
    }
    function is_bad_ip($ip) {
        if(!preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $ip)) {
            // IP must be in X.Y.Z.Q format
            return true;
        }
        $frontend = gethostbyname(gethostname());
        $backend = gethostbyname("ipfilter_backend");
        $subnet = long2ip(ip2long($frontend) & ip2long("255.255.255.0"));
        $bcast = long2ip(ip2long($frontend) | ~ip2long("255.255.255.0"));

        if(isset($_GET['debug_filter'])) {
            echo "<pre>";
            echo "IP: " . $ip . "<br>";
            echo "Frontend: " . $frontend . "<br>";
            echo "Backend: " . $backend . "<br>";
            echo "Subnet:" . $subnet . "<br>";
            echo "Broadcast:" . $bcast . "<br>";
            echo  "</pre>";
        }

        if(inet_pton($ip) < (int) inet_pton($subnet)) {
            // Do not go below the subnet!
            return true;
        }
        if(! (inet_pton($ip) < inet_pton($bcast))) {
            // Do not go above the subnet!
            return true;
        }
        if($ip == $backend) {
            // Do not allow the backend with our secrets ;-)
            return true;
        }
        return false;
    }
    if(isset($_GET['fetch_backend']) ) {
        echo fetch_backend($_GET['bip']);
    }
    if(isset($_GET['src'])) {
        highlight_file(__FILE__);
    }
    // with <3 from @gehaxelt
?>