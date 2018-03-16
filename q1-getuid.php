<?php
if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['challenger']))
{
    $who = trim($_POST['challenger']);
    $uid = hash_hmac("sha256", $who, "RecolicEncryptHead" + $who, false);
    echo("uid for $who is $uid.");
}
else
{
    die("invalid argument.");
}
?>