<?php
define('DB_SERVER','localhost');
define('DB_USER','root');
define('DB_PASS' ,'');
define('DB_NAME', 'frcnmain');
$con = mysqli_connect(DB_SERVER,DB_USER,DB_PASS,DB_NAME);
// Check connection
$domain = "http://localhost/paperless";

//Define sending email notification to webmaster

$email = 'mondabutu@gmail.com';
$subject = 'New user registration notification';
$from = 'From: Hospital Web Admin';

//Define Recaptcha parameters
$privatekey = "Your Recaptcha private key";
$publickey = "Your Recaptcha public key";

//Define length of salt,minimum=10, maximum=35
$length_salt = 15;

//Define the maximum number of failed attempts to ban brute force attackers
//minimum is 5
$maxfailedattempt = 5;

//Define session timeout in seconds
//minimum 60 (for one minute)
$sessiontimeout = 180;

////////////////////////////////////
//END OF USER CONFIGURATION/////////
////////////////////////////////////
//DO NOT EDIT ANYTHING BELOW!
if (mysqli_connect_errno())
{
 echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
?>