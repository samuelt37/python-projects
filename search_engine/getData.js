$(document).ready(function() {
    $("#search").click(function() {
		getData($("#term").val());
	});
});

function getData(term){
	$.ajax({
		type: 'POST',  
		url: "getData.php",
		data : {
			'term' : term
		},
		success: function(data){
        	console.log(data);
        	$("#links").empty();
        	$("#links").append(data);
    	}
    });
}