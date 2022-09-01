<?php

$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = 'qw8J'; 
    //Found the key by reversing the XOR with $key = cipher;
    //echo "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=" | base64 -d | hex
    //cipher = hex2bin("0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c");
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

echo base64_encode(xor_encrypt(json_encode($defaultdata)));

?>