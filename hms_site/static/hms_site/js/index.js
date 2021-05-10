function getRooms() {

	// remove options from select
	$('#id_room > option').remove();

	// get available rooms from api
	$.getJSON({
		url: '/api/available-rooms/',
		type: 'GET',
		dataType: 'json',
		data: {},
	})

	.done(function(data) {
		console.log("success");
		console.log(data);

		const rooms = JSON.parse(data.rooms);

		let select_el = $('#id_room')

		select_el.append(/*html*/`
			<option value selected>---------</option>
		`);

		rooms.forEach((item, index) => {

			const pk = item.pk;
			const name = item.fields.name;

			select_el.append(/*html*/`
				<option value="${pk}">${name}</option>
			`);
		});
	})

	.fail(function(error) {
		console.log("error");
		console.log(error.message);
	})

	.always(function() {
		console.log("ajax complete");
	});
}


jQuery(document).ready(function($) {
	
	getRooms();

});

[
	{
		"model": "hms_site.room", 
		"pk": 1, 
		"fields": {
			"name": "Room 0", 
			"price": 0, 
			"state": 0
		}
	}, 
	
	{
		"model": "hms_site.room", 
		"pk": 2, 
		"fields": {
			"name": "Room 1", 
			"price": 1, 
			"state": 0
		}
	}, 
	
	{
		"model": "hms_site.room", 
		"pk": 3, 
		"fields": {
			"name": "Room 2", 
			"price": 2, 
			"state": 0
		}
	}
]