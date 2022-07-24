function ajax (data) { //AJAX request
	$.ajax({ 
		cache: false,
		url: "/",
		type: 'POST',
		contentType: "application/json",
		dataType: "json",
		data: JSON.stringify(data),
		success: function(result) {
            $('#result').html(result)
        },
		error: function () {
			alert("Error retrieving search results, please refresh the page");
		}
	});
}
window.onload = function(){
    $('#main').submit((function (e) {

    e.preventDefault();
    d= {
            "sent1": $('#sent1').val(),
            "sent2": $('#sent2').val()
    };
    console.log(d);

    ajax(d)   

  }));
}

