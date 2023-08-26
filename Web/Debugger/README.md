Debugger to obtain the flag required your IP to be 127.0.0.0, which is not directly modifiable due to the fact that it used `$_SERVER['REMOTE_ADDR']`, using the following PHP code:
```php
<?php
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
?>
```
The vulnerability at this point lies in the PHP `extract()` function, which [imports variables](https://www.php.net/manual/en/function.extract.php) from an array into the current symbol table. My exploit, more precisely, involved overwriting the `$is_admin` variable with 1 by using the following payload in the GET request URL `/?action=debug&filters[is_admin]=1`<br> This way, I managed to obtain the flag.
