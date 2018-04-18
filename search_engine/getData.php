
<?php
	if(isset($_POST['term'])){
		$term = $_POST['term'];
	}

	$string = file_get_contents("WEBPAGES_CLEAN/bookkeeping.json");
	$jobj = json_decode($string, true);
	$links = "";

	$conn = new mysqli("127.0.0.1", "root", "", "termindex");
	$sql = "select docid from termindex where term = '".$term."' order by weight desc limit 5";

	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
	    // output data of each row
	    while($row = $result->fetch_assoc()) {
	        $links .= $jobj[$row['docid']]."<br>";
	    }
	}
	$conn->close();

	echo($links)
?>