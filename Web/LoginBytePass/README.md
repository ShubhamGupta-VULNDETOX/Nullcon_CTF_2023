Loginbytes provided the opportunity to attempt logging in with the username `admin` or `flag`. In this case, the username was injected into the database query without any sanitization, while for the password it was double-hashed using md5 without being converted into a hexadecimal string.

At this point, looking at this portion of the code:
```php
<?php
function check_auth($username, $password)
{
    global $db;
    $username = mysqli_real_escape_string($db, $username); // preventSQLinjection
    $password = md5(md5($password, true), true);
    $res = mysqli_query($db, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
    if (isset($res) && $res->fetch_object()) {
        return true;
    }
    return false;
}
?>
```
My team and I managed to discover that by finding a hash containing the substring `first_part_of_hash'='second_part_of_hash`, we could bypass the login. This was because PHP transformed both the first and second parts of the hash into `0`, performed the comparison, and resulted in a query like this:
```sql
SELECT * FROM users WHERE username='admin' AND true
```
This allowed us to obtain the flag.
