<?php
if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['challenger']))
{
    $who = trim($_POST['challenger']);
    $uid = hash("sha256", "RecolicEncryptHead$who");
    echo("uid for $who is $uid.");
}
else
{
    die("invalid argument.");
}
?>
