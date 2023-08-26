<?php
define("LOADFLAG", true);
error_reporting(0);
$db = mysqli_connect('db', 'user', 'password', 'db');

function list_users()
{
    global $db;
    echo "<h1>Registeredusers:</h1>";
    $res = mysqli_query($db, "SELECT*FROMusers");
    while ($user = $res->fetch_object()) {
        echo "<p>";
        echo "User:" . $user->username . "Password:" . $user->password;
        echo "</p>";
    }
}
function check_auth($username, $password)
{
    global $db;
    $username = mysqli_real_escape_string($db, $username); //preventSQLinjection
    $password = md5(md5($password, true), true);
    $res = mysqli_query($db, "SELECT * FROM users WHERE username = '$username' AND password = '$password'");
    if (isset($res) && $res->fetch_object()) {
        return true;
    }
    return false;
}

if (check_auth($_POST['username'], $_POST['password'])) {
    include_once "flag.php";
}
list_users();

if (isset($_GET['src'])) {
    highlight_file(__FILE__);
}
//with<3from@gehaxelt
?>