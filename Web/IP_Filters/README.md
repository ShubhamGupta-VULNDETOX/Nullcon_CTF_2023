This was IPFilters's source code:

```php
<?php
    function fetch_backend($ip) {
        if(is_bad_ip($ip)) {
            return "This IP is not allowed!";
        }
        return file_get_contents("http://". $ip . "/");
    }
    function is_bad_ip($ip) {
        if(!preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $ip)) {
            return true;
        }
        $frontend = gethostbyname(gethostname());
        $backend = gethostbyname("ipfilter_backend");
        $subnet = long2ip(ip2long($frontend) & ip2long("255.255.255.0"));
        $bcast = long2ip(ip2long($frontend) | ~ip2long("255.255.255.0"));

        if(isset($_GET['debug_filter'])) {
            // Debugging echos that also print the backend local IP
        }

        if(inet_pton($ip) < (int) inet_pton($subnet)) {
            return true;
        }
        if(! (inet_pton($ip) < inet_pton($bcast))) {
            return true;
        }
        if($ip == $backend) {
            return true;
        }
        return false;
    }
    if(isset($_GET['fetch_backend']) ) {
        echo fetch_backend($_GET['bip']);
    }
?>
```
Apparently, there don't seem to be any specific bypasses to perform. However, by analyzing each PHP function used in the program one by one, I discovered that `inet_pton` is vulnerable because it also accepts IPv4 addresses containing zeros in the last subset. For example: `xxx.xxx.x.00x`.<br>
In this way, I can fit the backend's IP address within the subnet range by passing it the same IP printed by the debug, with trailing zeros.<br>
For instance, `192.168.1.2` => `192.168.1.002`.
