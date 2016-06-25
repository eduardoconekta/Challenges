<?php
	$factor = $_POST['i1'];
	$res=1;
	for ($i=1; $i <= $factor ; $i++) { 
		$res*=$i;
		echo ">:".$res.'<br>';
	}

?>