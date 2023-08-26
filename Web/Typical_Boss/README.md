### TYpical Boss
In this challenge, it was noticeable that if you accessed the main directory '/' of the challenge's website, the web server would render all the files and directories present on the page (including a file named `database.db`, which was an SQLite database).<br>
As soon as I found this file, I analyzed its contents until I discovered the hashed password of the admin. This hash (in SHA-1) started with a very famous prefix known for its vulnerabilities in PHP, namely `0e`.<br>
In fact, the password would be interpreted by PHP as a number, specifically `0`. The only way I had to bypass the login was to find a SHA-1 hash that also started with `0e`.<br>
This is one useful repository with a lot of these hashes: [Repository](https://github.com/spaze/hashes/tree/master)

### Debugger
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
