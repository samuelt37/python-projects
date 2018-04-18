<?php
	// require __DIR__ . '/vendor/autoload.php';
	require "vendor/autoload.php";
	// $client = new MongoDB("mongodb://127.0.0.1:27017");
	$client = new MongoDB\Client("mongodb://localhost:27017");

	if(isset($_POST['term'])){
		$term = $_POST['term'];
	}

	$string = file_get_contents("WEBPAGES_CLEAN/bookkeeping.json");
	$jobj = json_decode($string, true);
	$links = "";

	$m = new MongoClient();
	$db = $m->selectDB('termindex');
	// $collection = new MongoCollection($db, 'termindex');

	// search for fruits
	$termQuery = array($term => 1);

	$cursor = $collection->find($termQuery);
	foreach ($cursor as $doc) {
	    echo($doc);
	}

	// echo($links)
?>