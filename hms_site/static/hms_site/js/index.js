// $('#id_room')

jQuery(document).ready(function($) {
	
	// get available rooms from api
	$.ajax({
		url: '/api/available-rooms/',
		type: 'GET',
		dataType: 'json',
		data: {},
	})

	.done(function(data) {
		console.log("success");
		console.log(data);
	})

	.fail(function() {
		console.log("error");
	})

	.always(function() {
		console.log("ajax complete");
	});

});