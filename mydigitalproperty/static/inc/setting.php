<?php
	include "include/config.php";
	session_start();
	if(!isset($_SESSION['phone'])){
		header("Location: ../index.php");
	}
	else{
		
		  

$phone = $_SESSION['phone'];
	
	}

			
$sql=mysqli_query($con,"select * from authentication where phone='".$_SESSION['phone']."'");
$dat=mysqli_fetch_array($sql);

$fullname=$dat['fullname'];

		?>   