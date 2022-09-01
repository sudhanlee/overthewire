<?php
	$a = readline("Enter encodedsecret: ");
	function decoder($s){
		return base64_decode((strrev(hex2bin($s))));
	}
	echo decoder($a);
?>