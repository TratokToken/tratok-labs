This is an example of code provided by HG showing how easy it is to leverage Tratok's translation engine in less than 20 lines of code.

Example code:

<?php
//Set your parameters
$request = "translate";
$id = ""; //insert your app id here
$secret = ""; //insert your secret here
$text = "Bonjour, pouvez-vouz m'aider? Je cherche la bibliothèque";
$originalLanguage = "fr";
$targetLanguage = "en";

//Construct the query with perl
$post = [
    'request' => $request,
    'id' => $id,
    'secret'   => $secret,
	'city'   => $text,
	'sourceLanguage'   => $originalLanguage,
	'targetLanguage'   => $targetLanguage,
];
$ch = curl_init('https://developer.tratok.net/data.php');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $post);

//Execute the request.
$response = curl_exec($ch);

//Close your conection
curl_close($ch);

//Output the data and use as required.
print_r($response);
?>

Response:

{"status":"Ok","originalLanguage":"fr","newLanguage":"en","originalMessage":"Bonjour, pouvez-vouz m'aider? Je cherche la biblioth\u00e8que","translatedMessage":"Hello, can you help me? I'm looking for the library"}
