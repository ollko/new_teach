$('#foto').ready(function() {

/*	$('a.thumbnail').click(function(e) {

    e.preventDefault();

    $('#image-modal .modal-body img').attr('src', $(this).find('img').attr('src'));

    $("#image-modal").modal('show');
});

	$('#image-modal .modal-body img').on('click', function() {
	$("#image-modal").modal('hide')
});
*/
	$("a.fancyimage").fancybox();
});
