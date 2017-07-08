function post_data( data ){
	$.ajax({
		method	: 'post',
		url		: 'proto.py',
		data	: {'package' : JSON.stringify( data )},
		success	: function(result){
			result = JSON.parse(result);
			con('Received the following data from proto.py:');
			con(result);
		}
	})
}