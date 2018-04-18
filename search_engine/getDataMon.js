$(document).ready(function() {
    $("#search").click(function() {
		getData($("#term").val());
	});
});

function getData(term){
	$.ajax({
		type: 'get',  
		url: "getDataMon.php",
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